package main

import (
	"bufio"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"sync"

	"gopkg.in/ini.v1"
)

// ================== CONFIGURATION ==================
const maxThreads = 10

// ===================================================

var logo = `
╔════════════════════════════════════╗
║ ·································· ║
║ :           ___      _       _   : ║
║ :  ___ ____/ _ \ ___(_)_ __ | |_ : ║
║ : / _ \_  / | | / __| | '_ \| __|: ║
║ :|  __// /| |_| \__ \ | | | | |_ : ║
║ : \___/___|\___/|___/_|_| |_|\__|: ║
║ ·································· ║
║ ...Version.2.0....Written.in.Go... ║
╚════════════════════════════════════╝
`

var (
	verbose    bool
	userAgent  = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15"
	resultFile = "./ezosint.results.txt"
)

type LinkCheck struct {
	URLTemplate string
	ValidString string
	ResolvedURL string
}

func colorBrightGreen(s string) string {
	return "\033[1;32m" + s + "\033[0m"
}

func colorBrightRed(s string) string {
	return "\033[1;31m" + s + "\033[0m"
}

func loadConfig() ([]LinkCheck, error) {
	cfg, err := ini.Load("config.ini")
	if err != nil {
		return nil, err
	}

	var checks []LinkCheck
	for _, section := range cfg.Sections() {
		if section.Name() == "DEFAULT" {
			continue
		}
		checks = append(checks, LinkCheck{
			URLTemplate: section.Key("url").String(),
			ValidString: section.Key("valid_string").String(),
		})
	}
	return checks, nil
}

func checkLink(lc LinkCheck, username string, wg *sync.WaitGroup, mu *sync.Mutex, semaphore chan struct{}) {
	defer wg.Done()
	semaphore <- struct{}{}        // Acquire slot
	defer func() { <-semaphore }() // Release slot

	url := strings.ReplaceAll(lc.URLTemplate, "{USER}", username)

	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("User-Agent", userAgent)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		if verbose {
			fmt.Println(colorBrightRed("Error accessing:"), url)
		}
		return
	}
	defer resp.Body.Close()

	bodyBytes, _ := io.ReadAll(resp.Body)
	body := string(bodyBytes)

	if strings.Contains(body, lc.ValidString) {
		output := fmt.Sprintf("[+] Valid: %s", url)
		fmt.Println(colorBrightGreen(output))

		mu.Lock()
		appendToFile(resultFile, fmt.Sprintf("%s\n", url))
		mu.Unlock()
	}
}

func appendToFile(filePath, text string) {
	f, err := os.OpenFile(filePath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		if verbose {
			fmt.Println(colorBrightRed("Error writing to result file"))
		}
		return
	}
	defer f.Close()

	if _, err := f.WriteString(text); err != nil && verbose {
		fmt.Println(colorBrightRed("Failed to write result"))
	}
}

func main() {
	help := flag.Bool("h", false, "Display help")
	flag.BoolVar(&verbose, "v", false, "Enable verbose output")
	flag.Parse()

	if *help {
		fmt.Println("Usage: ./ezosint")
		fmt.Println("Prompts for usernames, checks each link in config.ini")
		fmt.Println("Appends valid results to ./ezosint.results.txt")
		fmt.Println("Options:\n  -h  Show help\n  -v  Verbose output")
		return
	}

	fmt.Println("\033[1;94m" + logo + "\033[0m")
	fmt.Print("Enter username(s) (comma-separated): ")
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	usernames := strings.Split(strings.TrimSpace(input), ",")

	links, err := loadConfig()
	if err != nil {
		fmt.Println(colorBrightRed("Failed to read config.ini"))
		os.Exit(1)
	}

	semaphore := make(chan struct{}, maxThreads) // Thread limit control

	for _, username := range usernames {
		username = strings.TrimSpace(username)
		fmt.Printf("\nChecking: %s\n", colorBrightGreen(username))

		var wg sync.WaitGroup
		var mu sync.Mutex

		for _, link := range links {
			wg.Add(1)
			go checkLink(link, username, &wg, &mu, semaphore)
		}
		wg.Wait()
	}
}

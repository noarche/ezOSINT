import configparser
import requests
import os
from colorama import Fore, Style, init
from datetime import datetime
import time

main_logo = '''


\033[92m███████╗███████╗ ██████╗ ███████╗██╗███╗   ██╗████████╗\033[0m
\033[92m██╔════╝╚══███╔╝██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝\033[0m
\033[92m█████╗    ███╔╝ ██║   ██║███████╗██║██╔██╗ ██║   ██║   \033[0m
\033[92m██╔══╝   ███╔╝  ██║   ██║╚════██║██║██║╚██╗██║   ██║   \033[0m
\033[92m███████╗███████╗╚██████╔╝███████║██║██║ ╚████║   ██║   \033[0m
\033[92m╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   \033[0m
                                                       
                                                          
      \033[95m****************************\033[0m
      \033[96m github.com/noarche/ezOSINT \033[0m
      \033[94m     Username Recon         \033[0m
      \033[95m****************************\033[0m

   \033[94m  Please push your edits if you add to the config.ini\nAlways get the latest update from the repo.\033[0m

'''

print(main_logo)

# Initialize colorama
init(autoreset=True)

def read_config():
    # Create a ConfigParser instance with no interpolation
    config = configparser.ConfigParser(interpolation=None)
    config.read('config.ini')
    
    links_with_valid_strings = []
    for section in config.sections():
        url = config.get(section, 'url')
        valid_string = config.get(section, 'valid_string')
        links_with_valid_strings.append((url, valid_string))
    
    return links_with_valid_strings

def fetch_content(url):
    try:
        response = requests.get(url, timeout=5)  # Set a timeout of 5 seconds
        # Handle specific status codes quietly
        if response.status_code in (404, 403, 405, 410, 406, 503):
            return ""
        response.raise_for_status()  # Raise other HTTP errors
        return response.text
    except requests.RequestException:
        # Suppress error messages for handled status codes
        return ""

def check_validity(content, valid_string):
    return valid_string in content

def log_result(user, url, valid_string):
    with open("results.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | {user} | {url} | {valid_string}\n")

def process_url(url, valid_string, user):
    formatted_url = url.format(USER=user)
    content = fetch_content(formatted_url)
    if check_validity(content, valid_string):
        print(Fore.GREEN + f"\nValid content found at {formatted_url}")
        log_result(user, formatted_url, valid_string)
    else:
        print(Fore.CYAN + f"\rChecking {formatted_url}... ", end="")

def main():
    links_with_valid_strings = read_config()
    user = input(Fore.CYAN + "Input Target USERNAME: ")

    for url, valid_string in links_with_valid_strings:
        process_url(url, valid_string, user)
        
    print(Fore.RESET + "\nAll tasks completed.")

    rerun = input(Fore.RED + "\nWould you like to run again? (yes/no): ").strip().lower()
    if rerun == 'yes':
        main()
    else:
        print(Fore.RED + "Exiting...")

if __name__ == "__main__":
    main()
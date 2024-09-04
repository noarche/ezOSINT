import configparser
import requests
import os
from colorama import Fore, Style, init
from datetime import datetime
import time

init(autoreset=True)

def read_config():
    config = configparser.ConfigParser(interpolation=None)
    config.read('config.ini')
    
    links_with_valid_strings = []
    for section in config.sections():
        url = config.get(section, 'url')
        valid_strings = config.get(section, 'valid_string').split(';')  
        links_with_valid_strings.append((url, valid_strings))
    
    return links_with_valid_strings

def fetch_content(url):
    try:
        response = requests.get(url, timeout=3)
        
        if response.status_code in (404, 403, 405, 410, 406, 503):
            return ""
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return ""

def check_validity(content, valid_strings):
    
    for valid_string in valid_strings:
        if valid_string in content:
            return True
    return False

def log_result(user, url, valid_strings):
    with open("results.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | {user} | {url}\n")

def process_url(url, valid_strings, user):
    formatted_url = url.format(USER=user)
    content = fetch_content(formatted_url)
    if check_validity(content, valid_strings):
        print(Fore.GREEN + f"\nValid content found at {formatted_url}")
        log_result(user, formatted_url, valid_strings)
    else:
        print(Fore.CYAN + f"\rChecking {formatted_url}... ", end="")

def main():
    links_with_valid_strings = read_config()
    users = input(Fore.CYAN + "Input Target USERNAMES (separated by commas): ")
    user_list = [user.strip() for user in users.split(',')]

    for user in user_list:
        for url, valid_strings in links_with_valid_strings:
            process_url(url, valid_strings, user)
    
    print(Fore.RESET + "\nAll tasks completed.")

    rerun = input(Fore.RED + "\nWould you like to run again? (yes/no): ").strip().lower()
    if rerun == 'yes':
        main()
    else:
        print("Exiting the script. Goodbye!")

if __name__ == "__main__":
    main()

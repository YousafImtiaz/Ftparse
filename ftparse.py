#!/usr/bin/python3

import pexpect
import sys

def print_blue_banner():
    # Brighter blue color using ANSI escape codes
    print("\033[1;34mFtparse\033[0m")

def ftp_auto_login(ip):
    try:
        print(f"Trying anonymous login on {ip}")  # Removed the extra newline
        
        # Start the FTP client
        ftp = pexpect.spawn(f"ftp {ip}")
        
        # Handle the login process
        ftp.expect("Name .*: ")
        ftp.sendline("anonymous")
        ftp.expect("Password: ")
        ftp.sendline("anonymous")
        
        # Hand over control to the user
        print("Anonymous login successful!")  # Removed the extra newline
        ftp.interact()  # Provides direct terminal interaction
    except KeyboardInterrupt:
        print("\nSession terminated by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print_blue_banner()  # Print the banner first

    if len(sys.argv) != 2:
        print("Usage: ./ftparse.py <IP>")
        sys.exit(1)

    target_ip = sys.argv[1]
    ftp_auto_login(target_ip)

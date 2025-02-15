#!/usr/bin/python3

import pexpect
import sys

def print_blue_banner():
    # Brighter blue color using ANSI escape codes
    print("\033[1;34mFtparse\033[0m")

def ftp_auto_login(ip, port):
    try:
        print(f"Trying anonymous login on {ip}:{port}")
        
        # Start the FTP client with the specified port
        ftp = pexpect.spawn(f"ftp {ip} {port}")
        
        # Handle the login process
        ftp.expect("Name .*: ")
        ftp.sendline("anonymous")
        ftp.expect("Password: ")
        ftp.sendline("anonymous")
        
        # Hand over control to the user
        print("Anonymous login successful!")
        ftp.interact()  # Provides direct terminal interaction
    except KeyboardInterrupt:
        print("\nSession terminated by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print_blue_banner()
    
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: ./ftparse.py <IP> [PORT]")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    target_port = sys.argv[2] if len(sys.argv) == 3 else "21"  # Default to port 21
    
    ftp_auto_login(target_ip, target_port)

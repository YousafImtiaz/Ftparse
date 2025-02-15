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
        ftp = pexpect.spawn(f"ftp {ip} {port}", encoding='utf-8', timeout=10)
        
        # Handle the login process
        ftp.expect("Name .*: ")
        ftp.sendline("anonymous")
        ftp.expect("Password: ")
        ftp.sendline("anonymous")
        ftp.expect("ftp>")
        
        # Print success message before running commands
        print("Anonymous login successful!")
        
        # Run 'pwd' command automatically after logging in
        ftp.sendline("pwd")
        ftp.expect("ftp>")
        pwd_output = ftp.before.strip()
        print(pwd_output)
        
        # Run 'ls' command automatically after logging in
        ftp.sendline("ls")
        ftp.expect("ftp>")
        ls_output = ftp.before.strip()
        
        # Check if 'ls' command returned an empty response or access denied
        if not ls_output or "access denied" in ls_output.lower():
            print("No files found or access denied.")
        else:
            print(ls_output)  # Print the directory listing without extra spaces
        
        # Ensure smooth transition to interactive mode
        ftp.sendline("")
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

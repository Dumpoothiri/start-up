#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m
┌──────────────────────────────────────────────────┐
│    ███████╗████████╗ █████╗ ██████╗ ████████╗    │
│    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝    │
│    █████╗     ██║   ███████║██████╔╝   ██║       │
│    ██╔══╝     ██║   ██╔══██║██╔═══╝    ██║       │
│    ███████╗   ██║   ██║  ██║██║        ██║       │
│    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝        ╚═╝       │
│        START-UP: The One-Click Installer         │
│                 Author: Dumpoothiri              │
└──────────────────────────────────────────────────┘
''')

print("\033[96m\nLoading...\033[0m")
time.sleep(1)

print('''\033[92m
"Now I am become Death, the destroyer of worlds."
- Lord Krishna (Bhagavad Gita)
\033[0m''')
print("\033[95m\nAuthor: Dumpoothiri\n\033[0m")

for i in range(0, 101, 5):
    sys.stdout.write(f"\r\033[93mLoading... {i}%\033[0m")
    sys.stdout.flush()
    time.sleep(0.1)
sys.stdout.write("\n")

print('''\033[93m
Choose a category to install the relevant packages:
[01] Programmer
[02] Hacker
[03] Pen Tester
[04] Basic Utilities
[05] Install All Packages
[00] Exit
''')

category = input("\033[93mEnter your choice: ")

if category == '01':
    print("\033[92mSetting up your terminal for Programmer mode...\033[0m")
    time.sleep(1)
    print("\033[92mStarting installation... Great code requires patience!\033[0m")
    os.system("apt update && apt upgrade -y")
    os.system("apt install python python2 python3 java git ruby clang perl -y")
    print("\033[92mProgramming packages installed successfully!\033[0m")

elif category == '02':
    print("\033[92mSetting up your terminal for Hacker mode...\033[0m")
    time.sleep(1)
    print("\033[92mStarting installation... Hackers don't rush; they strategize!\033[0m")
    os.system("apt update && apt upgrade -y")

    hacker_packages = [
        "python", "python2", "python-dev", "python3", "php", "java", "git", "perl", "bash", 
        "nano", "curl", "openssl", "openssh", "wget", "clang", "nmap", "w3m", 
        "hydra", "ruby", "macchanger", "host", "dnsutils", "coreutils", "sqlmap", "metasploit", 
        "zsh", "nikto", "netcat"
    ]
    
    for i, pkg in enumerate(hacker_packages, start=1):
        os.system(f"apt install {pkg} -y")
        if i % 5 == 0:
            print("\033[93mPatience is key; real hackers wait while greatness is installed...\033[0m")
            time.sleep(1)

    print("\033[92mHacking packages installed successfully! Your terminal is now hacker-ready!\033[0m")

elif category == '03':
    print("\033[92mSetting up your terminal for Pen Tester mode...\033[0m")
    time.sleep(1)
    print("\033[92mStarting installation... Precision is the pen tester's weapon!\033[0m")
    os.system("apt update && apt upgrade -y")
    os.system("apt install dnsutils host php perl clang nikto netcat -y")
    print("\033[92mPen Testing packages installed successfully!\033[0m")

elif category == '04':
    print("\033[92mSetting up your terminal with Basic Utilities...\033[0m")
    time.sleep(1)
    print("\033[92mStarting installation... A solid foundation builds greatness!\033[0m")
    os.system("apt update && apt upgrade -y")
    os.system("apt install nano openssl wget coreutils -y")
    print("\033[92mBasic utilities installed successfully!\033[0m")

elif category == '05':
    print("\033[92mSetting up your terminal for All Packages...\033[0m")
    time.sleep(1)
    print("\033[92mStarting installation... You're building an empire here!\033[0m")
    os.system("apt update && apt upgrade -y")
    os.system("apt install python python2 python3 java git ruby clang perl nmap hydra macchanger w3m openssh curl sqlmap metasploit zsh dnsutils host php nikto netcat nano openssl wget coreutils -y")
    print("\033[92mAll packages installed successfully!\033[0m")

elif category == '00':
    print("\033[91mExiting... Have a great day!\033[0m")
    sys.exit()

else:
    print("\033[91mInvalid choice! Please restart the script.\033[0m")
    sys.exit()

print("\033[96mFollow me on Instagram for more tools and updates: @dumpoothiri\033[0m")

input("\033[93mPress Enter to return to home directory...\033[0m")
os.chdir(os.environ['HOME'])
print("\033[92mYou are now back to your home directory. Thank you for using Start-Up! 😁\033[0m")
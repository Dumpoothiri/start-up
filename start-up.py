#!/usr/bin/python3
import os
import time
import sys
import random

# Clear the terminal
os.system("clear")

# Hacker-themed ASCII art header
print('''\033[92m
░█▀▀░▀█▀░█▀█░█▀▄░▀█▀░░░░░█░█░█▀█
░▀▀█░░█░░█▀█░█▀▄░░█░░▄▄▄░█░█░█▀▀
░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░░░░░▀▀▀░▀░░
 START-UP: The One-Click Installer
    Author: Dumpoothiri
------------------------------------------------
\033[0m''')

# Loading animation
print("\033[96mLoading...\033[0m")
time.sleep(1)

# Random motivational quotes from Sanatana Dharma
quotes = [
    "\"I am time, the great destroyer of the world, and I have come here to destroy all people.\" - Bhagavad Gita 11.32",
    "\"For the protection of the good and the destruction of the wicked, I come into being age after age.\" - Bhagavad Gita 4.8",
    "\"Whatever action you do, make it an offering to me.\" - Bhagavad Gita 9.27",
    "\"Those who worship me with devotion, meditating on my transcendental form, to them I carry what they lack and preserve what they have.\" - Bhagavad Gita 9.22",
    "\"The soul is neither born, and nor does it ever die; it is eternal, indestructible, and timeless.\" - Bhagavad Gita 2.20"
]

# Display random quote
print(f"\033[92m\n{random.choice(quotes)}\033[0m\n")
time.sleep(2)

# Options menu
print('''\033[93m
Choose a category to install the relevant packages:
[01] Programmer Mode
[02] Hacker Mode
[03] Pen Tester Mode
[04] Basic Utilities
[05] Install All Packages
[00] Exit
''')

# Input choice
category = input("\033[93mEnter your choice: ")

# Helper function to install packages
def install_packages(packages):
    for i, pkg in enumerate(packages, start=1):
        os.system(f"apt install {pkg} -y")
        if i % 5 == 0:
            print("\033[93mInstalling... Please wait...\033[0m")
            time.sleep(1)

# Handle choices
if category == '01':
    print("\033[92mSetting up Programmer mode...\033[0m")
    time.sleep(1)
    os.system("apt update && apt upgrade -y")
    install_packages(["python", "python2", "python3", "java", "git", "ruby", "clang", "perl"])
    print("\033[92mProgrammer mode setup complete!\033[0m")

elif category == '02':
    print("\033[92mSetting up Hacker mode...\033[0m")
    time.sleep(1)
    os.system("apt update && apt upgrade -y")
    install_packages([
        "python", "python2", "python3", "php", "java", "git", "perl", "nano", "curl",
        "openssl", "openssh", "wget", "clang", "nmap", "hydra", "ruby", "macchanger",
        "host"
    ])
    print("\033[92mHacker mode setup complete!\033[0m")

elif category == '03':
    print("\033[92mSetting up Pen Tester mode...\033[0m")
    time.sleep(1)
    os.system("apt update && apt upgrade -y")
    install_packages(["dnsutils", "host", "php", "perl", "clang", "nikto", "netcat"])
    print("\033[92mPen Tester mode setup complete!\033[0m")

elif category == '04':
    print("\033[92mSetting up Basic Utilities...\033[0m")
    time.sleep(1)
    os.system("apt update && apt upgrade -y")
    install_packages(["nano", "openssl", "wget", "coreutils"])
    print("\033[92mBasic utilities installed successfully!\033[0m")

elif category == '05':
    print("\033[92mSetting up All Packages...\033[0m")
    time.sleep(1)
    os.system("apt update && apt upgrade -y")
    install_packages([
        "python", "python2", "python3", "java", "git", "ruby", "clang", "perl", "nmap", 
        "hydra", "macchanger", "w3m", "openssh", "curl", "sqlmap", "metasploit", "zsh", 
        "dnsutils", "host", "php", "nikto", "netcat", "nano", "openssl", "wget", "coreutils"
    ])
    print("\033[92mAll packages installed successfully!\033[0m")

elif category == '00':
    print("\033[91mExiting... May Lord Vishnu guide your path!\033[0m")
    sys.exit()

else:
    print("\033[91mInvalid choice! Please restart the script.\033[0m")
    sys.exit()

print("\033[96mFollow me on Instagram for more tools and updates: @dumpoothiri\033[0m")

input("\033[93mPress Enter to return to the home directory...\033[0m")
os.chdir(os.environ['HOME'])
print("\033[92mYou are now back to your main directory. Thank you for using Start-Up!\033[0m")

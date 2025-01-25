# Start-Up: One-Click Installer for Termux

**Author:** Dumpoothiri  
**Instagram:** [@dumpoothiri](https://www.instagram.com/dumpoothiri)

[![GitHub stars](https://img.shields.io/github/stars/yourusername/start-up?style=social)](https://github.com/yourusername/start-up/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/start-up?style=social)](https://github.com/yourusername/start-up/network)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/start-up)](https://github.com/yourusername/start-up/issues)
[![License](https://img.shields.io/github/license/yourusername/start-up)](https://github.com/yourusername/start-up/blob/main/LICENSE)
[![Python version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Termux compatibility](https://img.shields.io/badge/Termux-✔️-green.svg)](https://termux.com)

![Logo](https://img.icons8.com/ios-filled/50/000000/hacker.png)

---

## About

Welcome to **Start-Up**, your one-click installer for **Termux**. This tool is designed for Termux users who want to quickly set up their environment for various tasks such as programming, ethical hacking, and penetration testing. With just a few commands, you can install all the essential packages for your desired category.

---

## 🚀 Features
- **Easy-to-use installation script** for quick setup
- Categorized packages for different tasks:
  - **Programmer Mode**
  - **Hacker Mode**
  - **Pen Tester Mode**
  - **Install All Packages**
- One-click install for a variety of tools
- **Beautiful Terminal UI** with hacker-style loading screen and quotes
- Designed for **Termux** on Android

---

## 📦 Categories

Choose from the following categories for your Termux setup:

- **Programmer Mode**
- **Hacker Mode**
- **Pen Tester Mode**
- **Install All Packages**

---

## 📋 Package Details

The following packages are installed depending on the category selected:

### 1. **Programmer Mode**
   - `python`, `python2`, `python3`, `java`, `git`, `ruby`, `clang`, `perl`

### 2. **Hacker Mode**
   - `python`, `python2`, `python-dev`, `python3`, `php`, `java`, `git`, `perl`, `bash`, `nano`, `curl`, `openssl`, `openssh`, `wget`, `clang`, `nmap`, `w3m`, `hydra`, `ruby`, `macchanger`, `host`, `dnsutils`, `coreutils`, `sqlmap`, `metasploit`, `zsh`, `nikto`, `netcat`

### 3. **Pen Tester Mode**
   - `dnsutils`, `host`, `php`, `perl`, `clang`, `nikto`, `netcat`

### 4. **Basic Utilities**
   - `nano`, `openssl`, `wget`, `coreutils`

### 5. **Install All Packages**
   - All packages from the categories above

---

## 🧑‍💻 Installation Steps

### 1. **Install Termux on Your Android Device**  
   Download and install Termux from [F-Droid](https://f-droid.org/packages/com.termux/).

### 2. **Clone the Repository**  
   Open Termux and execute the following commands to clone the repository:
   ```bash
   pkg update
   pkg install git -y
   git clone https://github.com/dumpoothiri/start-up.git
   cd start-up
   python start-up.py
   
   
   
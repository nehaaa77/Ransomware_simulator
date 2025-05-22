# 🛡️ Secure Ransomware Simulator

![Build](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-purple?style=for-the-badge&logo=open-source-initiative)

> 🎓 **Educational Only** – This ransomware simulator is designed for cybersecurity training, CTFs, and ethical testing in sandboxed environments.

---

## 🎬 Live Demo GIF

> _Here's how it runs on terminal!_

![ransomware-demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWZ6bzR6Y3VtYmoxOGdnczM1cWxhcDk4emZyY2R3cTNraXpvOThwbiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l3vRlGpqgxXvvWm8c/giphy.gif)

---

## 📂 Features

✅ Safe & sandboxed  
✅ AES-256 encryption via `cryptography`  
✅ Auto-generates encryption key  
✅ Drops a ransom note  
✅ Allows easy decryption  
✅ Console-based menu UI  
✅ Realistic metadata tracking (time, machine ID)

---

## 💻 Folder Structure

```

project/
│
├── victim\_folder/         # Folder where files will be encrypted
├── unlock\_key.txt         # Stores generated key & metadata
├── !!!READ\_ME!!!.txt      # Ransom note after encryption
└── ransome\_simulator.py   # Main simulator script

````

---

## 🧠 How It Works

### 1. `generate_complex_key()`
Creates an encryption key with timestamp and machine details.

### 2. `encrypt_folder()`
Encrypts all files in the victim folder and deletes originals.

### 3. `create_ransom_note()`
Drops a ransom note with key, BTC wallet, and recovery instructions.

### 4. `decrypt_folder()`
Decrypts `.encrypted` files back to their original state using the saved key.

---

## 🛠️ Usage

> ⚠️ Use in a controlled sandbox environment only. Do **not** run on real user files.

```bash
# 1. Clone this repo
git clone https://github.com/yourusername/ransomware-simulator.git

# 2. Navigate to project
cd ransomware-simulator

# 3. Install dependencies
pip install cryptography

# 4. Run the simulator
python ransome_simulator.py
````

---

## 📸 Screenshots

> Encrypting files with animation:

```
███████╗██╗   ██╗██████╗ ██╗   ██╗███╗   ███╗███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██║   ██║████╗ ████║██╔════╝██╔══██╗
█████╗  ██║   ██║██████╔╝██║   ██║██╔████╔██║█████╗  ██████╔╝
██╔══╝  ██║   ██║██╔═══╝ ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║     ╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝      ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
```

---

## 🧪 Educational Use Cases

* ✅ InfoSec Training Labs
* ✅ Demonstrating Ransomware Behavior
* ✅ Testing Decryption Logic
* ✅ CTF or Red Team Simulations

---

## ⚠️ Disclaimer

This simulator is for **educational purposes only**. Do not use it on unauthorized systems or real data. The authors are not responsible for any misuse.

---


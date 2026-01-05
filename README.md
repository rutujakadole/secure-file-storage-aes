# Secure File Storage System Using AES Encryption

## Objective
The objective of this project is to design and implement a simple secure file storage system that encrypts and decrypts files using the AES (Advanced Encryption Standard) algorithm. This project demonstrates how encryption protects sensitive data from unauthorized access.

---

## Tools & Technologies Used
- Operating System: Windows
- Programming Language: Python 3
- Encryption Library: `cryptography`
- GUI Framework: Tkinter

---

## Project Structure
secure-file-storage-aes/
│── aes_gui.py
│── README.md

---

## How the Application Works

1. The application provides a simple graphical interface.
2. The user selects a file using a file browser.
3. The selected file is encrypted using AES-based symmetric encryption.
4. The encrypted file is saved with a `.enc` extension.
5. The same application can decrypt the encrypted file using the stored secret key.
6. The decrypted file is restored to its original readable format.

---

## Encryption Details
- Algorithm Used: AES (symmetric encryption)
- Key Management: A single secret key is generated and used for both encryption and decryption.
- File Security: Encrypted files appear as unreadable binary data, confirming successful encryption.

> Note: After encryption, the output file may appear as an unknown or Wireshark-captured file type. This is expected behavior because encrypted data has no recognizable file signature.

---

## How to Run the Project

### Step 1: Install required library
pip install cryptography

### Step 2: Run the application
python aes_gui.py

### Step 3: Use the GUI

Click Encrypt File → select any file → encrypted file is created

Click Decrypt File → select .enc file → original file is restored

## Security Benefits

Protects sensitive files from unauthorized access

Prevents data leakage

Ensures confidentiality of stored data

Demonstrates real-world use of encryption

## Safety Note

This project uses only test files.
No real or sensitive data was encrypted or uploaded.
The secret key file should never be shared publicly.

## Conclusion

This project successfully demonstrates secure file storage using AES encryption with a simple graphical interface, highlighting the importance of data confidentiality and encryption in real-world applications.

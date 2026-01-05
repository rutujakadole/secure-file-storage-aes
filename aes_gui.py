import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Generate or load key
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

key = load_key()
fernet = Fernet(key)

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    enc_file = file_path + ".enc"
    with open(enc_file, "wb") as f:
        f.write(encrypted)

    messagebox.showinfo("Success", f"File encrypted:\n{enc_file}")

def decrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
    if not file_path:
        return

    with open(file_path, "rb") as f:
        data = f.read()

    try:
        decrypted = fernet.decrypt(data)
    except Exception:
        messagebox.showerror("Error", "Invalid key or corrupted file")
        return

    dec_file = file_path.replace(".enc", "_decrypted")
    with open(dec_file, "wb") as f:
        f.write(decrypted)

    messagebox.showinfo("Success", f"File decrypted:\n{dec_file}")

# GUI Window
root = tk.Tk()
root.title("AES File Encryption Tool")
root.geometry("350x200")

tk.Label(root, text="Secure File Storage (AES)", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(root, text="Encrypt File", width=20, command=encrypt_file).pack(pady=5)
tk.Button(root, text="Decrypt File", width=20, command=decrypt_file).pack(pady=5)

root.mainloop()

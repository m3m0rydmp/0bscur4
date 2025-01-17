from cryptography.fernet import Fernet
import os

# Generate key and save it securely, Share to client
KEY_FILE = "key.key"

if not os.path.exists(KEY_FILE):
    KEY = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(KEY)
else:
    with open(KEY_FILE, 'rb') as f:
        KEY = f.read()

cipher = Fernet(KEY)

def enc_data(output):
    enc_output = cipher.encrypt(output.encode('utf-8'))
    return enc_output

def dec_data(enc_data):
    data = cipher.decrypt(enc_data).decode('utf-8')
    return data
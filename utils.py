import rsa
import base64

def generate_keys():
    public_key, private_key = rsa.newkeys(2048)
    return private_key, public_key  # ✅ trả về đúng thứ tự

def sign_data(data: bytes, private_key):
    if isinstance(data, str):
        data = data.encode()
    signature = rsa.sign(data, private_key, 'SHA-256')
    return base64.b64encode(signature).decode()

def export_key(key):
    return key.save_pkcs1().decode()

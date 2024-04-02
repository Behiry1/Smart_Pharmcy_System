import hashlib
import secrets
import string
import base64


secret_pepper_key = "tr3A4gRpo^{HT7pS1RtKbD@p]Q?y@z/1"

def hash_password(password, salt, pepper_key):
    pepper = pepper_key.encode('utf-8')
    combined_password = salt + pepper + password.encode('utf-8')
    hashed_password = hashlib.sha256(combined_password).hexdigest()
    return hashed_password

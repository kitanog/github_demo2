# example_sec.py
import hashlib

def insecure_hash(data):
    return hashlib.md5(data.encode()).hexdigest()  # MD5 is insecure

print(insecure_hash("Sensitive Data"))

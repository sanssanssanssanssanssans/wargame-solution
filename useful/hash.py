import hashlib

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()
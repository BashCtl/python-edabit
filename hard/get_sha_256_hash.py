import hashlib


def get_sha256_hash(txt):
    sha = hashlib.sha256(txt.encode()).hexdigest()
    return sha

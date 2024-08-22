import hashlib

def compute_md5(message):
    """Compute the MD5 hash of a given message."""
    md5_hash = hashlib.md5()
    md5_hash.update(message.encode('utf-8'))
    return md5_hash.hexdigest()

def compute_sha1(message):
    """Compute the SHA-1 hash of a given message."""
    sha1_hash = hashlib.sha1()
    sha1_hash.update(message.encode('utf-8'))
    return sha1_hash.hexdigest()

def main():
    # User inputs a message
    message = input("Enter a message: ")

    # Compute and display MD5 and SHA-1 hashes
    md5_result = compute_md5(message)
    sha1_result = compute_sha1(message)

    print(f"Original Message: {message}")
    print(f"MD5 Hash: {md5_result}")
    print(f"SHA-1 Hash: {sha1_result}")

if __name__ == "__main__":
    main()

from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# 1. Generate DSA private key
private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())

# 2. Generate public key from the private key
public_key = private_key.public_key()

# 3. Ask the user for input message
user_message = input("Enter the message to be signed: ")
message = user_message.encode('utf-8')  # Encode the message to bytes

# 4. Sign the message
signature = private_key.sign(message, hashes.SHA256())

print(f"\nMessage: {user_message}")
print(f"Signature: {signature.hex()}")  # Print the signature in hex format

# 5. Verify the signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("\nSignature is valid.")
except Exception as e:
    print("Signature verification failed.", str(e))

import hashlib
import RSA_key_exchange as rsa
import time

def sign(message, private_key):
    # Signs a message using RSA signature.Returns the signature as a hexadecimal string.

    d, n = private_key
    hash_value = hashlib.sha256(message.encode()).digest()
    signature = pow(int.from_bytes(hash_value, byteorder='big'), d, n)
    return hex(signature)[2:]  


def verify(message, signature, public_key):
    # Verifies the authenticity of a message using RSA signature.Returns True if the signature is valid, False otherwise.

    e, n = public_key
    hash_value = hashlib.sha256(message.encode()).digest()
    computed_signature = pow(int.from_bytes(hash_value, byteorder='big'), e, n)
    return hex(computed_signature)[2:] == signature



k = 128  

start_time = time.time()
public_key, private_key = rsa.generate_keys(k)
end_time = time.time()
print("Time taken to generate keys:", end_time - start_time)

print("Public key:", public_key)
print("Private key:", private_key)

message = "Two One Nine Two"
signature = sign(message, private_key)
is_valid = verify(message, signature, public_key)

print("Message:", message)
print("Signature:", signature)
print("Is Valid:", is_valid)

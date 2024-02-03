import RSA_key_exchange as rsa
import time
k = 128 

start_time = time.time()
public_key, private_key = rsa.generate_keys(k)
end_time = time.time()
print("Time taken to generate keys:", end_time - start_time)
print("Public key:", public_key)
print("Private key:", private_key)

message = "Two One Nine Two"
start_time = time.time()
ciphertext = rsa.encrypt(message, public_key)
end_time = time.time()
print("Time taken to encrypt:", end_time - start_time)

start_time = time.time()
decrypted_message = rsa.decrypt(ciphertext, private_key)
end_time = time.time()
print("Time taken to decrypt:", end_time - start_time)

print("Original message:", message)
print("Decrypted message:", decrypted_message)
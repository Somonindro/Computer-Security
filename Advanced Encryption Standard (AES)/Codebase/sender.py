import socket
import AES as aes
import Diffie_Hellman as df


# Agreement on p, g, and A = g^a (mod p)
k=128
p = df.generate_large_prime(k)
g = df.generate_primitive_root(p)
a = df.generate_large_prime(k//2)
A = df.power(g,a,p)

print("p , g , A =" ,p , g , A)

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Bob
host = 'localhost'
port = 12345
sock.connect((host, port))

# Send p, g, and A = g^a (mod p) to Bob
message = f"{p},{g},{A}"
sock.sendall(message.encode())

# Receive B = g^b (mod p) from Bob
B = int(sock.recv(1024).decode())
print("B = " , B)

# Compute the shared secret key
shared_secret_key = df.power(B, a, p)
print("Shared Secret Key = " , shared_secret_key)
hex_string = format(shared_secret_key, 'x')
key_hex_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
print("key : " ,key_hex_list)

# Inform Bob that Alice is ready for transmission
sock.sendall(b"Ready")

# Encrypt and send the ciphertext to Bob
plaintext = "Thats my Kung Fu I am Somonindro Roy"
li=aes.split_plaintext(plaintext)
#sending the length of the list
sock.sendall(str(len(li)).encode())

for i in range(len(li)):
    plaintext=li[i]
    if len(plaintext) < 16:
            plaintext += " " * (16 - len(plaintext))
    # shared_secret_key = aes.fix_key_length(shared_secret_key)
    plaintext_hex_list = aes.convert_string_to_hex(plaintext)
    # key_hex_list = aes.convert_string_to_hex(shared_secret_key)
    round_key_li = aes.round_key_scheduling(key_hex_list)
    state = aes.form_col_major_mat(plaintext_hex_list)
    encrypted_text_mat= aes.encryption(state, False , round_key_li)
    ciphertext = aes.matrix_to_text(encrypted_text_mat)
    print("In ASCII: ",ciphertext)
    sock.sendall(ciphertext.encode())

# Close the socket
sock.close()

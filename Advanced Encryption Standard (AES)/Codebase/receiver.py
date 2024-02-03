import socket
import AES as aes
import Diffie_Hellman as df


# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = 'localhost'
port = 12345
sock.bind((host, port))

# Listen for incoming connections
sock.listen(1)

# Accept a connection from Alice
alice_sock, alice_addr = sock.accept()

# Receive p, g, and g^a (mod p) from Alice
message = alice_sock.recv(1024).decode()
p, g, A = map(int, message.split(','))

print("p , g , A =" , p , g , A)

# Agreement on p, g, and g^b (mod p)
k=128
b = df.generate_large_prime(k//2)
B = df.power(g,b,p)

print("B = " , B)

# Send B = g^b (mod p) to Alice
alice_sock.sendall(str(B).encode())

# Compute the shared secret key
shared_secret_key = df.power(A, b, p)
print("Shared Secret Key = " , shared_secret_key)
hex_string = format(shared_secret_key, 'x')
#converting a big hex number to hex list where each element is 8 bits
key_hex_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
print("key : " ,key_hex_list)
decrypted_text = ""
# Wait for Alice to be ready for transmission
print(alice_sock.recv(1024).decode())
l=int(alice_sock.recv(1024).decode())
print("length of list : " , l)
# Receive the ciphertext from Alice
for i in range(l):
    ciphertext = alice_sock.recv(1024).decode()
    # Decrypt the ciphertext
    ciphertext_hex_list = aes.convert_string_to_hex(ciphertext)
    state = aes.form_col_major_mat(ciphertext_hex_list)
    round_key_li = aes.round_key_scheduling(key_hex_list)
    decrypted_text_mat = aes.decryption(state, True , round_key_li)
    parted_decrypted_text = aes.matrix_to_text(decrypted_text_mat)
    decrypted_text += parted_decrypted_text
    
print("Decrypted Text In ASCII: ",decrypted_text)
# Close the sockets
alice_sock.close()
sock.close()

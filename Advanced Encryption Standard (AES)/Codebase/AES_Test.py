import AES as aes
import time

f = open("input.txt", "r")
plaintext = f.readline()
#ignore the newline character
plaintext = plaintext[:-1]
key = f.readline()
f.close()

# plaintext = input("Enter plaintext: ")
# key = input("Enter key: ")
# plaintext = "Two One Nine Two"
# key = "Thats my Kung Fu"
li=aes.split_plaintext(plaintext)
print(li)
decrypted_text = ""
key = aes.fix_key_length(key)
# print(key)

for i in range(len(li)):
    plaintext = li[i]
    if len(plaintext) < 16:
        plaintext += " " * (16 - len(plaintext))
    print("Plaintext: ", plaintext)
    plaintext_hex_list = aes.convert_string_to_hex(plaintext)
    print("plain text in hex: ",plaintext_hex_list)
    key_hex_list = aes.convert_string_to_hex(key)
    print("key :", key)
    print("key in hex: ",key_hex_list)

    #round key scheduling
    start_time = time.time()
    round_key_li = aes.round_key_scheduling(key_hex_list)
    end_time = time.time()
    print("Time taken for round key scheduling: ", end_time - start_time)

    
    #encryption
    print("Encryption: ")
    state = aes.form_col_major_mat(plaintext_hex_list)
    start_time = time.time()
    encrypted_text_mat= aes.encryption(state, False , round_key_li)
    end_time = time.time()
    print("Time taken for encryption: ", end_time - start_time)
    encrypted_text = aes.matrix_to_text(encrypted_text_mat)
    print("In ASCII: ",encrypted_text)
    

    #decryption
    print("Decryption: ")
    start_time = time.time()
    decrypted_text_mat = aes.decryption(encrypted_text_mat, True , round_key_li)
    end_time = time.time()
    print("Time taken for decryption: ", end_time - start_time)

    parted_decrypted_text = aes.matrix_to_text(decrypted_text_mat)
    decrypted_text += parted_decrypted_text
    print("In ASCII: ",parted_decrypted_text)


print("In ASCII (final): ",decrypted_text)
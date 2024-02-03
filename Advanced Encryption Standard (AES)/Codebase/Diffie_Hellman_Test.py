import Diffie_Hellman as df
import time
k = 128
print(k)
start_time = time.time()
prime = df.generate_large_prime(k)
end_time = time.time()
print("Time taken to generate prime p:", end_time - start_time)
print("Generated prime:", prime)

#now find a random number g that lies between 2 and prime-1 and g^2%prime != 1 and g^((prime-1)/2)%prime != 1
start_time = time.time()
g=df.generate_primitive_root(prime)
end_time = time.time()
print("Time taken to generate primitive root g:", end_time - start_time)
print("Generated g:", g)

start_time = time.time()
a=df.generate_large_prime(k//2)
end_time = time.time()
print("Time taken to generate a:", end_time - start_time)
b=df.generate_large_prime(k//2)
print("Generated a:", a)
print("Generated b:", b)

start_time = time.time()
A = df.power(g,a,prime)
end_time = time.time()
print("Time taken to generate A:", end_time - start_time)
B = df.power(g,b,prime)
print("Generated A:", A)
print("Generated B:", B)

#now generate the key
start_time = time.time()
key1 = df.power(B,a,prime)
key2 = df.power(A,b,prime)
end_time = time.time()
print("Time taken to generate shared key:", end_time - start_time)
print("Generated shared key1:", key1)
print("Generated shared key2:", key2)
#check if key1 == key2
print("key1 == key2:", key1 == key2)
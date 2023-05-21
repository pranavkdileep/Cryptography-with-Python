import cryptography

from cryptography.fernet import Fernet

with open("pranavkd.key", "rb") as ourkey:
    key = ourkey.read()

encrypted_message = input("enter your encripted message :").encode()

message = Fernet(key).decrypt(encrypted_message)

print(message.decode())
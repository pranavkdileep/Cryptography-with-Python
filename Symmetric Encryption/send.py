import cryptography

from cryptography.fernet import Fernet #for Symmetric Encryption

key = Fernet.generate_key() #for generate a key

with open("pranavkd.key","wb") as key_file:  #create and store our secret key
    key_file.write(key)

message = input("enter your message : ").encode() #get normal readable message
crypter = Fernet(key) #creaing Fernet Object
encrypted_message = crypter.encrypt(message) #encrypting our message
print(encrypted_message.decode())
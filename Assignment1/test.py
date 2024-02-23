'''class Create_info:
    # create information
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def print_info(self):
        print(self.name)
        print(self.phone)
        print(self.email)
inputname = input('yourname')
inputphone = input('yourphone')
inputemail = input('youremail')
file = Create_info(inputname, inputphone, inputemail)
file.print_info()'''

'''# Define a simple XOR encryption function
def xor_encrypt_decrypt(message, key):
    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the message
    for char in message:
        # Perform XOR operation between the character and the key character
        # Use modulo operator to cycle through the key if it's shorter than the message
        result += chr(ord(char) ^ ord(key))

    return result

# Message to be encrypted
message = "Hello, this is a secret message!"
# Key for encryption
key = "k"

# Encrypt the message
encrypted_message = xor_encrypt_decrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message using the same key
decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)'''
print(ord('b'))
# Define a simple XOR encryption function
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
message = "Hello, this is a secret message45634!"
# Key for encryption
key = "k"

# Encrypt the message
encrypted_message = xor_encrypt_decrypt(message, key)
print("Encrypted message:", encrypted_message)

def encrypt(message, key):
    # Remove spaces from the message and calculate the length
    message = message.replace(" ", "")
    msg_len = len(message)
    
    # Calculate number of rows required
    rows = (msg_len + key - 1) // key
    
    # Create an empty matrix to store the message
    matrix = [['' for _ in range(key)] for _ in range(rows)]
    
    # Fill the matrix column-wise
    index = 0
    for col in range(key):
        for row in range(rows):
            if index < msg_len:
                matrix[row][col] = message[index]
                index += 1
            else:
                break
    
    # Read the matrix row-wise to generate the ciphertext
    ciphertext = ''
    for row in range(rows):
        for col in range(key):
            ciphertext += matrix[row][col]
    
    return ciphertext

def decrypt(ciphertext, key):
    # Calculate number of rows required
    rows = (len(ciphertext) + key - 1) // key
    
    # Calculate number of empty cells
    empty_cells = rows * key - len(ciphertext)
    
    # Determine the number of characters in the last row
    cols = key - empty_cells // rows
    
    # Create an empty matrix to store the ciphertext
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    
    # Fill the matrix row-wise
    index = 0
    for row in range(rows):
        for col in range(cols):
            if index < len(ciphertext):
                matrix[row][col] = ciphertext[index]
                index += 1
            else:
                break
    
    # Read the matrix column-wise to generate the plaintext
    plaintext = ''
    for col in range(cols):
        for row in range(rows):
            plaintext += matrix[row][col]
    
    return plaintext

# User input for message and key
message = input("Enter the message: ")
key = int(input("Enter the key: "))

# Encrypt the message
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

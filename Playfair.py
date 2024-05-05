def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_char_positions(matrix, char):
    positions = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == char:
                positions.append((i, j))
    return positions

def encrypt(playfair_matrix, plaintext):
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i+1] if i+1 < len(plaintext) else 'X'
        row1, col1 = find_char_positions(playfair_matrix, char1)[0]
        row2, col2 = find_char_positions(playfair_matrix, char2)[0]
        if row1 == row2:  # Same row
            ciphertext += playfair_matrix[row1][(col1 + 1) % 5]
            ciphertext += playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += playfair_matrix[(row1 + 1) % 5][col1]
            ciphertext += playfair_matrix[(row2 + 1) % 5][col2]
        else:  # Forming rectangle
            ciphertext += playfair_matrix[row1][col2]
            ciphertext += playfair_matrix[row2][col1]
    return ciphertext

def decrypt(playfair_matrix, ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        row1, col1 = find_char_positions(playfair_matrix, char1)[0]
        row2, col2 = find_char_positions(playfair_matrix, char2)[0]
        if row1 == row2:  # Same row
            plaintext += playfair_matrix[row1][(col1 - 1) % 5]
            plaintext += playfair_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += playfair_matrix[(row1 - 1) % 5][col1]
            plaintext += playfair_matrix[(row2 - 1) % 5][col2]
        else:  # Forming rectangle
            plaintext += playfair_matrix[row1][col2]
            plaintext += playfair_matrix[row2][col1]
    return plaintext

def display_matrix(playfair_matrix):
    for row in playfair_matrix:
        print(" ".join(row))

def main():
    key = input("Enter the key for Playfair cipher: ")
    playfair_matrix = generate_playfair_matrix(key)
    
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Show Matrix")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            plaintext = input("Enter plaintext: ")
            ciphertext = encrypt(playfair_matrix, plaintext)
            print("Encrypted ciphertext:", ciphertext)
        elif choice == "2":
            ciphertext = input("Enter ciphertext: ")
            plaintext = decrypt(playfair_matrix, ciphertext)
            print("Decrypted plaintext:", plaintext)
        elif choice == "3":
            print("Playfair Matrix:")
            display_matrix(playfair_matrix)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

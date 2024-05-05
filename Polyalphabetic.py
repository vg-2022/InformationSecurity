def validate_key(key):
    # Check if the key contains at least one letter
    if not key or not key.isalpha():
        return False
    return True

def vigenere_cipher_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key = key.upper()  # Convert key to uppercase for consistency
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext

def main():
    while True:
        key_input = input("Enter the encryption key (at least one letter): ").upper()
        if validate_key(key_input):
            break
        else:
            print("Invalid key! Please enter at least one letter.")

    plaintext = input("Enter plaintext: ")

    encrypted_text = vigenere_cipher_encrypt(plaintext, key_input)
    print("Encrypted ciphertext:", encrypted_text)

if __name__ == "__main__":
    main()

def validate_substitution_key(substitution_key):
    # Check if the substitution key contains at least one letter
    if not substitution_key or not substitution_key.isalpha():
        return False
    return True

def monoalphabetic_cipher_encrypt(plaintext, substitution_key):
    ciphertext = ""
    key_length = len(substitution_key)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                index = alphabet.find(char)
                ciphertext += substitution_key[index % key_length].upper()
            else:
                index = alphabet.find(char.upper())
                ciphertext += substitution_key[index % key_length].lower()
        else:
            ciphertext += char
    return ciphertext

def main():
    while True:
        key_input = input("Enter the substitution key (at least one letter): ").upper()
        if validate_substitution_key(key_input):
            break
        else:
            print("Invalid key! Please enter at least one letter.")

    plaintext = input("Enter plaintext: ")

    encrypted_text = monoalphabetic_cipher_encrypt(plaintext, key_input)
    print("Encrypted ciphertext:", encrypted_text)

if __name__ == "__main__":
    main()

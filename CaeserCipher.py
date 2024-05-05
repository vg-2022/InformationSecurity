def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine the appropriate shift for uppercase and lowercase letters
            if char.isupper():
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine the appropriate shift for uppercase and lowercase letters
            if char.isupper():
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

def main():
    plaintext = input("Enter plaintext: ")
    shift = int(input("Enter the shift value: "))

    ciphertext = caesar_cipher_encrypt(plaintext, shift)
    print("Encrypted ciphertext:", ciphertext)

    decrypted_plaintext = caesar_cipher_decrypt(ciphertext, shift)
    print("Decrypted plaintext:", decrypted_plaintext)

if __name__ == "__main__":
    main()

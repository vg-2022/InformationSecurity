import numpy as np

def create_cipher(plain_text, key):
    plain_text = plain_text.replace(" ", "").lower()
    text_len = len(plain_text)
    
    col = len(key)
    row = -(-text_len // col)  # Equivalent to ceil(text_len / col)

    arr = np.zeros((row, col), dtype=int)

    k = 0
    for i in range(row):
        for j in range(col):
            if k < text_len:
                arr[i, j] = ord(plain_text[k]) - ord('a')
                k += 1
            else:
                arr[i, j] = ord('x') - ord('a')  # Padding with 'x' if necessary

    return [arr[i, key[j] - 1] for j in range(col) for i in range(row)]

def decryption(key, cipher):
    col = len(key)
    row = -(-len(cipher) // col)  # Equivalent to ceil(len(cipher) / col)

    arr = np.zeros((row, col), dtype=int)

    k = 0
    for j in range(col):
        for i in range(row):
            arr[i, key[j] - 1] = cipher[k]
            k += 1

    plaintext = "".join(chr(arr[i, j] + ord('a')) for i in range(row) for j in range(col))
    return plaintext


def main():
    print("Row Transposition Cipher")

    # Input plaintext
    plain_text = input("Enter plaintext: ")

    # Input key
    key = list(map(int, input("Enter key (e.g., '2314' means read columns in the order 2,3,1,4): ")))

    # Encrypt plaintext
    cipher = create_cipher(plain_text, key)
    print("Encrypted ciphertext:", "".join(chr(elem + ord('a')) for elem in cipher))

    # Input ciphertext
    cipher_input = input("Enter ciphertext: ").replace(" ", "").lower()

    # Decrypt ciphertext
    decrypted_plain_text = decryption(key, [ord(char) - ord('a') for char in cipher_input])
    print("Decrypted plaintext:", decrypted_plain_text)


if __name__ == "__main__":
    main()

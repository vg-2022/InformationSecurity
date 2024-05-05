import numpy as np

def encryption():
    global encrypt
    encrypt = np.zeros((3, 2))
    for i in range(3):
        for j in range(2):
            for k in range(3):
                encrypt[i][j] += a[i][k] * mes[k][j]
            encrypt[i][j] = fmod(encrypt[i][j], 26)
    print("\nEncrypted string is : ", end="")
    for i in range(3):
        for j in range(2):
            print(chr(int(encrypt[i][j]) + 97), end="")
    print()

def decryption():
    global decrypt
    inverse()
    decrypt = np.zeros((3, 2))
    for i in range(3):
        for j in range(2):
            for k in range(3):
                decrypt[i][j] += b[i][k] * encrypt[k][j]
            decrypt[i][j] = fmod(decrypt[i][j], 26)
    print("\nDecrypted string is : ", end="")
    for i in range(3):
        for j in range(2):
            print(chr(int(decrypt[i][j]) + 97), end="")
    print()

def getKeyMessage():
    global a, c, mes
    a = np.zeros((3, 3))
    c = np.zeros((3, 3))
    mes = np.zeros((3, 2))

    # Get key input
    while True:
        key_input = input("Enter a 9-letter string for key: ")
        if len(key_input) >= 9:
            break
        else:
            print("Key should be at least 9 characters long.")

    for i in range(3):
        for j in range(3):
            a[i][j] = ord(key_input[i * 3 + j]) - ord('a')
            c[i][j] = a[i][j]

    # Get message input
    while True:
        msg = input("Enter a 6-letter message: ")
        if len(msg) >= 6:
            break
        else:
            print("Message should be at least 6 characters long.")

    for i in range(3):
        for j in range(2):
            mes[i][j] = ord(msg[i * 2 + j]) - ord('a')


def inverse():
    global b
    b = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if i == j:
                b[i][j] = 1
            else:
                b[i][j] = 0

    for k in range(3):
        for i in range(3):
            p = c[i][k]
            q = c[k][k]
            for j in range(3):
                if i != k:
                    c[i][j] = c[i][j] * q - p * c[k][j]
                    b[i][j] = b[i][j] * q - p * b[k][j]

    for i in range(3):
        for j in range(3):
            b[i][j] = ceil((b[i][j] / c[i][i]) * 10000) / 10000.0

    print("\n\nInverse Matrix is:\n", end="")
    for i in range(3):
        for j in range(3):
            print(b[i][j], "\t", end="")
        print()

def fmod(a, b):
    return a % b

def ceil(a):
    return int(a + 0.5)

def main():
    while True:
        print("\nHill Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            getKeyMessage()
            encryption()
        elif choice == "2":
            getKeyMessage()
            decryption()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

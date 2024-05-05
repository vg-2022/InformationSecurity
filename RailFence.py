def rail_fence_encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction

    ciphertext = ''.join([''.join(rail) for rail in fence])
    return ciphertext

def rail_fence_decrypt(ciphertext, rails):
    fence = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction

    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*' and index < len(ciphertext):
                fence[i][j] = ciphertext[index]
                index += 1

    rail = 0
    direction = 1
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext += fence[rail][i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction

    return plaintext

def main():
    while True:
        print("\nRail Fence Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            plaintext = input("Enter plaintext: ")
            rails = int(input("Enter the number of rails: "))
            ciphertext = rail_fence_encrypt(plaintext, rails)
            print("Encrypted ciphertext:", ciphertext)
        elif choice == "2":
            ciphertext = input("Enter ciphertext: ")
            rails = int(input("Enter the number of rails: "))
            plaintext = rail_fence_decrypt(ciphertext, rails)
            print("Decrypted plaintext:", plaintext)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

def calcRedundantBits(m):
    for i in range(m):
        if 2**i >= m + i + 1:
            return i

def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if i == 2**j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1 * j])
        res = res + val*(10**i)
    return int(str(res), 2)

def correctError(received_data, error_position):
    if error_position > 0:
        # Flip the bit at the detected error position
        corrected_data = list(received_data)
        corrected_data[error_position - 1] = '1' if received_data[error_position - 1] == '0' else '0'
        corrected_data = ''.join(corrected_data)
        return corrected_data
    else:
        return received_data

def main():
    data = input("Enter data to be transmitted: ")
    m = len(data)
    r = calcRedundantBits(m)
    arr = posRedundantBits(data, r)
    arr = calcParityBits(arr, r)
    print("Data transmitted is:", arr)

    received_data = input("Enter received data (with possible errors): ")
    correction = detectError(received_data, r)
    if correction == 0:
        print("There is no error in the received message.")
    else:
        print("Error detected at position:", len(received_data) - correction + 1, "from the left")
        corrected_data = correctError(received_data, len(received_data) - correction + 1)
        print("Corrected data is:", corrected_data)

if __name__ == "__main__":
    main()

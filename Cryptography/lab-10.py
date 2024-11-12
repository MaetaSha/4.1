# Dictionary to map letters to numerical positions and vice versa
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))

# Function to decrypt the ciphertext using the key
def vernam_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        # XOR the ciphertext character with the key character to get the original plaintext character
        xor = mp[ciphertext[i]] ^ mp[key[i]]
        plaintext += mp2[xor % 26]  # Convert result back to a letter
    return plaintext

# Main function
def main():
    ciphertext = input("Enter ciphertext: ")  # Example ciphertext
    key = input("Enter key: ")  # Example key used during encryption

    # Decrypt the ciphertext using the key
    decrypted_text = vernam_decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)  # This should match the original plaintext

# Run the program
if __name__ == "__main__":
    main()

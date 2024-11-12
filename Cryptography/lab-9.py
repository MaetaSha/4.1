import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))


# Function to generate a random key of given length
def generate_key(length):
    key = ""
    for i in range(length):
        key += random.choice(alphabet)  # Randomly choose a letter from the alphabet
    return key


# Function to encrypt the plaintext using the key
def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        xor = mp[plaintext[i]] ^ mp[key[i]]  # XOR operation
        ciphertext += mp2[(mp['A'] + xor) % 26]  # Create the ciphertext
    return ciphertext


# Main function
def main():
    plaintext = input("Enter the plain text: ")  # Example plaintext
    plaintext = plaintext.upper()  # Ensure the plaintext is in uppercase
    key = generate_key(len(plaintext))  # Generate a random key with the same length as the plaintext
    ciphertext = encrypt(plaintext, key)  # Encrypt the plaintext using the key
    print("Key:", key)  # Print the generated key
    print("Ciphertext:", ciphertext)  # Print the ciphertext


# Run the program
if __name__ == "__main__":
    main()

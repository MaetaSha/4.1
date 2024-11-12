# Function to encrypt a message with a given key (shift)
def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Convert letter to its alphabetical index (0-25)
            char_index = ord(char.upper()) - 65
            # Encrypt the letter by shifting it forwards by the given key
            new_index = (char_index + shift) % 26
            # Convert back to letter and preserve case
            encrypted_char = chr(new_index + 65) if char.isupper() else chr(new_index + 97)
            ciphertext += encrypted_char
        else:
            # Keep non-alphabet characters unchanged
            ciphertext += char
    return ciphertext

# Function to decrypt a message with a given key (shift)
def decrypt_with_key(ciphertext, k):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            # Convert letter to its alphabetical index (0-25)
            char_index = ord(char.upper()) - 65
            # Decrypt the letter by shifting it backwards by key k
            new_index = (char_index - k) % 26
            # Convert back to letter and preserve case
            decrypted_char = chr(new_index + 65) if char.isupper() else chr(new_index + 97)
            plaintext += decrypted_char
        else:
            # Keep non-alphabet characters unchanged
            plaintext += char
    return plaintext

# Function for brute force attack on the Caesar cipher
def brute_force_attack(ciphertext):
    for k in range(1, 26):  # Try all shifts from 1 to 25
        decrypted_text = decrypt_with_key(ciphertext, k)
        print(f"Key {k}: {decrypted_text}")

# Main function to demonstrate encryption, brute force attack and decryption
def main():
    # Input the plaintext and the shift value
    plaintext = input("Enter the plaintext to encrypt: ")
    shift = int(input("Enter the shift value (1-25): "))

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, shift)
    print(f"Ciphertext: {ciphertext}")

    # Perform brute force attack on the ciphertext to recover the original message
    print("\nBrute force attack results:")
    brute_force_attack(ciphertext)

# Run the main function
if __name__ == "__main__":
    main()

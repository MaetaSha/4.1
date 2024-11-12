# Function to decrypt a message with a given key
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

# Main function to demonstrate brute force decryption
def main():
    ciphertext = input("Enter the ciphertext to decrypt: ")
    print("\nBrute force attack results:")
    brute_force_attack(ciphertext)

# Run the main function
if __name__ == "__main__":
    main()

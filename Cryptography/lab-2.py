# Function to create the cipher mapping from the key
def create_cipher_mapping(key):
    # Remove spaces and duplicate characters from the key
    key = ''.join(sorted(set(key), key=key.index)).replace(' ', '')
    
    # Define the alphabet for the mapping
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Create a list of letters that are not in the key
    remaining_letters = [letter for letter in alphabet if letter not in key]
    
    # Combine key with the remaining letters to complete the substitution
    full_key = key + ''.join(remaining_letters)
    return full_key

# Function for encryption
def encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_mapping = create_cipher_mapping(key)
    
    ciphertext = ""
    for letter in plaintext.upper():
        if letter in alphabet:
            # Find the position of the letter in the alphabet and get the corresponding letter from the key
            index = alphabet.index(letter)
            ciphertext += cipher_mapping[index]
        else:
            ciphertext += letter  # Non-alphabet characters (like spaces) remain unchanged
    
    return ciphertext

# Function for decryption
def decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_mapping = create_cipher_mapping(key)
    
    plaintext = ""
    for letter in ciphertext.upper():
        if letter in cipher_mapping:
            # Find the position of the letter in the key and get the corresponding letter from the alphabet
            index = cipher_mapping.index(letter)
            plaintext += alphabet[index]
        else:
            plaintext += letter  # Non-alphabet characters (like spaces) remain unchanged
    
    return plaintext

# Main function to demonstrate encryption and decryption
def main():
    key = input("Enter the substitution key: ").upper()
    plaintext = input("Enter the message to encrypt: ").upper()
    
    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext: ", ciphertext)
    
    # Decrypt the ciphertext back to plaintext
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted message: ", decrypted_text)

# Run the main function
if __name__ == "__main__":
    main()

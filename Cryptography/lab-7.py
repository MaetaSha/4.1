# Define the alphabet and mappings
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))

# Function for Poly-Alphabetic Cipher Encryption
def polyalphabetic_encrypt(plaintext, key):
    plaintext = plaintext.upper()  # Ensure plaintext is in uppercase
    key = key.upper()  # Ensure key is in uppercase
    
    # Repeat the key to match the length of the plaintext
    repeated_key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    
    ciphertext = ""
    for i in range(len(plaintext)):
        # Get the numeric positions for plaintext and key characters
        pt_pos = mp[plaintext[i]]
        key_pos = mp[repeated_key[i]]
        
        # Apply the encryption formula
        encrypted_pos = (pt_pos + key_pos) % 26
        ciphertext += mp2[encrypted_pos]  # Convert back to letter and add to ciphertext
    
    return ciphertext

# Main program
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
ciphertext = polyalphabetic_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

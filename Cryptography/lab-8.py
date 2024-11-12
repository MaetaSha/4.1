# Define the alphabet and mappings
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))

# Function for Poly-Alphabetic Cipher Decryption
def polyalphabetic_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()  # Ensure ciphertext is in uppercase
    key = key.upper()  # Ensure key is in uppercase
    
    # Repeat the key to match the length of the ciphertext
    repeated_key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    
    plaintext = ""
    for i in range(len(ciphertext)):
        # Get the numeric positions for ciphertext and key characters
        ct_pos = mp[ciphertext[i]]
        key_pos = mp[repeated_key[i]]
        
        # Apply the decryption formula
        decrypted_pos = (ct_pos - key_pos + 26) % 26
        plaintext += mp2[decrypted_pos]  # Convert back to letter and add to plaintext
    
    return plaintext

# Main program
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")
plaintext = polyalphabetic_decrypt(ciphertext, key)
print("Plaintext:", plaintext)

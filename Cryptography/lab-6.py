def create_matrix(key):
    key = key.upper().replace('J', 'I')  # Replace J with I as per Playfair rules
    matrix = []
    used_chars = set()
    for char in key:
        if char.isalpha() and char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    # Fill the matrix with remaining letters of the alphabet (excluding 'J')
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # Note: No J
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    # Create a 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    # Find the position of the character in the matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


def decrypt_pair(matrix, pair):
    # Find positions of the two characters in the matrix
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])
    
    if row1 == row2:  # Same row
        return (matrix[row1][(col1 - 1) % 5], matrix[row2][(col2 - 1) % 5])
    elif col1 == col2:  # Same column
        return (matrix[(row1 - 1) % 5][col1], matrix[(row2 - 1) % 5][col2])
    else:  # Rectangle case
        return (matrix[row1][col2], matrix[row2][col1])


def playfair_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace('J', 'I')
    ciphertext = ''.join(c for c in ciphertext if c.isalpha())  # Remove non-alphabetic chars
    matrix = create_matrix(key)
    decrypted = []
    
    # Decrypt in pairs
    for i in range(0, len(ciphertext), 2):
        if i + 1 < len(ciphertext):
            pair = decrypt_pair(matrix, (ciphertext[i], ciphertext[i + 1]))
            decrypted.extend(pair)
    
    decrypted_text = ''.join(decrypted)
    
    # Remove the trailing 'X' if it exists (added during encryption)
    if decrypted_text.endswith('X'):
        decrypted_text = decrypted_text[:-1]
    
    return decrypted_text


def main():
    key = "RAKIB"
    ciphertext = "RFFECSKASNFMSY"  # Example ciphertext
    print("Key:", key)
    print("Ciphertext:", ciphertext)
    decrypted = playfair_decrypt(ciphertext, key)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()

def create_matrix(key):
    # Create a 5x5 matrix using the key
    key = key.upper().replace('J', 'I')  # Replace J with I as per Playfair rules
    matrix = []
    used_chars = set()
    for char in key:
        if char.isalpha() and char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # Note: No J
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def prepare_text(text):
    text = ''.join(c.upper() for c in text if c.isalpha())
    text = text.replace('J', 'I')
    
    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:  # If the last character is left
            pairs.append(text[i] + 'X')
            break
        elif text[i] == text[i + 1]:  # If two consecutive letters are the same
            pairs.append(text[i] + 'X')
            i += 1
        else:
            pairs.append(text[i] + text[i + 1])
            i += 2
            
    return pairs

def encrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])
    
    if row1 == row2:  # Same row
        return (matrix[row1][(col1 + 1) % 5] + 
                matrix[row2][(col2 + 1) % 5])
    elif col1 == col2:  # Same column
        return (matrix[(row1 + 1) % 5][col1] + 
                matrix[(row2 + 1) % 5][col2])
    else:  # Rectangle case
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(key, plaintext):
    matrix = create_matrix(key)
    pairs = prepare_text(plaintext)
    ciphertext = ''
    
    for pair in pairs:
        ciphertext += encrypt_pair(matrix, pair)
    
    return ciphertext

if __name__ == "__main__":
    key = "RAKIB"
    plaintext = "ICEDEPARTMENT"
    
    print("Key:", key)
    print("Original text:", plaintext)
    
    encrypted = playfair_encrypt(key, plaintext)
    print("\nEncrypted text:", encrypted)

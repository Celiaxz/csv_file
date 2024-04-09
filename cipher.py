def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Ciphertext
ciphertext = """zv tbjo klwlukz bwvu
h ylk dollsihyyvd
nshglk dpao yhpu dhaly
ilzpkl aol dopal jopjrluz"""

# Frequency analysis to discover the Caesar key
letter_frequency = {'a': 4, 'b': 2, 'd': 5, 'g': 1, 'h': 5, 'i': 1, 'j': 3, 'k': 5, 'l': 11, 'n': 1, 'o': 5, 'p': 5, 'r': 1, 's': 1, 't': 1, 'u': 4, 'v': 3, 'w': 2, 'y': 5, 'z': 3}
most_common_letter = max(letter_frequency, key=letter_frequency.get)
shift = (ord(most_common_letter) - ord('e')) % 26

# Decrypt the ciphertext using the discovered Caesar key
plaintext = decrypt_caesar(ciphertext, shift)

# Output the decrypted text
print("Decrypted text:")
print(plaintext)

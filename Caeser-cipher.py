def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Encryption/Decryption")
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the shift value.")
    mode = ''
    while mode not in ['e', 'd']:
        mode = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if mode == 'e':
        encrypted = caesar_cipher(message, shift, mode='encrypt')
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = caesar_cipher(message, shift, mode='decrypt')
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
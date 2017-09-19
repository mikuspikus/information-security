import os
import string

def _get_plain_text(file_name):
    path = os.path.join(file_name)

    with open(path, 'r') as f:
        buffer = f.read()

    return buffer

def _write_plain_text(plain_text, file_name):
    path = os.path.join(file_name)
    try:
        with open(path, 'w') as f:
            f.write(plain_text)

        return True
    except OSError:
        return False


def caesar_cipher(plain_text, key):
    return plain_text.translate(str.maketrans(string.ascii_lowercase + string.ascii_uppercase, string.ascii_lowercase[hash(key) % 26:] +
        string.ascii_lowercase[:hash(key) % 26] + string.ascii_uppercase[hash(key) % 26:] + string.ascii_uppercase[:hash(key) % 26]))

def caesar_decipher(plain_text, key):
    return plain_text.translate(str.maketrans(string.ascii_lowercase[hash(key) % 26:] + string.ascii_lowercase[:hash(key) % 26] + 
        string.ascii_uppercase[hash(key) % 26:] + string.ascii_uppercase[:hash(key) % 26], string.ascii_lowercase + string.ascii_uppercase))

if __name__ == '__main__':

    text = _get_plain_text('text.txt')
    key = 'lolmemespepe'

    print('Original text: \n', text)
    print('\nEncrypted text: \n', caesar_cipher(text, key))
    _write_plain_text(caesar_cipher(text, key), 'encrypted_text.txt')
    print('\nDecrypted text: \n', caesar_decipher(caesar_cipher(text, key), key))

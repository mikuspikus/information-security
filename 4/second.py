import os
from first import _psrndm_generator
from random import randint
import string

def _get_plain_text(file_name):
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, file_name)

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

def prg_cipher(plain_text, prg_numbers):
    return ''.join([ chr( ord(plain_text[char_index]) ^ prg_numbers[char_index % len(prg_numbers)] ) for char_index in range(len(plain_text)) ])

if __name__ == '__main__':
    a, c, t = randint(1, 100), randint(1, 100), randint(1, 100) 
    text = _get_plain_text('text.txt')
    generated_numbers = _psrndm_generator(a, c, t, k = int(1e5))

    print('Original text:\n', text)
    print('Generated numbers:\n', generated_numbers[:10], generated_numbers[-10:])

    encrypted_text = prg_cipher(text, generated_numbers)
    print('Ecrypted text:\n', repr(encrypted_text))

    print('Decrypted text:\n', prg_cipher(encrypted_text, generated_numbers))
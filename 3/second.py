import os
from first import _get_plain_text, caesar_decipher
import string

def _read_letter_freq(file_name):
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, file_name)
    letters_frequency = {}

    with open(path, 'r') as f:
        buffer = f.readlines()

    for line in buffer:
        word = line.split()
        if word == []:
            continue
        letters_frequency[word[0]] = float(word[1][:-1]) / 100

    return letters_frequency

def _letter_freq_counter(plain_text):
    plain_text = ''.join([ char for char in plain_text.lower() if char in string.ascii_lowercase ])
    return { letter : plain_text.count(letter) / len(plain_text) for letter in string.ascii_lowercase }

def _guess_cipher_shift(alphabet_frequency, text_frequency):
    shift_list = []
    alphabet_values, text_values = [i for i in alphabet_frequency.values()], [i for i in text_frequency.values()]

    for shift in range(0, len(alphabet_frequency)):
        shift_list.append(sum([ abs(alphabet_values[i] - text_values[(i + shift) % len(alphabet_frequency)]) ** 2 for i in range(0, len(alphabet_frequency)) ])) 
    
    return shift_list.index(min(shift_list))

print('Encrypted text:\n\n', _get_plain_text('encrypted_text.txt'))
print('\n\nDecrypted text:\n\n', caesar_decipher(_get_plain_text('encrypted_text.txt'), _guess_cipher_shift(_read_letter_freq('letters_frequency.txt'), _letter_freq_counter(_get_plain_text('encrypted_text.txt')))), 
    '\n\nKey: ', _guess_cipher_shift(_read_letter_freq('letters_frequency.txt'), _letter_freq_counter(_get_plain_text('encrypted_text.txt'))))
__author__ = 'tracyrohlin'

import re
from string import ascii_lowercase

alphabet = "".join(ascii_lowercase)
reverse_alph = "".join(alphabet[::-1])

def remove_unwanted(str_a):
    str_a = str_a.lower()
    str_a = re.sub(r"\W+", "", str_a)
    return str_a


def switch_letters(str_a, input_alph, output_alph):
    str_a = list(remove_unwanted(str_a))
    for letter in range(len(str_a)):
        if str_a[letter] in alphabet:
            for m in re.finditer(str_a[letter], input_alph):
                i = m.start()
            str_a[letter] = output_alph[i]
    return "".join(str_a)


def encode(str_a):
    str_a = switch_letters(str_a, alphabet, reverse_alph)
    result = ""
    for i in range(0, len(str_a)+1, 5):
        result += "".join(str_a[i:i+5]) + " "
    return result.strip()


def decode(str_a):
    result = switch_letters(str_a, reverse_alph, alphabet)
    return "".join(result)


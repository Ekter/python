# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:21:31 2018
@author: Satyajit
"""
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
}
def encryption(message):
    my_cipher = ''
    for myletter in message:
        if myletter != ' ':
            my_cipher += MORSE_CODE_DICT[myletter] + ' '
        else:
            my_cipher += ' '
        return my_cipher
# This function is used to decrypt
# Morse code to English
def decryption(message):
    message += ' '
    decipher = ''
    mycitext = ''
    for myletter in message:
        # checks for space
        if (myletter != ' '):
            i = 0
            mycitext += myletter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(mycitext)]
                mycitext = ''
    return decipher
def main():
    my_message = "PYTHON-PROGRAM"
    output = encryption(my_message.upper())
    print (output)
    my_message = "-... --- -. .--- --- ..- .-. "
    output = decryption(my_message)
    print (output)
# Executes the main function
if __name__ == '__main__':
    main()



ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
FIRST_LETTER = ord(ENGLISH_ALPHABET[0])
NUMBER_OF_LETTERS = len(ENGLISH_ALPHABET)


def shift(letter, amount):
    """ Shifts every letter by the amount given.
    If the shift surpasses the last letter of the alphabet, it starts from the beginning.
    Examples: 'A' shifted by 2 is 'C', 'Z' shifted by 1 is 'A', 'F' shifted by -3 is 'C' """
    number = ord(letter) - FIRST_LETTER  # Converts the letter into its equivalent number (0 - 25)
    number = number + amount  # Shifts the letter by the amount given
    number = number % NUMBER_OF_LETTERS  # Keep the number between 0 and 25 by using the modulus operator
    letter = chr(number + FIRST_LETTER)  # Converts the number back to a letter (97 - 122)
    return letter


def caesar(message='', key=0, encrypt=True):
    """ Returns a decrypted message using the Caesar Cipher method.
        Shifts every letter by the amount given by the key adding for encryption and subtracting for decryption.
        Characters not part of the English alphabet are ignored by the cipher and included in the final result.
        Not valid examples: spaces, numbers, punctuation, other alphabet letters... """
    encrypted = ''
    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only applies the cipher to letters, other characters are not encrypted
            if encrypt:  # Shifts the letter by the amount given by the key
                letter = shift(letter, key)  # Adding the shift for encryption
            else:
                letter = shift(letter, -key)  # Subtracting the shift for decryption
        encrypted += letter  # Appends the shifted letter at the end of the result message
    return encrypted

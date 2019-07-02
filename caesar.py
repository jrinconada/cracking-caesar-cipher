
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
FIRST_LETTER = ord(ALPHABET[0])
NUMBER_OF_LETTERS = len(ALPHABET)


def encrypt(message, key):
    """ Returns an encrypted message using the Caesar Cipher method.
        Shifts every letter by the amount given by the key.
        Character not part of the English alphabet are ignored by the cipher and included in the final result,
        (spaces, numbers, punctuation, other alphabet letters...) """
    encrypted = ''
    for letter in message:  # For every letter in the message
        if letter in ALPHABET:  # Only applies the cipher to letters, other characters are not encrypted
            number = ord(letter) - FIRST_LETTER  # Converts the letter into its equivalent number (0 - 25)
            number = (number + key) % NUMBER_OF_LETTERS  # Adds the key shifting the letter by letter
            letter = chr(number + FIRST_LETTER)  # Converts the number back to a letter (97 - 122)
        encrypted += letter  # Puts the letter at the end of the encrypted result message
    return encrypted

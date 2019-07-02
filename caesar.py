
ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
FIRST_LETTER = ord(ENGLISH_ALPHABET[0])
NUMBER_OF_LETTERS = len(ENGLISH_ALPHABET)


def encrypt(message, key):
    """ Returns an encrypted message using the Caesar Cipher method.
        Characters not part of the English alphabet are ignored by the cipher and included in the final result.
        For example: spaces, numbers, punctuation, other alphabet letters... """
    return apply(message, key, True)


def decrypt(message, key):
    """ Returns a decrypted message using the Caesar Cipher method.
        Characters not part of the English alphabet are ignored by the cipher and included in the final result.
        For example: spaces, numbers, punctuation, other alphabet letters... """
    return apply(message, key, False)


def apply(message, key, encryption):
    """ Shifts every letter by the amount given by the key adding for encryption and subtracting for decryption """
    encrypted = ''
    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only applies the cipher to letters, other characters are not encrypted
            number = ord(letter) - FIRST_LETTER  # Converts the letter into its equivalent number (0 - 25)
            if encryption:  # Shifts the letter by the amount given by the key
                number = number + key  # Adding the shift for encryption
            else:
                number = number - key  # Subtracting the shift for decryption
            number = number % NUMBER_OF_LETTERS  # Keep the number between 0 and 25 by using the modulus operator
            letter = chr(number + FIRST_LETTER)  # Converts the number back to a letter (97 - 122)
        encrypted += letter  # Appends the shifted letter at the end of the result message
    return encrypted

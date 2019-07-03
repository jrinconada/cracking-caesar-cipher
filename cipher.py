
ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
FIRST_LETTER = ord(ENGLISH_ALPHABET[0])  # Get the ASCII number of the first letter of the alphabet
NUMBER_OF_LETTERS = len(ENGLISH_ALPHABET)  # Get the number of letters in alphabet


def to_number(letter):
    """ Transforms a letter to a number between 0 and 25.
        Examples: 'A' is 0, 'B' is 1, 'Z' is 25 """
    number = ord(letter)  # Convert the letter into its equivalent ASCII number (97 - 122)
    return number - FIRST_LETTER  # Shift the number to the alphabet range (0 - 25)


def to_letter(number):
    """ Transforms a number to a letter of the alphabet.
        If the number surpasses the last letter of the alphabet, it starts from the beginning.
        Examples: 0 is 'A', 1 is 'B', 26 is 'A', 27 is 'B' """
    number = number % NUMBER_OF_LETTERS  # Keep the number between 0 and 25 by using the modulus operator
    number = number + FIRST_LETTER  # Shift the number back to the ASCII equivalent (97 - 122)
    return chr(number)  # Convert the number back to a character


def shift(letter, amount):
    """ Shifts every letter by the amount given cycling though the alphabet.
        Examples: 'A' shifted by 2 is 'C', 'Z' shifted by 1 is 'A', 'F' shifted by -3 is 'C' """
    number = to_number(letter)  # Convert the letter the equivalent number (0 - 25)
    number = number + amount  # Shift the letter by the amount given
    return to_letter(number)  # Convert the number back to a letter


def caesar(message, key, encrypt=True):
    """ Returns a processed message using the Caesar Cipher method.
        Shifts every letter by the amount given by the key adding for encryption and subtracting for decryption.
        Characters not part of the English alphabet are ignored by the cipher and included in the final result.
        Not valid examples: spaces, numbers, punctuation, other alphabet letters... """
    encrypted = ''
    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only applies the cipher to letters, other characters are not encrypted
            if encrypt:  # Shift the letter by the amount given by the key
                letter = shift(letter, key)  # Adding the shift for encryption
            else:
                letter = shift(letter, -key)  # Subtracting the shift for decryption
        encrypted += letter  # Append the shifted letter at the end of the result message
    return encrypted


def vigenere(message, key, encrypt=True):
    """ Returns a processed message using the Vigenere Cipher method.
        For every letter applies a shift cycling through the key word.
        Adds the shift for encryption and subtract it for decryption.
        Characters not part of the English alphabet are ignored by the cipher and included in the final result.
        Not valid examples: spaces, numbers, punctuation, other alphabet letters... """
    encrypted = ''
    i = 0  # Counter to cycle through the key
    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only applies the cipher to letters, other characters are not encrypted
            key_letter = key[i % len(key)]  # Cycling through the key using modulus operator to keep in range
            amount = to_number(key_letter)  # Get the equivalent number for this letter of the key
            if encrypt:  # Shift the letter by the amount given by the key
                letter = shift(letter, amount)  # Adding the shift for encryption
            else:
                letter = shift(letter, -amount)  # Subtracting the shift for decryption
            i += 1  # Next letter of the key
        encrypted += letter  # Append the shifted letter at the end of the result message
    return encrypted

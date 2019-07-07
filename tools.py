import numpy as np

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


def sort(numbers, letters, by_number=True, reverse=False):
    """ Given two lists, sorts them together.
        If by_number is True sorts them by number if False by letter.
        If reverse is True sorts them in descending order """
    # Put them together, first the one which sets the order
    together = zip(numbers, letters) if by_number else zip(letters, numbers)
    together = sorted(together, reverse=reverse)  # Sort them together
    # Get back the lists, now sorted
    if by_number:
        numbers, letters = zip(*together)
    else:
        letters, numbers = zip(*together)

    return numbers, letters


def count_to_frequency(count):
    """ Given a letter count gets the frequency aa a percentage of the total number of letters. """
    total = 0
    for letter_count in count:  # Sum all letter counts to get the total number of letters
        total += letter_count

    frequencies = []
    for letter_count in count:  # For every letter count
        # Divide by the total number of letter and multiply by 100 to get the frequency percentage
        frequencies.append((letter_count / total) * 100)

    return frequencies


def to_matrix(letters, letter_count):
    """ Transforms a string to matrix given the letter count """

    line_size = np.round(np.sqrt(len(letters)))  # Get the closest square, for example: for 20 is 4, since 4*4 = 16

    matrix = []  # A matrix is a list of lists
    line = []  # Letter count for each line
    i = 0  # Word counter

    for letter in letters:  # Get the count for every letter in the message
        if i == line_size:  # Line change
            matrix.append(line)  # Add line
            line = []  # Reset line data
            i = 0  # Reset line counter
        else:  # Same line
            if letter in ENGLISH_ALPHABET:  # Only get letter count if it is part of the alphabet
                position = to_number(letter)  # Get the position of that letter
                line.append(letter_count[position])  # Get the letter count of that letter
            else:
                line.append(0)  # If it is in the alphabet, just use a 0 count
            i += 1  # Add one to word count for this line

    return matrix

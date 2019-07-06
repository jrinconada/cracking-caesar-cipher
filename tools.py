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
    total = 0
    for letter_count in count:
        total += letter_count

    frequencies = []
    for letter_count in count:
        frequencies.append((letter_count / total) * 100)

    return frequencies

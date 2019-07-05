from tools import ENGLISH_ALPHABET
from tools import to_number
import matplotlib.pyplot as plt


def plot(letter_count, name):
    alphabet = list(ENGLISH_ALPHABET)
    plt.style.use('seaborn')
    plt.plot(alphabet, letter_count, label=name)


def show():
    plt.legend()
    plt.show()


def count_letters(message):
    """ Goes through every letter in the message and counts how many times it appears """
    letter_count = [0] * len(ENGLISH_ALPHABET)  # Create a list of zeroes to start with count zero for every letter

    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only count the letter if it is part of the alphabet
            position = to_number(letter)  # Get the position of the letter (a = 0, b = 1, c = 2...)
            letter_count[position] += 1  # Add one to the counter of this letter

    return letter_count

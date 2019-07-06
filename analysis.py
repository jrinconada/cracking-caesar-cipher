from tools import ENGLISH_ALPHABET
from tools import to_number
import matplotlib.pyplot as plt


THEORETICAL_FREQUENCIES = [12.7, 9.06, 8.17, 7.51, 6.97, 6.75, 6.33, 6.09, 5.99, 4.25, 4.02, 2.78, 2.76,
                           2.41, 2.36, 2.23, 2.01, 1.97, 1.93, 1.49, 0.99, 0.77, 0.15, 0.15, 0.09,  0.07]

ALPHABET_SORTED_BY_FREQUENCY = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u',
                                'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']


def theoretical():
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.pie(THEORETICAL_FREQUENCIES, labels=ALPHABET_SORTED_BY_FREQUENCY, autopct='%1.1f%%')
    ax2.bar(ALPHABET_SORTED_BY_FREQUENCY, THEORETICAL_FREQUENCIES)


def plot(letter_count, name):
    alphabet = list(ENGLISH_ALPHABET)
    plt.style.use('seaborn')
    plt.plot(alphabet, letter_count, label=name)
    # data = [1,2,3,4]
    # plt.scatter(x=data, y=data, c=data, cmap='RdYlGn')


def show():
    # plt.legend()
    plt.show()


def count_letters(message):
    """ Goes through every letter in the message and counts how many times it appears """
    letter_count = [0] * len(ENGLISH_ALPHABET)  # Create a list of zeroes to start with count zero for every letter

    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only count the letter if it is part of the alphabet
            position = to_number(letter)  # Get the position of the letter (a = 0, b = 1, c = 2...)
            letter_count[position] += 1  # Add one to the counter of this letter

    return letter_count

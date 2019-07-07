from tools import ENGLISH_ALPHABET
from tools import to_number
from tools import sort
from tools import count_to_frequency
import matplotlib.pyplot as plt
import numpy as np


THEORETICAL_FREQUENCIES = [12.7, 9.06, 8.17, 7.51, 6.97, 6.75, 6.33, 6.09, 5.99, 4.25, 4.02, 2.78, 2.76,
                           2.41, 2.36, 2.23, 2.01, 1.97, 1.93, 1.49, 0.99, 0.77, 0.15, 0.15, 0.09,  0.07]

ALPHABET_SORTED_BY_FREQUENCY = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u',
                                'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']


def theoretical():
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.pie(THEORETICAL_FREQUENCIES, labels=ALPHABET_SORTED_BY_FREQUENCY, autopct='%1.1f%%')
    ax2.bar(ALPHABET_SORTED_BY_FREQUENCY, THEORETICAL_FREQUENCIES)


def theoretical_vs_actual(sample_letter_count):
    # Sort in alphabetical order
    theoretical_frequencies, alphabet = sort(THEORETICAL_FREQUENCIES, ALPHABET_SORTED_BY_FREQUENCY, by_number=False)
    actual_frequencies = count_to_frequency(sample_letter_count)  # Get letter frequency from letter count
    # Plot
    plt.title('Letter frequency comparison')
    plt.plot(alphabet, theoretical_frequencies, linestyle='--', color='gray', label='Theoretical')
    plt.plot(alphabet, actual_frequencies, color='darkgray', label='Actual')
    # Fill
    plt.fill_between(alphabet, theoretical_frequencies, actual_frequencies,  # Fill green bellow the actual frequencies
                     where=np.array(theoretical_frequencies) <= np.array(actual_frequencies),
                     interpolate=True, color='green', alpha=0.3)
    plt.fill_between(alphabet, theoretical_frequencies, actual_frequencies,  # Fill red above the actual frequencies
                     where=np.array(theoretical_frequencies) > np.array(actual_frequencies),
                     interpolate=True, color='red', alpha=0.3)


def plot(letter_count, name):
    alphabet = list(ENGLISH_ALPHABET)
    plt.style.use('seaborn-muted')
    plt.plot(alphabet, letter_count, label=name)
    # data = [1,2,3,4]
    # plt.scatter(x=data, y=data, c=data, cmap='RdYlGn')


def show(legend=True):
    if legend:
        plt.legend()
    plt.show()


def stackplot(plain, caesar, vigenere):
    alphabet = list(ENGLISH_ALPHABET)
    names = ['Plain text', 'Caesar cipher', 'Vigenère cipher']
    plt.style.use('seaborn')
    plt.stackplot(alphabet, plain, caesar, vigenere, labels=names)


def count_letters(message):
    """ Goes through every letter in the message and counts how many times it appears """
    letter_count = [0] * len(ENGLISH_ALPHABET)  # Create a list of zeroes to start with count zero for every letter

    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only count the letter if it is part of the alphabet
            position = to_number(letter)  # Get the position of the letter (a = 0, b = 1, c = 2...)
            letter_count[position] += 1  # Add one to the counter of this letter

    return letter_count

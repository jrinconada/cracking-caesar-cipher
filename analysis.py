from tools import ENGLISH_ALPHABET
from tools import to_number
from tools import sort
from tools import count_to_frequency
from tools import to_matrix
import matplotlib.pyplot as plt
import numpy as np


THEORETICAL_FREQUENCIES = [12.7, 9.06, 8.17, 7.51, 6.97, 6.75, 6.33, 6.09, 5.99, 4.25, 4.02, 2.78, 2.76,
                           2.41, 2.36, 2.23, 2.01, 1.97, 1.93, 1.49, 0.99, 0.77, 0.15, 0.15, 0.09, 0.07]

ALPHABET_SORTED_BY_FREQUENCY = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u',
                                'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']


def theoretical():
    """ Shows theoretical letter count plotted as a pie chart and a bar chart sorted by frequency """
    plt.style.use('seaborn-muted')  # Set display style
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']  # Get cycle of colors
    plt.title('Theoretical letter frequency for the English alphabet')  # Set plot title

    plt.bar(ALPHABET_SORTED_BY_FREQUENCY, THEORETICAL_FREQUENCIES, color=colors)  # Show bar chart

    # For the pie chart to be nicer, last 8 frequencies displayed together
    alphabet_pie = ALPHABET_SORTED_BY_FREQUENCY[:-7]  # Remove the last 8 letters for the pie chart
    alphabet_pie.append('y - z')  # Put the last 8 as a single part of the pie
    frequencies_pie = THEORETICAL_FREQUENCIES[:-7]  # # Remove the last 8 frequencies
    frequencies_pie.append(3.71)  # Add the las 8 frequencies together
    ax = plt.axes([.35, .27, .6, .6])  # Draw the pie chart inside the bar chart
    ax.pie(frequencies_pie, labels=alphabet_pie, autopct='%.1f', pctdistance=0.8)  # Show pie chart


def theoretical_vs_actual(sample_letter_count):
    """ Given  a sample letter count plots side by side with the theoretical letter frequency for comparison """
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
    """ Given a list of count for every letter in alphabetical order and a name displays the counts as a line plot """
    plt.style.use('seaborn-muted')  # Set display style
    alphabet = list(ENGLISH_ALPHABET)  # Get a list from a string with all the letters in the alphabet
    plt.plot(alphabet, letter_count, label=name)  # Plot the line using the alphabet as x and the count as y


def show(legend=True):
    """ Display the plots, legend is shown by default """
    if legend:
        plt.legend()
    plt.show()


def matrix(message, letter_count):
    """ Show letter count as a matrix of colors, the more intense the color, the more frequent the letter is """
    letter_count_matrix = to_matrix(message, letter_count)  # Transform the message to a matrix with every letter count
    plt.imshow(letter_count_matrix)  # Plot the matrix
    plt.colorbar()  # Show a color bar for reference
    plt.title('Letter frequency for every letter in the message')


def count_letters(message):
    """ Goes through every letter in the message and counts how many times it appears """
    letter_count = [0] * len(ENGLISH_ALPHABET)  # Create a list of zeroes to start with count zero for every letter

    for letter in message:  # For every letter in the message
        if letter in ENGLISH_ALPHABET:  # Only count the letter if it is part of the alphabet
            position = to_number(letter)  # Get the position of the letter (a = 0, b = 1, c = 2...)
            letter_count[position] += 1  # Add one to the counter of this letter

    return letter_count

import sys
import cipher
import storage
import analysis


def usage():
    return """
    Usage: main.py encrypt/decrypt caesar-key vigenere-key [message] [-i in.txt] [-o out.txt]
    Ciphers: For Caesar cipher the key is an integer. For Vigènere cipher is a word.
    Examples:
        main.py encrypt 13 thekey hello
        main.py e 13 thekey hello
        main.py e 5 anotherkey this is a longer message
        main.py decrypt -1 thisisverystrongkey hal
        main.py encrypt 13 thekey -i letter.txt -o secret.txt"""


# Validate number of arguments
if len(sys.argv) < 5:
    print(usage())  # Invalid number of arguments
    exit(-1)

# Encryption or decryption
encrypt = True if sys.argv[1][0] == 'e' else False

# Get the input
if '-i' in sys.argv:  # Get message from file
    if not storage.file_exists(sys.argv[5]):  # Check if file exists
        print('File not found.')
        exit(-1)
    message = storage.read(sys.argv[5])
else:  # Get message from arguments
    message = ' '.join(sys.argv[4:])

# Get the keys
key_caesar = eval(sys.argv[2])  # In the Caesar cipher the key is an integer number
key_vigenere = sys.argv[3]  # In Vigenere cipher the key is a word

# Apply ciphers
caesar = cipher.caesar(message.lower(), key_caesar, encrypt)
vigenere = cipher.vigenere(message.lower(), key_vigenere.lower(), encrypt)

# Output results
results = 'CAESAR CIPHER:\n' + caesar + '\n\nVIGENERE CIPHER:\n' + vigenere
if '-o' in sys.argv:  # Write result to file
    i = sys.argv.index('-o')
    storage.write(sys.argv[i + 1], results)
else:  # Write result to console
    print(results)

# Analise by counting the letter in the alphabet
plain_letter_count = analysis.count_letters(message.lower())
caesar_letter_count = analysis.count_letters(caesar)
vigenere_letter_count = analysis.count_letters(vigenere)

# Show theoretical letter frequency
analysis.theoretical()
analysis.show(legend=False)

# Show comparison between theoretical and actual letter frequency
analysis.theoretical_vs_actual(plain_letter_count)
analysis.show()

# Show a matrix of letter frequency
analysis.matrix(message, plain_letter_count)
analysis.show(legend=False)

# Show letter count analysis comparing original text, Caesar and Vigenère ciphers
analysis.plot(plain_letter_count, 'Plain text')
analysis.plot(caesar_letter_count, 'Caesar cipher')
analysis.plot(vigenere_letter_count, 'Vigenère cipher')
analysis.show()

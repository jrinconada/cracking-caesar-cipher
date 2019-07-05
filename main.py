import sys
import cipher
import storage
import analysis


def usage():
    return """
    Usage: main.py [cipher] [encrypt/decrypt] [key] [message] [-i in.txt] [-o out.txt]
    Ciphers: caesar vigenere
    Examples:
        main.py caesar encrypt 13 hello
        main.py c e 13 hello
        main.py v e thekey this is a longer message
        main.py caesar decrypt -1 hal
        main.py caesar encrypt 13 -i letter.txt -o secret.txt"""


plain = storage.read('test_files/einstein.txt')
caesar = cipher.caesar(plain.lower(), 2)
vigenere = cipher.vigenere(plain.lower(), 'uncertainty')
analysis.plot(analysis.count_letters(plain.lower()), 'Plain text')
analysis.plot(analysis.count_letters(caesar), 'Caesar cipher')
analysis.plot(analysis.count_letters(vigenere), 'Vigenère cipher')
analysis.show()
# if len(sys.argv) < 5:
#     print(usage())  # Invalid number of arguments
#     exit(-1)
#
# method = sys.argv[1][0]  # caesar or vigenere
# choice = sys.argv[2][0]  # encryption or decryption
#
# if '-i' in sys.argv:  # Message from file
#     message = storage.read(sys.argv[5])
# else:  # Message from arguments
#     message = ' '.join(sys.argv[4:])
#
# if method == 'c':  # Caesar cipher
#     key = eval(sys.argv[3])  # In the Caesar cipher the key is an integer number
#     if choice == 'e':  # Encryption
#         result = cipher.caesar(message.lower(), key)
#     elif choice == 'd':  # Decryption
#         result = cipher.caesar(message.lower(), key, False)
#     else:
#         result = usage()  # Invalid argument
# elif method == 'v':  # Vigenere cipher
#     key = sys.argv[3]  # In Vigenere cipher the key is a word
#     if choice == 'e':  # Encryption
#         result = cipher.vigenere(message.lower(), key.lower())
#     elif choice == 'd':  # Decryption
#         result = cipher.vigenere(message.lower(), key.lower(), False)
#     else:
#         result = usage()  # Invalid argument
# else:
#     result = usage()  # Invalid argument
#
# if '-o' in sys.argv:  # Result to file
#     i = sys.argv.index('-o')
#     storage.write(sys.argv[i + 1], result)
# else:  # Result to console
#     print(result)

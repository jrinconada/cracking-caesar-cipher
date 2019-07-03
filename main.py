import sys
import cipher
import storage
import analysis


def usage():
    manual = 'Usage: main.py [cipher] [encrypt/decrypt] [key] [message] [-i in.txt] [-o out.txt]'
    manual += 'Ciphers: caesar vigenere'
    manual += 'Examples:'
    manual += '\tmain.py caesar encrypt 13 hello'
    manual += '\tmain.py c e 13 hello'
    manual += '\tmain.py v e thekey this is a longer message'
    manual += '\tmain.py caesar decrypt -1 hal'
    manual += '\tmain.py caesar encrypt 13 -i letter.txt -o secret.txt'
    return manual


analysis.show()

#
# if len(sys.argv) < 5:
#     print(usage())
#     exit(-1)
#
# method = sys.argv[1][0]
# choice = sys.argv[2][0]
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
#         result = usage()
# elif method == 'v':  # Vigenere cipher
#     key = sys.argv[3]  # In Vigenere cipher the key is a word
#     if choice == 'e':  # Encryption
#         result = cipher.vigenere(message.lower(), key.lower())
#     elif choice == 'd':  # Decryption
#         result = cipher.vigenere(message.lower(), key.lower(), False)
#     else:
#         result = usage()
# else:
#     result = usage()
#
# if '-o' in sys.argv:  # Result to file
#     i = sys.argv.index('-o')
#     storage.write(sys.argv[i + 1], result)
# else:  # Result to console
#     print(result)

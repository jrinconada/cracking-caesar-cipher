import sys
import cipher


def usage():
    print('Usage: main.py [cipher] [encrypt/decrypt] [key] [message]')
    print('Ciphers: caesar vigenere')
    print('Examples:')
    print('    main.py caesar encrypt 13 hello')
    print('    main.py c e 13 hello')
    print('    main.py v e thekey this is a longer message')
    print('    main.py caesar decrypt -1 hal')
    exit(-1)


if len(sys.argv) < 5:
    usage()

method = sys.argv[1][0]
choice = sys.argv[2][0]
message = ' '.join(sys.argv[4:])

if method == 'c':  # Caesar cipher
    key = eval(sys.argv[3])  # In the Caesar cipher the key is an integer number
    if choice == 'e':  # Encryption
        result = cipher.caesar(message.lower(), key)
        print(result)
    elif choice == 'd':  # Decryption
        result = cipher.caesar(message.lower(), key, False)
        print(result)
    else:
        usage()
elif method == 'v':  # Vigenere cipher
    key = sys.argv[3]  # In Vigenere cipher the key is a word
    if choice == 'e':  # Encryption
        result = cipher.vigenere(message.lower(), key.lower())
        print(result)
    elif choice == 'd':  # Decryption
        result = cipher.vigenere(message.lower(), key.lower(), False)
        print(result)
    else:
        usage()
else:
    print('Invalid choice')
    usage()

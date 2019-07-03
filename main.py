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

if method == 'c':
    key = eval(sys.argv[3])
    if choice == 'e':
        result = cipher.caesar(message.lower(), key)
        print(result)
    elif choice == 'd':
        result = cipher.caesar(message.lower(), key, False)
        print(result)
    else:
        usage()
else:
    print('Invalid choice')
    usage()

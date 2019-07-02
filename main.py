import caesar

print('1. Encryption')
print('2. Decryption')
choice = input('Your choice: ')
message = input('Message: ')
if choice == '1':
    secret = caesar.encrypt(message.lower(), -1)
    print(secret)
elif choice == '2':
    secret = caesar.decrypt(message.lower(), -1)
    print(secret)
else:
    print('Invalid choice')

# Cracking Caesar Cipher
Visualising letter frequency in encrypted massages using *Caesar* and *Vigenère* ciphers.

## About the encryption
For simplicity, characters that are not part of the English alphabet are ignored by the cipher and included in the final result.
Some explamples of ignored characters are: spaces, numbers, punctuation, symbols, other alphabet letters...

In a real life example this characters may also be encrypted to preserve the integrity of the original message and not to give out any structural clues that might aid to the cracking the encoded message.

## Usage
Written in **Python 3** using **matplotlib** for the graphs and **numpy** for some number and list processing.

To run the program the following parameters must be specified:
- **Option**: `encrypt` or `decrypt` or `e` or `d` to choose encryption or decryption of the message.
- **Caesar cipher key**: Must be an *integer* number.
- **Vigenère cipher key**: Must be word composed of letters from *a* to *z*.
- **Message**: Can be typed directly in the console or read from a file with option `-i`.
- **Result** [optional]: By default the result is shown in the console, it can be saved to a file with option `-o`.

### General form 
```
python main.py encrypt/decrypt caesar-key vigenere-key [message] [-i in.txt] [-o out.txt]
```
### Usage examples
```
main.py encrypt 13 thekey hello
main.py e 13 thekey hello
main.py e 5 anotherkey this is a longer message
main.py decrypt -1 thisisverystrongkey hal
main.py encrypt 13 thekey -i letter.txt -o secret.txt
```

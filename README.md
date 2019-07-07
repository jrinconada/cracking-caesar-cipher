# Cracking Caesar Cipher
Visualising letter frequency in encrypted massages using *Caesar* and *Vigenère* ciphers.
## Usage
Written in **Python 3** using **matplotlib** for the graphs and **numpy** for some number and list processing.

To run the program the following parameters must be specify:
- **Option**: `encrypt` or `decrypt` or `e` or `d` to choose encryption or decryption of the message.
- **Caesar cipher key**: Must be an *integer* number.
- **Vigenère cipher key**: Must be word composed of letters from *a* to *z*.
- **Message**: Can be written directly in the console or from a file with option `-i`.
- **Result**: By default the result is shown in the console, it can be or to a file with option `-o`.
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
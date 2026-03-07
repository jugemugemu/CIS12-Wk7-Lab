from os import system, name # Allows the clearing of the terminal window for cleaner user experience

def vigenere_sq_header(alphabet:str):
    """Prints the first row (header) of the Vigenere square

    :param alphabet: the alphabet used to make the Vigenere square.
    """
    print('|  ', end=' | ')
    for char in alphabet:
        print(char, end= ' | ')
    print()
    print(f'{'|---' * (len(alphabet) + 1)}|')

def vigenere_sq_body(alphabet:str):
    """Prints the body of the Vigenere square.

    :param alphabet: the alphabet used to make the Vigenere square
    """
    for i in range(len(alphabet)):
        j = i
        print('|', alphabet[j], end=' | ')
        for _ in range(len(alphabet)):
            j = j % len(alphabet)
            print(alphabet[j], end=' | ')
            j += 1
        print('')

def vigenere_sq(alphabet:str):
    """Prints the full Vigenere square

    :param alphabet: the alphabet used to make the Vigenere square
    """
    vigenere_sq_header(alphabet)
    vigenere_sq_body(alphabet)

def letter_to_index(letter:str, alphabet:str) -> int:
    """ Returns the index of the letter in the given alphabet.

    :param letter: the letter whose position in the alphabet is being found
    :param alphabet: the alphabet used as an index for the letters
    """
    if letter not in alphabet:
        raise 'ERROR: Letter not in alphabet.'
    for i, c in enumerate(alphabet):
        if c == letter:
            return i
    return -1

def index_to_letter(index:int, alphabet:str) -> str:
    """Returns the letter in the given alphabet based on its index.

    :param index: the place in the alphabet where the letter resides
    :param alphabet: the alphabet used as an index for the letters
    """
    if not 0 <= index < len(alphabet):
        raise 'ERROR: Index out of bounds.'
    return alphabet[index]

def vigenere_index(key_letter:str, plaintext_letter:str, alphabet:str) -> str:
    """Returns an encrypted character using a key character and the Vigenere cipher.

    :param key_letter: the character used to encrypt the plaintext character
    :param plaintext_letter: the character to be encrypted
    :param alphabet: the alphabet used by the Vigenere cipher to encrypt and decrypt
    :return: the ciphertext (encrypted) character
    """
    ciphertext_index = (letter_to_index(plaintext_letter, alphabet) +
                        letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(ciphertext_index, alphabet)

def undo_vigenere_index(key_letter:str, ciphertext_letter:str, alphabet:str) -> str:
    """Returns the decrypted character using a key character and the Vigenere cipher.

    :param key_letter: the character used to decrypt the ciphertext character
    :param ciphertext_letter: the character to be decrypted
    :param alphabet: the alphabet used by the Vigenere cipher to encrypt and decrypt
    :return: the plaintext (original, unencrypted) character
    """
    plaintext_index = (letter_to_index(ciphertext_letter, alphabet) -
                        letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(plaintext_index, alphabet)

def encrypt_vigenere(key:str, plaintext:str, alphabet:str) -> str:
    """Returns encrypted string (ciphertext) using a key string and the Vigenere cipher.

    :param key: the string used to encrypt the plaintext
    :param plaintext: the string to be encrypted
    :param alphabet: the alphabet used by the Vigenere cipher to encrypt and decrypt
    :return: the ciphertext
    """
    ciphertext = ''
    for i, c in enumerate(plaintext):
        ciphertext += vigenere_index(key[i % len(key)], c, alphabet)
    return ciphertext

def decrypt_vigenere(key:str, ciphertext:str, alphabet:str) -> str:
    """Returns decrypted string (plaintext) using a key string and the Vigenere cipher.

    :param key: the string used to decrypt the ciphertext
    :param ciphertext: the string to be decrypted
    :param alphabet: the alphabet used by the Vigenere cipher to encrypt and decrypt
    :return: the plaintext
    """
    plaintext = ''
    for i, c in enumerate(ciphertext):
        plaintext += undo_vigenere_index(key[i % len(key)], c, alphabet)
    return plaintext

def clear_terminal():
    """Detects the OS and clears the terminal, then displays the name of the calculator."""
    if name == 'nt': # Windows
        system('cls')
    else: # Unix-like OS (e.g. Linux, MacOS)
        system('clear')
    print("VIGENERE CIPHER CALCULATOR")

def error_msg(error_id:int = 0):
    """Prints error messages based on error codes reached when incorrectly using the UI.

    :param error_id: the error code used to map to error message strings
    """
    ERRORS = ('',
              'INPUT ERROR - INT BETWEEN 1 AND 4 NOT ENTERED',
              'INPUT ERROR - ALPHABET DOES NOT CONTAIN ALL CHARS IN KEY OR TEXT'
    )
    if error_id != 0:
        print(ERRORS[error_id])

def in_alphabet(key:str, text:str, alphabet:str) -> bool:
    """Returns True or False if the all characters in key and text are in alphabet.

    :param key: the key in the Vigenere cipher
    :param text: the plaintext or ciphertext in the Vigenere cipher
    :param alphabet: the alphabet used to encrypt and decrypt by the Vigenere cipher
    :returns: True if chars in key and text are in alphabet, False if not
    """
    for char in key + text:
        if char not in alphabet:
            return False
    return True

def menu_select():
    """Main menu to select encryption, decryption, show Vigenere square, or exit."""
    error = 0
    while True:
        clear_terminal()
        error_msg(error)

        print('Select option below: \n'
              '[1] Encrypt \n'
              '[2] Decrypt \n'
              '[3] Show Table \n'
              '[0] Exit')
        user_input = input('> ')

        if user_input == '1':
            crypt_menu(int(user_input) - 1)
            error = 0
        elif user_input == '2':
            crypt_menu(int(user_input) - 1)
            error = 0
        elif user_input == '3':
            show_table()
            error = 0
        elif user_input == '0':
            break
        else:
            error = 1 # INVALID INPUT - ENTER INT BETWEEN 1 AND 4

def crypt_menu(selection):
    """Calculates and prints plaintext or ciphertext based on user-inputted key, text, and alphabet.

    :param selection: determines whether to do encryption (0) or decryption (1)
    """
    error = 0
    TEXT_TYPE = ('PLAINTEXT', 'CIPHERTEXT')
    DEFAULT_TEXT = ('THE EAGLE HAS LANDED', 'WHZHRCOOEUPNUHOAHLRF')
    DEFAULT_KEY = 'DAVINCI'
    DEFAULT_ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

    while True:
        clear_terminal()
        error_msg(error)

        # Get plaintext/ciphertext from user, default if nothing is entered
        print(f"INSERT {TEXT_TYPE[selection]} (DEFAULT '{DEFAULT_TEXT[selection]}'):")
        text = input('> ') or DEFAULT_TEXT[selection]

        # Get key from user, default if nothing is entered
        print(f"INSERT KEY (DEFAULT '{DEFAULT_KEY}')")
        key = input('> ') or DEFAULT_KEY

        # Get alphabet from user, default if nothing is entered
        print(f"INSERT ALPHABET (DEFAULT '{DEFAULT_ALPHABET}'")
        alphabet = input('> ') or DEFAULT_ALPHABET

        # Ensure encrypt_vigenere or decrypt_vigenere has valid data before calling, otherwise produce error
        if in_alphabet(key, text, alphabet): # All characters found in alphabet, conduct encryption/decryption
            print()
            print(f'{TEXT_TYPE[(selection + 1) % 2]}')
            if selection == 0:
                print(encrypt_vigenere(key, text, alphabet))
            else:
                print(decrypt_vigenere(key, text, alphabet))
            break
        else: # Not all characters are found in alphabet, raise error
            error = 2 # INPUT ERROR - ALPHABET DOES NOT CONTAIN ALL CHARS IN KEY OR TEXT
    print()
    print('PRESS ENTER TO RETURN TO MENU')
    input('> ')

def show_table():
    """Displays a Vigenere square based on user-inputted alphabet."""
    DEFAULT_ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

    clear_terminal()

    print(f"INSERT ALPHABET (DEFAULT '{DEFAULT_ALPHABET}'")
    alphabet = input('> ') or DEFAULT_ALPHABET

    vigenere_sq(alphabet)

    print()
    print('PRESS ENTER TO RETURN TO MENU')
    input('> ')

if __name__ == '__main__':
    #alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #alphabet = alphabet + alphabet.upper() + ' '

    #print(letter_to_index('A', alphabet))
    #print(index_to_letter(0, alphabet))
    #vigenere_sq()
    #print(vigenere_index('k', 'h', alphabet))

    #KEY = 'DAVINCI'
    #PLAINTEXT = 'The Eagle has landed'
    #ciphertext = encrypt_vigenere(KEY, PLAINTEXT, alphabet)
    #print(ciphertext)
    #print(decrypt_vigenere(KEY, ciphertext, alphabet))

    menu_select() # Run program in OS terminal with command `python lab06.py` for best results

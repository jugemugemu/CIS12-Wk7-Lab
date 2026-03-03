alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet + ' ' + alphabet.upper()

def vigenere_sq_header():
    print('|  ', end=' | ')
    for char in alphabet:
        print(char, end= ' | ')
    print()
    print(f'{'|---' * (len(alphabet) + 1)}|')

def vigenere_sq_body():
    for i in range(len(alphabet)):
        j = i
        print('|', alphabet[j], end=' | ')
        for _ in range(len(alphabet)):
            j = j % len(alphabet)
            print(alphabet[j], end=' | ')
            j += 1
        print('')

def vigenere_sq():
    vigenere_sq_header()
    vigenere_sq_body()

def letter_to_index(letter:str, alphabet:str) -> int:
    """ Returns the index of the letter in the given alphabet

    @letter: (str) the letter to look for
    @alphabet: (str) the alphabet that is used
    """
    if letter not in alphabet:
        raise 'ERROR: Letter not in alphabet.'
    for i, c in enumerate(alphabet):
        if c == letter:
            return i
    return -1

def index_to_letter(index:int, alphabet:str) -> str:
    if not 0 <= index < len(alphabet):
        raise 'ERROR: Index out of bounds.'
    return alphabet[index]

def vigenere_index(key_letter:str, plaintext_letter:str, alphabet:str) -> str:
    ciphertext_index = (letter_to_index(plaintext_letter, alphabet) +
                        letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(ciphertext_index, alphabet)

def encrypt_vigenere(key:str, plaintext:str, alphabet:str) -> str:
    ciphertext = ''
    for i, c in enumerate(plaintext):
        ciphertext += vigenere_index(key[i % len(key)], c, alphabet)
    return ciphertext

if __name__ == '__main__':
    #print(letter_to_index('A', alphabet))
    #print(index_to_letter(0, alphabet))
    #vigenere_sq()
    #print(vigenere_index('k', 'h', alphabet))

    KEY = 'DAVINCI'
    PLAINTEXT = 'The Eagle has landed'
    print(encrypt_vigenere(KEY, PLAINTEXT, alphabet))
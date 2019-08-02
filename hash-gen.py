'''Basic CLI for hashing files using Python'''

from sys import argv
from hashlib import sha256, sha384, sha512
from base64 import encodebytes
import chardet


def hash_file(file, hashStrategy):
    """
        Takes a file and hashObject, instantiates the hash object,
        updates it with the file, and returns a hash digest that is "decoded".
    """
    print(type(file))

    """
        Changes the encoding of the file from a Python string to unicode bytes is required
        by the hashing object. 
        
        Remember, in Python, everythin is an object! All strings are in fact collections
        of characters AND! have methods like `rstrip()`, `encode()` and many more which
        can be called.

        A more detailed explanation of strings, unicode and bytes in Python can be found at:
        https://timothybramlett.com/Strings_Bytes_and_Unicode_in_Python_2_and_3.html
    """
    
    text = file.encode('utf8') # Encodes the file as a byte string
    
    hashStrategy.update(text) # updates the hash strategy instance with the encoded file text

    hash = hashStrategy.digest() # get the hash digest as bytes - 

    return encodebytes(hashStrategy.digest()).decode() # returns the hash digest as base64 to remove special characters that could cause problems in an HTML document


def sha256_strategy():
    '''Returns an instance of the sha256 object'''
    return sha256()


def sha384_strategy():
    '''Returns an instance of the sha384 object'''
    return sha384()


def sha512_strategy():
    '''Returns an instance of the sha512 object'''
    return sha512()


def get_file(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except:
        print('Error reading file')


def hash_workflow(path, hash_algo):
    file = get_file(path)
    hash_digest = ''
    if hash_algo == 'sha256':
        hash_digest = hash_file(file, sha256_strategy())
    elif hash_algo == 'sha384':
        hash_digest = hash_file(file, sha384_strategy())
    elif hash_algo == 'sha512':
        hash_digest = hash_file(file, sha512_strategy())
    else:
        print('Error with hashing algorithm.\n Check the hash algorithm is `sha256`, `sha384` or `sha512`')
    return hash_digest


if __name__ == "__main__":
    print('Argv: ', argv)
    if argv[1] is not None and argv[2] is not None:
        hash = hash_workflow(argv[1], argv[2])
        print('Hash digest:', hash)
    else:
        print('Please include the correct number of arguments. Ensure the first argument is a file path, and the second is either `sha256`, `sha384`, or `sha512`')

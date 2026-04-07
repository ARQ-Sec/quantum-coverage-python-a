from Crypto.Cipher import ARC4

def execute():
    # rule_key: quantum.arq-q-0255-python
    legacy_cipher = "RC4"
    ARC4.new(b"legacy-rc4-key")

if __name__ == '__main__':
    execute()

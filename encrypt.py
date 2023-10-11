from Crypto.Cipher import AES
import hashlib


def encrypt_data(key, filename):
    chunksize = 65536
    outfile = filename + ".enc"
    iv = b"0000000000000000"
    hasher = hashlib.sha256(key.encode())
    key = hasher.digest()

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    with open(filename, "rb") as infile, open(outfile, "wb") as outfile:
        outfile.write(iv)

        while True:
            chunk = infile.read(chunksize)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += b" " * (16 - len(chunk) % 16)

            outfile.write(encryptor.encrypt(chunk))


if __name__ == "__main__":
    key = input("Enter encryption key: ")
    encrypt_data(key, "data.py")

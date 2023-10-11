import os
import platform
import requests
import json


def get_os_name():
    return platform.system()


def get_ip_address():
    url = "https://api.ipify.org/"
    return requests.get(url).text


def get_coordinates():
    url = "https://ipapi.co/json/"
    data = requests.get(url).json()
    return f"{data['latitude']},{data['longitude']}"


def get_location_data():
    url = "https://ipapi.co/json/"
    data = requests.get(url).json()
    return {
        "city": data["city"],
        "region": data["region"],
        "country": data["country"],
        "postal_code": data["postal"],
    }


def write_data_to_json(name, age, location, reason, change, os_name, ip_address, coordinates, location_data, time, json_file, email):
    # Collect data
    data = {
        "name": name,
        "age": age,
        "location": location,
        "reason": reason,
        "change": change,
        "os_name": os_name,
        "ip_address": ip_address,
        "coordinates": coordinates,
        "location_data": location_data,
        "time": time,
    }
    
    # Write data to JSON file
    with open(json_file, "w") as f:
        json.dump(data, f)
    
    # Send email with JSON data
    # Implementation for sending email
              
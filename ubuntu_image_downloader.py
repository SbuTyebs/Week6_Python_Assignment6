import requests
import os
from urllib.parse import urlparse

def fetch_image(image_url):
    # Create the directory if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)

    # Extract filename from URL
    parsed_url = urlparse(image_url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "image.jpg"  # Default name if URL doesn't provide one

    filepath = os.path.join(directory, filename)

    # Download the image
    response = requests.get(image_url, stream=True)

    # Check for HTTP errors
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image downloaded to {filepath} 🎉")
    else:
        print(f"Failed to download image. Status code: {response.status_code} 😞")

# Prompt the user for a URL
image_url = input("Please enter the URL of the image: ")
fetch_image(image_url)
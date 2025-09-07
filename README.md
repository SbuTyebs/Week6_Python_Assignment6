# Week6_Python_Assignment6

# Ubuntu Image Fetcher 📸

A Python script inspired by the Ubuntu philosophy of community and sharing, designed to fetch images from the web. It embodies the principles of respect, practicality, and community by mindfully collecting images and organizing them for later use.

## Features ✨

- **User-Friendly**: Greets the user with a welcoming message.
- **URL Input**: Prompts the user to enter an image URL.
- **Directory Creation**: Automatically creates a directory named `Fetched_Images` if it doesn't already exist.
- **Image Fetching**: Downloads the image from the provided URL.
- **Error Handling**: Gracefully handles connection errors and bad status codes.
- **Filename Extraction**: Extracts the filename from the URL or generates a default name if one isn't available.
- **Image Saving**: Saves the image in binary mode to the `Fetched_Images` directory.
- **Success/Error Messages**: Provides clear feedback on whether the image was successfully fetched and saved.

## How to Use 🚀

1.  **Prerequisites**:

- Python 3.x installed
- `requests` library: Install via pip: `pip install requests`

2.  **Running the Script**:

- Save the script as `image_fetcher.py`.
- Run the script from your terminal: `python image_fetcher.py`

3.  **Instructions**:

- Enter the URL of the image when prompted.
- The image will be downloaded and saved to the `Fetched_Images` directory.

## Example Output 🖼️

```text
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web


Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg


Connection strengthened. Community enriched.
```

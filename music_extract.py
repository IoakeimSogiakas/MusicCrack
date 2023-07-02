import os
import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://musescore.com/user/31132549/scores/5903735'

try:
    # Send a GET request to the URL and fetch the HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was not successful
    html_content = response.content

    # Extract image URLs using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = []
    for img in soup.find_all('img', class_="EEnGW F16e6 YVkCb"):
        image_urls.append(img['src'])

    # Create a directory to save the downloaded images
    save_directory = 'downloaded_images'
    os.makedirs(save_directory, exist_ok=True)

    # Download the images
    for i, image_url in enumerate(image_urls):
        response = requests.get(image_url)
        if response.status_code == 200:
            file_path = os.path.join(save_directory, f'image{i+1}.jpg')
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Downloaded image {i+1}/{len(image_urls)}: {file_path}')
        else:
            print(f'Failed to download image {i+1}/{len(image_urls)}')

except requests.exceptions.RequestException as e:
    print(f'Error occurred during the request: {e}')

except Exception as e:
    print(f'An error occurred: {e}')

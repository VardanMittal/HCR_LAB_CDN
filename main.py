"""This is a script helps in scrape all the images from the lab news page of HCR lab website and save them in a folder named labNewsImages"""

from bs4 import BeautifulSoup
import requests
import os
import urllib

url = 'https://labs.iitgn.ac.in/hcr-lab/lab-news/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

imgs = soup.find_all('img')
folder = "labNewsImages"

print(f"Found {len(imgs)}")

def orignal_images(img):
    images = []
    for img in imgs:
        img_url = img.get("src")
        if not img_url.startswith("data:image"):
            images.append(img_url)
    return images


images = orignal_images(imgs)
print(f"Found {len(images)}")


if not os.path.exists(folder):
    os.makedirs(folder)

for img in images:
    img_url = img.split('//')[-1]
    file_name = urllib.parse.urlsplit(img_url.split('/')[-1])._replace(query='').geturl()
    link = f"https://{img_url}"
    print(f"Downloading {file_name} from {link}")
    file_path = os.path.join(folder, file_name)
    urllib.request.urlretrieve(link, file_path)
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import pyinputplus as pyip
import os
from PIL import Image


# Downloading the images from the page


# Check if the url is valid
def is_valid(url) -> bool:
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# Look for all the images into the page
# Note! This will not work with pages where images are using JS or have many tags over them!
def get_images_urls(url) -> list:
    soup = bs(requests.get(url).content, "html.parser")  # get all the content from the page using beautiful soup
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")  # check if image contains src, else - skip it
        if not img_url:
            continue
        img_url = urljoin(url, img_url)  # make an absolute path to img_url
        try:
            pos = img_url.index("?")  # remove urls like '/hsts-pixel.gif?c=3.2.5'
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)  # if url is ok add it to the list
    return urls


def download(url, pathname):
    response = requests.get(url)  # download the body of response
    file_size = int(response.headers.get("Content-length", 0))
    filename = os.path.join(pathname, url.split("/")[-1])  # relative path to the file
    with open(filename, "wb") as file:
        for data in response:
            file.write(data)  # write data to the file
            print(f'Downloading... {filename}, size: ({round(file_size / 1024, 2)})mb')


# Resizing the images and save them


def resize_images(width, height):
    start_path = './images/'  # path to the folder with images
    if not os.path.exists('./resizedImages'):  # create a resizedImages folder
        os.mkdir('./resizedImages')
    dest_path = './resizedImages/'
    for filename in os.listdir(start_path):  # resize and save every image in the images folder
        img = Image.open(start_path + filename)
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(filename)  # image will be saved into imgDownloader folder
        os.rename(filename, dest_path + filename)  # move image from imgDownloader folder to the resizedImages


# Main function

def main(url, path, width, height):
    # get all images
    images = get_images_urls(url)  # images contains only essential urls for images that we will download
    for img in images:
        # for each img, download it
        download(img, path)
    resize_images(width, height)


if __name__ == "__main__":
    user_url = pyip.inputURL('Please input url: ')
    user_width = pyip.inputInt('Please input width of the images: ')
    user_height = pyip.inputInt('Please input height of the images: ')
    main(user_url, './images', user_width, user_height)  # all the images will be in images folder

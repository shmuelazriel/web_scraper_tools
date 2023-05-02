import os
import requests
from bs4 import BeautifulSoup

# The URL of the website to crawl
url = input("Enter URL: ")

# The local directory to save the downloaded contents
output_dir = 'output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# A set to keep track of the visited pages to avoid duplicates
visited_pages = set()

def download_page(url):
    # Make an HTTP GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the links in the page
    links = soup.find_all('a')

    # Iterate through the links and download their contents
    for link in links:
        href = link.get('href')
        if href and href.startswith(url) and href not in visited_pages:
            visited_pages.add(href)
            download_page(href)

    # Save the page content to a file
    filename = os.path.join(output_dir, url[len('https://'):].replace('/', '_').strip('_'))
    with open(filename, 'wb') as f:
        f.write(response.content)

# Start crawling the website from the homepage
download_page(url)

import requests
from bs4 import BeautifulSoup

# Set the URL of the website to crawl
url = input("Enter URL: ")

# Make a GET request to the URL and create a BeautifulSoup object from the response content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a sitemap HTML file
sitemap_file = open('sitemap.html', 'w')
sitemap_file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Sitemap for ' + url + '</title>\n</head>\n<body>\n')

# Find all the <a> tags in the BeautifulSoup object
links = soup.find_all('a')

# Write each link to the sitemap file
for link in links:
    href = link.get('href')
    if href is not None and href.startswith('http'):
        sitemap_file.write('<a href="' + href + '">' + href + '</a><br/>\n')

# Close the sitemap file
sitemap_file.write('</body>\n</html>')
sitemap_file.close()

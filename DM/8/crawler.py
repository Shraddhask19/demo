# Import libraries
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse


# Set for storing urls with same domain
links_intern = set()
input_url = "http://snap.stanford.edu/data/#web/"
depth = 1

# Set for storing urls with different domain
links_extern = set()


# Method for crawling a url at next level
def level_crawler(input_url):
	temp_urls = set()
	current_url_domain = urlparse(input_url).netloc

	# Creates beautiful soup object to extract html tags
	beautiful_soup_object = BeautifulSoup(
		requests.get(input_url).content, "lxml")

	# Access all anchor tags from input
	# url page and divide them into internal
	# and external categories
	for anchor in beautiful_soup_object.findAll("a"):
		href = anchor.attrs.get("href")
		if(href != "" or href != None):
			href = urljoin(input_url, href)
			href_parsed = urlparse(href)
			href = href_parsed.scheme
			href += "://"
			href += href_parsed.netloc
			href += href_parsed.path
			final_parsed_href = urlparse(href)
			is_valid = bool(final_parsed_href.scheme) and bool(
				final_parsed_href.netloc)
			if is_valid:
				if current_url_domain not in href and href not in links_extern:
					print("Extern - {}".format(href))
					links_extern.add(href)
				if current_url_domain in href and href not in links_intern:
					print("Intern - {}".format(href))
					links_intern.add(href)
					temp_urls.add(href)
	return temp_urls


if(depth == 0):
	print("Intern - {}".format(input_url))

elif(depth == 1):
	level_crawler(input_url)

else:
	# We have used a BFS approach
	# considering the structure as
	# a tree. It uses a queue based
	# approach to traverse
	# links upto a particular depth.
	queue = []
	queue.append(input_url)
	for j in range(depth):
		for count in range(len(queue)):
			url = queue.pop(0)
			urls = level_crawler(url)
			for i in urls:
				queue.append(i)










# import logging
# from urllib.parse import urljoin
# import requests
# from bs4 import BeautifulSoup

# logging.basicConfig(
#     format='%(asctime)s %(levelname)s:%(message)s',
#     level=logging.INFO)

# class Crawler:

#     def __init__(self, urls=[]):
#         self.visited_urls = []
#         self.urls_to_visit = urls

#     def download_url(self, url):
#         return requests.get(url).text

#     def get_linked_urls(self, url, html):
#         soup = BeautifulSoup(html, 'html.parser')
#         for link in soup.find_all('a'):
#             path = link.get('href')
#             if path and path.startswith('/'):
#                 path = urljoin(url, path)
#             yield path

#     def add_url_to_visit(self, url):
#         if url not in self.visited_urls and url not in self.urls_to_visit:
#             self.urls_to_visit.append(url)

#     def crawl(self, url):
#         html = self.download_url(url)
#         for url in self.get_linked_urls(url, html):
#             self.add_url_to_visit(url)

#     def run(self):
#         while self.urls_to_visit:
#             url = self.urls_to_visit.pop(0)
#             logging.info(f'Crawling: {url}')
#             try:
#                 self.crawl(url)
#             except Exception:
#                 logging.exception(f'Failed to crawl: {url}')
#             finally:
#                 self.visited_urls.append(url)

# if __name__ == '__main__':
#     Crawler(urls=['http://snap.stanford.edu/data/#web']).run()



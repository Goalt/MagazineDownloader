import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def getURLDisk(htmlText):
	soup = BeautifulSoup(htmlText, features="html.parser")
	item = soup.find('div', {'class': 'post2 singlepost2'})
	return item.p.a.get("href")

def getURLImage(htmlText):
	soup = BeautifulSoup(htmlText, features="html.parser")
	item = soup.find('div', {'class': 'post2 singlepost2'})
	return item.p.a.img.get("src")

def getTitle(htmlText):
	soup = BeautifulSoup(htmlText, features="html.parser")
	item = soup.find('div', {'class': 'post2 singlepost2'})
	return item.p.a.img.get("title")

def getItemInfo(url):
	r = requests.get(url)
	o = urlparse(url)
	urlImage = o.scheme + "://" + o.netloc + getURLImage(r.text)
	title = getTitle(r.text)
	urlDisk = getURLDisk(r.text)
	return (title, urlImage, urlDisk)

# Returns url of last release
def getLast(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, features="html.parser")
	item = soup.find('div', {'id': 'contentindex'})
	return item.find('div', {'class': 'zagnomera'}).h3.a.get("href")

# Save str to file
def save(s, fileName):
	f = open(fileName, "w")
	f.write(s)
	f.close()

# Read str from file
def read(fileName):
	f = open(fileName, "r")
	s = f.read()
	f.close()
	return s
import urllib.request
from urllib.parse import quote
import filecmp
import os.path
import string

webPages = []

def addWebPage(name, url):
	webPage = {'name': name, 'url': url}
	webPages.append(webPage)

def downloadWebPage(url):
	response = urllib.request.urlopen(webPages[0]['url']) 
	return response.read().decode('utf-8')
	

def saveToFile(data, filename):
	file = open(filename, 'w')
	file.write(data)
	file.close()

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

addWebPage('nu.nl homepage', 'https://www.budgetgaming.nl/')
#response = downloadWebPage(webPages[0]['url'])
#saveToFile(response, 'kappa.txt')

#print(filecmp.cmp('kappa.txt', 'kappa.txt'))


for webPage in webPages:
	url = webPage['url']
	oldFileName = format_filename(quote(url)) + '.old'
	response = downloadWebPage(url)

	if os.path.exists(oldFileName):
		newFileName = format_filename(quote(url)) + '.new'
		saveToFile(response, newFileName)
		
		if filecmp.cmp(oldFileName, newFileName):
			pass
			print('kappa')
			#no changes
		else:
			print('there are changes to ' + webPage['name'])
			#changes
	else:
		saveToFile(response, oldFileName)
	

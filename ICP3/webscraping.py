#importing required libraries
import requests
from bs4 import BeautifulSoup
import re

class Webscrape :
# get URL to perform scraping using request
    wiki = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
    soup = BeautifulSoup(wiki.text, "html.parser")
    # displaying the title
    def display_title(self):
        for title in self.soup.find_all('title'):
            print('\033[1m' + "Title of the website is : ",title.get_text() + '\033[0m') # prints title in bold letters

# Find all the links in the page (‘a’ tag)
    def display_all_links(self):
        f = open("allLinks.txt", "w")              # opening a file in write mode
        # traverse paragraphs from soup
        for link in self.soup.find_all("a"):
                data = str(link.get('href'))
                f.write(data)
                f.write("\n")
        f.close()
        print('\033[1m' +"All links output is stored in webscrape1.txt file "+ '\033[0m')

# Iterate over each tag(above) then return the link using attribute "href" using get
    def display_href_links(self):
        f = open("hreflinks.txt", "w")
        # traverse paragraphs from soup and has attribute href to find all links
        for link in self.soup.find_all("a",attrs={'href': re.compile("^http")}):
            data = str(link.get('href'))
            f.write(data)
            f.write("\n")
        f.flush()
        f.close()
        print('\033[1m' + "All href output links are stored in webscrape2.txt file  " + '\033[0m')

if __name__ == '__main__':
    # create class Webscrape object
    web = Webscrape()
    # call functions to dispaly title,all links and href links
    web.display_title()
    web.display_all_links()
    web.display_href_links()









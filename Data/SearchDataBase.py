import requests
from bs4 import BeautifulSoup
import re
import random

class PoemScraper:

    choice = None
    soup = None
    results = None
    poemList = None
    page1, page2, randomPage = "","",""
    poemLink = ""

    def __init__(self, mood):
        self.mood = mood

    def choiceDict (self):
        # define id of the category
        choices = {
            'milosc': 1,
            'erotyk': 2,
            'nadzieja': 3,
            'wiara': 4,
            'przyjazn': 5,
            'zycie': 6,
            'zyczenia': 7,
            'okazyjne': 8,
            'dladzieci': 9,
            'przyroda': 10,}
        self.choice = str(choices.get(self.mood))
        return self.choice

    def getHtml_content (self):

        #retrieve HTML content
        URL = 'https://www.twojecentrum.pl/poezja.php?catid=' + self.choiceDict() + '&page=1'
        page= requests.get(URL)
        #parsing data from the URL
        self.soup = BeautifulSoup(page.content, 'html.parser')
        return self.soup

    def getPage (self):
        #store the whole text on 0 position of an array
        page0=self.results.find(text=re.compile('^Strona:*'))
        page0 = page0[:-3]
        #store the position of '/' dividing the number of pages
        slashPosition=(page0.index("/"))
        #store the position of first digit of first page
        pageStart=(page0.index(" ")+1)
        for i in range (0, int(slashPosition-pageStart)):
            self.page1 = str(self.page1) + str(page0[pageStart+i])
        #store the position of last digit of last page
        pageEnd=len(page0)-1
        for i in range (0, int(pageEnd-slashPosition)):
            self.page2 = str(self.page2) + str(page0[slashPosition+1+i])
        return self.page1, self.page2

    def getRandomPage (self):
        self.randomPage = (random.randint(int(self.page1), int(self.page2)))
        #print(self.randomPage)
        return self.randomPage

    def getHtml (self):

        #retrieve HTML content
        URL = 'https://www.twojecentrum.pl/poezja.php?catid=' + self.choiceDict() + '&page=' + str(self.randomPage)
        page= requests.get(URL)
        #parsing data from the URL
        self.soup = BeautifulSoup(page.content, 'html.parser')
        return self.soup

    def findId (self):
        self.results = self.soup.find(id = 'container')
        return self.results

    def findClass (self):
        self.poemList= self.results.find("ul", class_="list circle")
        return self.poemList


    def getPoemLink (self):
        a=self.poemList.find_all('a')
        counter = 0
        poemLinks = []
        for poem_elem in a:
            counter = counter + 1
            poemLinks.append(poem_elem.attrs['href'])
        self.poemLink=(poemLinks[random.randint(0, counter-1)])
        #print(self.poemLink)
        return self.poemLink

    def getPoemText (self):
        # retrieve HTML content
        URL = 'https://www.twojecentrum.pl/' + self.poemLink
        page = requests.get(URL)
        # parsing data from the URL
        self.soup = BeautifulSoup(page.content, 'html.parser')
        self.results = self.soup.find(id='container')
        poemContainer = self.results.find("div", class_="two_third first")
        poemText = poemContainer
        #Write a poem down
        for br in poemText.find_all('br'):
            br.replace_with('\n')
        return poemText.text















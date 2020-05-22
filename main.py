from SearchDataBase import PoemScraper

def main():
    mypoem = PoemScraper(mood='milosc')
    mypoem.choiceDict()
    mypoem.getHtml_content()
    mypoem.findId()
    mypoem.getPage()
    mypoem.getRandomPage()
    mypoem.getHtml()
    mypoem.findId()
    mypoem.findClass()
    mypoem.getPoemLink()
    mypoem.getPoemText()



if __name__ == "__main__":
    main()


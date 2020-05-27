from Data.SearchDataBase import PoemScraper


def poemFind(category):
    mypoem = PoemScraper(mood=str(category))
    mypoem.choiceDict()
    mypoem.getHtml_content()
    mypoem.findId()
    mypoem.getPage()
    mypoem.getRandomPage()
    mypoem.getHtml()
    mypoem.findId()
    mypoem.findClass()
    mypoem.getPoemLink()
    text = mypoem.getPoemText()
    return text


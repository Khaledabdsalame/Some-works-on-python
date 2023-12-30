import requests
import bs4
import random
while True:
    randome=input("what is type of fovorite quotes")
    quotes=requests.get("https://www.goodreads.com/quotes/tag/"+randome)
    html=quotes.text
    html_perser=bs4.BeautifulSoup(html, "html.parser")
    quote=html_perser.findAll("div",attrs={"class":"quoteText"})
    random_num=random.randint(1,12)
    print(quote[random_num].text)

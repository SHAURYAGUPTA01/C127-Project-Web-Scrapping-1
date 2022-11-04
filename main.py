from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver")
browser.get(starturl)
time.sleep(10)

def scrape() :
    headers = ["Proper_name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 10):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for j in soup.find_all("tr") :
            tdtag = j.find_all("td")
            templist = []
            for index,s in enumerate(tdtag):
                if index == 1 :
                    templist.append(s.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(s.contents[1,4,6,7])
                    except:
                        templist.append("")
    star_data.append(templist)
    with open("scrapper.csv","w") as f:
        c = csv.writer(f)
        c.writerow(headers)
        c.writerows(star_data)
        
scrape()
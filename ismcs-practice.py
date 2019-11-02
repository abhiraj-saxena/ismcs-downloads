import requests
from bs4 import BeautifulSoup as bs 
from selenium import webdriver

url = 'http://www.medicalmediapartner.com/ismcs/'
#C:/webdrivers/chromedriver
driver = webdriver.Firefox(executable_path='/mnt/c/webdrivers/geckodriver.exe')

driver.get(url)

html = driver.execute_script("return document.documentElement.outerHTML")

sel_soup = bs(html, "html.parser")

download_mp4_list = []
mp4_list = []
date_list = []
name_list = []
title_list = []

for main in sel_soup.find_all('div', class_= 'modal-content ng-scope'):
    for main2 in sel_soup.find_all('ul', class_ = 'collection'):
        for main3 in sel_soup.find_all('li', class_ = 'collection-item avatar hoverable ng-scope'):
            for links in sel_soup.find_all('a'):
                #download_mp4_list.append(links['href'])
                for date in sel_soup.find_all('p', class_= "giorno-sessione ng-binding"):
                    date_list.append(date)
                    with open('date1.txt', 'a') as f:
                        print(date_list[0:126], file=f)
                for name in sel_soup.find_all("p", class_ = "relatore ng-binding"):
                    name_list.append(name)
                    with open('name1.txt', 'a') as f:
                        print(name_list[0:126], file=f)
                for title in sel_soup.find_all("p", class_ = "relazione ng-binding"):
                    title_list.append(title)
                    with open('title1.txt', 'a') as f:
                        print(title_list[0:126], file=f)
                
# #print(date_list[1:127])

# with open('html4.txt', 'a') as f:
# print(name.text, file=f)
#print(download_mp4_list[1:127])
print(date_list[1:127])
# print(name_list[1:127])
# print(title_list[1:127])

# with open('html_3.txt', 'a') as f:
#     print(date_list, file=f)

# prepscraper v0.1
# Pulls the daily announcments from scrantonprep.com and saves them to a text file.
# Code by Ethan MacDonald 3/11/16

from selenium import webdriver
driver = webdriver.Chrome()
url = "http://scrantonprep.com/s/139/index.aspx?sid=139&gid=1&pgid=478"
driver.get(url)
anns = driver.find_element_by_xpath('//*[@id="ContentMiddle"]/div')
print (anns.text)
file = open("daily_anns.txt", "w")
file.write(anns.text)

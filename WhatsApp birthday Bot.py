import pandas as pd
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

# XXS Paths

searchBox='//*[@id="side"]/div[1]/div/label/div/div[2]'
messageBox='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
# Chrome drivers
PATH ='C:\Program Files (x86)\Google\chromedriver.exe'
# for cookies
chrome_cookies = Options()
chrome_cookies.add_argument("--user-data-dir=\\chrome-data")
driver = webdriver.Chrome(PATH,options=chrome_cookies)
    
def msg_sender(cntname, message):
    sel_contact(cntname)
    elementfinder(messageBox,message)

def sel_contact(cntname):
    url='https://web.whatsapp.com' 
    driver.get(url)
    time.sleep(10)
    elementfinder(searchBox,cntname)
    
def elementfinder(element,keys):
    search = driver.find_element_by_xpath(element)
    search.send_keys(Keys.RETURN)
    search.send_keys(keys)
    search.send_keys(Keys.RETURN)

if __name__ == "__main__":
    df = pd.read_excel("demo.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index, item in df.iterrows():
        bday = item['Birthday']
        if(today == bday) and yearNow not in str(item['Year']):
            msg_sender(str(item['Name']), str(item['message'])) 
            writeInd.append(index)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
    df.to_excel('contact birthday.xlsx', index=False)   

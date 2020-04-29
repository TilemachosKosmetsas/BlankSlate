import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


query = input("Dwse ton titlo  tis Tainias:  ")

y= True

query2=query.replace(" ",".")

driver = webdriver.Chrome()
driver.get('https://rarbg.to/index8.php')

try:
    elem1 = driver.find_element_by_link_text("Movies")
    elem1.click()
except Exception as e: 
    print (" DEN YPARXEI TO LINK Movies , %s" % e)




if (len(driver.window_handles) == 2):
    curWindowHndl = driver.current_window_handle
    driver.switch_to_window(driver.window_handles[1])
    driver.close() #closes new tab
    

driver.switch_to_window(driver.window_handles[0])   #gurizei tin prosoxh stin monh kartela
                 
inputElement1= driver.find_element_by_id('searchinput')
inputElement1.send_keys(query2)            #stelnei to keimeno sti mpara gia search
inputElement1.submit()


driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table[2]/tbody/tr[1]/td[5]/a').click() #list by max seeders


try:
    driver.find_element_by_partial_link_text(query2).click()  #prwta dokimh me teleies
    
except Exception as e: 
    print (" Den yparxei h tainia grammenh me teleies , %s" % e)
    try:
        driver.find_element_by_partial_link_text(query).click()    #meta me kena
       
    except Exception as e:
        print (" Den yparxei h tainia auth  , %s" % e)
        print (" Den yparxei h tainia auth  , %s" % e)
        print (" Den yparxei h tainia auth  , %s" % e)
        y= False

if (y== True):
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/a[1]').click()

if (len(driver.window_handles) == 2):
    curWindowHndl = driver.current_window_handle
    driver.switch_to_window(driver.window_handles[1])
    driver.close() #closes new tab
    

driver.switch_to_window(driver.window_handles[0])
time.sleep(5)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') # kleinei ton browser


path = 'C:\\Users\\Burgundy\\Downloads'


if (y == True):
    files=[]

    os.chdir(path)
    for file in os.listdir(path):
            files.append(file)
            sortefil = sorted (files,key=os.path.getmtime)
    assert isinstance(sortefil, object)
    print(sortefil[-1])

    assert isinstance(sortefil, object)
    os.startfile(sortefil[-1])
    


if 2==2:
    x=input("press Enter to exit")


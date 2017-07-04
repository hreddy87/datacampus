import os
from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def evaluate(s):
    global driver
    global html
    global url
    global idd
    global var
    eval(s)

def multick(string,times=1000):
    global driver
    global file
    for n in range(times):
        kick=0
        
        try:
            evaluate(string)
            kick=1
        except:
            if n==times-1:
                time.sleep(1)
                return 0
            continue

        
        if kick==1:
            time.sleep(1)
            return 1
   
binary = FirefoxBinary('C:/Users/harshith reddy/Downloads/geckodriver-v0.17.0-win32/geckodriver.exe')
driver = webdriver.Firefox(executable_path='C:/Users/harshith reddy/Downloads/geckodriver-v0.17.0-win32/geckodriver.exe')
driver.get("https://www.datacamp.com/")
multick("driver.find_element_by_xpath(\"//*[@id='logged-out-header']/div/div[1]/div[2]/div/div/a[3]/i\").click()")
multick("driver.find_element_by_xpath('//*[@id=\"identifierId\"]').send_keys('h.reddy87@gmail.com')")
multick("driver.find_element_by_xpath('//*[@id=\"identifierNext\"]/content/span').click()")
multick("driver.find_element_by_xpath('//*[@id=\"password\"]/div[1]/div/div[1]/input').send_keys('Vihaan!23')")
multick("driver.find_element_by_xpath(\"//*[@id='passwordNext']/content\").click()")
multick("https://campus.datacamp.com/courses/importing-and-managing-financial-data-in-r/extracting-and-transforming-data-2?ex=1")
f1,f2,f3,f4,f5,idd,url,var=0,0,0,0,0,None,None,None
while True:
    multick("driver.find_element_by_link_text('Continue').click()",10)
    time.sleep(2)
    f1,f2,f3,f4,f5=0,0,0,0,0
    f1=multick("driver.find_element_by_partial_link_text('Got').click()",100)
    

   
    if f1!=1:
        f2=multick("driver.find_element_by_partial_link_text('Hint').click()",100)

    if f2==1:
        f3=multick("driver.find_element_by_partial_link_text('Show').click()",100)
        if f3==1:
            try:
                time.sleep(2)
                html = driver.execute_script('return document.getElementsByTagName("html")[0].innerHTML')
                soup = BeautifulSoup(html, 'html.parser')
                idd=soup.findAll("div",{"id":re.compile("ace-code-editor-(\d){1,}$")})[-1]["id"]

                var="//*[@id='"+idd+"']/textarea"
                driver.find_element_by_xpath(var).send_keys(Keys.CONTROL,'a')
                time.sleep(0.5)
                driver.find_element_by_xpath(var).send_keys(Keys.CONTROL,'c')
                url=driver.current_url
                multick("driver.get(url)")
                time.sleep(2)
                html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")            
                soup = BeautifulSoup(html, 'html.parser')
                idd=soup.find("div",{"id":re.compile("ace-code-editor-(\d){1,}$")})["id"]
                var="//*[@id='"+idd+"']/textarea"
                driver.find_element_by_xpath(var).send_keys(Keys.CONTROL,'a')
                time.sleep(0.5)
                driver.find_element_by_xpath(var).send_keys(Keys.CONTROL,'v')
                driver.find_element_by_xpath(var).send_keys(Keys.CONTROL,Keys.SHIFT,Keys.ENTER)
                g1=multick("driver.find_element_by_link_text('Continue').click()",100)
                continue

            except:
                multick("driver.get(url)")
                continue
                
                

            
        
    else:
        try:
            if len(driver.find_elements_by_xpath("//*[@type='radio']"))<3:
                continue
                print(3)
            for i in range(6):
                try:
                    driver.find_element_by_xpath('//*[@id="gl-aside"]').click()   
                    driver.find_element_by_xpath('//*[@id="gl-aside"]').send_keys(str(i+1))
                    driver.find_element_by_xpath('//*[@id="gl-aside"]').send_keys(Keys.CONTROL,Keys.SHIFT,Keys.ENTER)

                except:
                     driver.find_element_by_xpath('//*[@id="rendered-view"]').click()
                     driver.find_element_by_xpath('//*[@id="rendered-view"]').send_keys(str(i+1))
                     driver.find_element_by_xpath('//*[@id="rendered-view"]').send_keys(Keys.CONTROL,Keys.SHIFT,Keys.ENTER)
                     
                    
                time.sleep(0.2)
                g1=multick("driver.find_element_by_link_text('Continue').click()",100)
                if g1==1:
                    break
                continue
        except:
            multick("driver.get(url)")
            continue
                
                

        
            
            
            
            
            
            
                
                    
                
                
                
                    
                
            


        
        
        
        
                    
                

        
    

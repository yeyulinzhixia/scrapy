from selenium import webdriver
import time 
browser = webdriver.Chrome(executable_path=r'C:\Users\王祥霖\AppData\Local\Programs\Python\Python37\Lib\site-packages\chromedriver')

browser.get('https://accounts.pixiv.net/login')
browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[1]/input').send_keys('479892367@qq.com')
browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[2]/input').send_keys('13678475618zl')
browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/button').click()
time.sleep(10)


for i in range(1,19):
    browser.get('https://www.pixiv.net/users/21405138/bookmarks/artworks?p=%d' % i )
    time.sleep(10)
    # browser.find_element_by_xpath('/html/body/div[9]/div/form/section/div[1]/button').click()
    #获取
    for list in range(1,49):
        x = browser.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div[1]/section/ul/li[%d]/div/div[1]/div/a/div[2]/img' % list).text
        print(x)




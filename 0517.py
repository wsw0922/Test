from bs4 import BeautifulSoup
import requests

# headers = {"User-Agent" : "Dongyang"}
# web = requests.get("https://n.news.naver.com/mnews/article/001/0013946648?sid=105", headers = headers)
# print(web)
# # print(web.content)
# s = BeautifulSoup(web.content, "html.parser")
# print(s)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get("https://www.naver.com/")
# time.sleep(3)

# driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
# time.sleep(5)

# newsTitle1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
# print(newsTitle1)
# newsTitle2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[4]/a/div[2]/div").text
# print(newsTitle2)

# driver.get("https://m.land.naver.com/search")
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
# time.sleep(1)
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]").click()
# time.sleep(1)

# rentPrice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
# print(rentPrice)
# memePrice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]/dd").text
# print(memePrice)
# addr = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[3]/article[4]/div[2]/p[1]").text
# print(addr)

driver.get("https://finance.naver.com/")

subject1 = driver.find_element(By.XPATH, "").
subject2 = driver.find_element(By.XPATH, "").
subject3 = driver.find_element(By.XPATH, "").
print(subject1, subject2, subject3)
print("===========================================")

lst =[]
for i in range(10):
    subject = driver.find_element(By.XPATH, f"").text
    lst.append(subject)
print(lst)

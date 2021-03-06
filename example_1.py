#!/usr/bin
# -*- coding: UTF-8 -*-
# 自动登录
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://121.43.61.190")

elem = browser.find_element_by_xpath("/html/body/header/ul/li[5]/a")
elem.send_keys(Keys.RETURN)
try:
    emailInput = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "userName")))
    pswInput = browser.find_element_by_id("passWord")
    loginBtn = browser.find_element_by_id("login-btn")
except Exception, e:
    print Exception, ":", e
    browser.quit()
    sys.exit()

emailInput.send_keys("nmzfrank@sjtu.edu.cn")
pswInput.send_keys("123")
time.sleep(1)
loginBtn.click()

try:
    # applicationTab = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "new-form")))
    loading = WebDriverWait(browser, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-overlay")))
except Exception, e:
    print Exception, ":", e
    browser.quit()
    sys.exit()

applicationTab = browser.find_element_by_class_name("new-form")
html = applicationTab.get_attribute("innerHTML")
print html
applicationTab.click()

try:
    formName = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "formTitle")))
except Exception, e:
    print Exception, ":", e
    browser.quit()
    sys.exit()

formName.send_keys("selenium_test");

fileUploader = browser.find_element_by_xpath('//*[@id="fileAddBtn11"]')
fileUploader.click()

time.sleep(2);
formInput = browser.find_element_by_id('fileAddBtn11')
formInput.click();
time.sleep(1);
formSave = browser.find_element_by_id("saveList")
formSave.click();
time.sleep(5)
browser.quit()



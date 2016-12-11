#!/usr/bin
# -*- coding: utf-8 -*-
from testAuxiliary import sqtWebdriver
from selenium.webdriver.common.by import By

sqt_test = sqtWebdriver("http://121.43.61.190")
login = sqt_test.find_element_by_xpath("/html/body/header/ul/li[5]/a")
login.click()
# 登录页面
user = sqt_test.find_element_by_id("userName")
pswd = sqt_test.find_element_by_id("passWord")
submit = sqt_test.find_element_by_id("login-btn")
user.send_keys("nmzfrank@sjtu.edu.cn")
pswd.send_keys("123")
submit.click()
# 首页
newForm = sqt_test.find_first_element_in_page("emptyForm", By.CLASS_NAME)
newForm.click()
# 新建表单
formTitle = sqt_test.find_first_element_in_page("formTitle", By.ID)
formTitle.send_keys("selenium_test")
singleLine = sqt_test.find_element_by_xpath('//*[@id="model-select"]/li[2]/a/span')
singleLine.click()
singleLineTitle = sqt_test.find_element_by_xpath('//div[@class="model-edit-top"]/div[1]/input')
singleLineTitle.clear()
singleLineTitle.send_keys("1111")
singlineSave = sqt_test.find_element_by_class_name("form-save")
singlineSave.click()
saveFormBtn = sqt_test.find_element_by_id("saveList")
saveFormBtn.click()
# 表单编辑页面
sqt_test.find_first_element_in_page("form-audit-link", By.CLASS_NAME).click()
# 流程设置页面
sqt_test.find_first_element_in_page('//ul[@class="auditor-container"]/li/a', By.XPATH).click()

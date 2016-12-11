#!/usr/bin
# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class sqtWebdriver():
    """docstring for SQT-webdriver"""
    def __init__(self, host):
        self.browser = webdriver.Chrome()
        self.browser.get(host)

    def find_element_by_id(self, elem_selector):
        try:
            target_element = self.browser.find_element_by_id(elem_selector)
        except exceptions.NoSuchElementException:
            try:
                target_element = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.ID, elem_selector)))
            except exceptions.TimeoutException:
                print "can not find element with id: ", elem_selector
                self.browser.quit()
                sys.exit()
        return target_element

    def find_element_by_class_name(self, elem_selector):
        try:
            target_element = self.browser.find_element_by_class_name(elem_selector)
        except exceptions.NoSuchElementException:
            try:
                target_element = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, elem_selector)))
            except exceptions.TimeoutException:
                print "can not find element with id: ", elem_selector
                self.browser.quit()
                sys.exit()
        return target_element

    def find_element_by_css_selector(self, elem_selector):
        try:
            target_element = self.browser.find_element_by_css_selector(elem_selector)
        except exceptions.NoSuchElementException:
            try:
                target_element = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, elem_selector)))
            except exceptions.TimeoutException:
                print "can not find element with id: ", elem_selector
                self.browser.quit()
                sys.exit()
        return target_element

    def find_element_by_xpath(self, elem_selector):
        try:
            target_element = self.browser.find_element_by_xpath(elem_selector)
        except exceptions.NoSuchElementException:
            try:
                target_element = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, elem_selector)))
            except exceptions.TimeoutException:
                print "can not find element with id: ", elem_selector
                self.browser.quit()
                sys.exit()
        return target_element

    def find_first_element_in_page(self, elem_selector, by):
        try:
            WebDriverWait(self.browser, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-overlay")))
        except exceptions.TimeoutException:
            print "check your network"
            self.browser.quit()
            sys.exit()
        try:
            target_element = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((by, elem_selector)))
        except exceptions.TimeoutException:
            print "can not find element with id: ", elem_selector
            self.browser.quit()
            sys.exit()
        return target_element

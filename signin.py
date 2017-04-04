'''
Created on 03/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time
from lib2to3.tests.support import driver
if __name__ == '__main__':
    driver=webdriver.Firefox()
    time.sleep(1)
    driver.get("http://www.firstnaukri.com/freshersmnj/mynaukri.php/ForgotPassword/showForgotPassword")
    time.sleep(1)
    #driver.find_element_by_xpath("//img[@src='http://static.naukimg.com/sfnr/images/fn_logo.gif']").click()
    #time.sleep(1)
    #driver.find_element_by_xpath("//div[@id='spanid_qf']").click()
    #time.sleep(3)
    #driver.find_element_by_xpath("//a[text()='MCA']").click()
    #time.sleep(3)
    #element=driver.find_element_by_name("ql")
    #element.clear()
    #element.send_keys("bangalore")
    #time.sleep(3)
    #element=driver.find_element_by_name("qp")
    #element.clear()
    #element.send_keys("python")
    #driver.find_element_by_xpath("//input[@value='Search']").click()
    #time.sleep(3)
    #driver.find_element_by_xpath("//span[@class='loc'] ").click()
    #time.sleep(3)
    driver.find_element_by_id("btnsubmit").click()
    driver.find_element_by_xpath("//a[@class='cancel']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@onclick='flogin();']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//label[@id='loginbutton']").click()
    #frame = driver.find_element_by_xpath('//frame/button[@class="fn_logBtn fn_mR5 fn_fL"]')
    #driver.switch_to.frame(frame)
    

    
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
    driver.get("http://www.firstnaukri.com/freshersmnr/MNR.php/Register/register")
    time.sleep(1)
    driver.find_element_by_xpath("//img[@src='http://static.naukimg.com/sfnr/images/fn_logo.gif']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='spanid_qf']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[text()='MCA']").click()
    time.sleep(3)
    element=driver.find_element_by_name("ql")
    element.clear()
    element.send_keys("bangalore")
    time.sleep(3)
    element=driver.find_element_by_name("qp")
    element.clear()
    element.send_keys("python")
    driver.find_element_by_xpath("//input[@value='Search']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[@class='loc'] ").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span/button[text()=' Apply Now ']").click()
   
    

    

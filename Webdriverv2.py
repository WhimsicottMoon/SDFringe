#Veronica Tang, 06/14/18

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import sys
import time

amountoff = "100"
desc = " Show Pass"
tagnum = [1, 3, 4, 5, 25, 44]#index starts a 1, stupid Ticketleap
startdate = "06/15/18" #mm/dd/yy
starttime = "12:00"
startampm = "am"
enddate = "07/03/18" #mm/dd/yy
endtime = "12:00"
endampm = "am"

list = [line.rstrip('\n') for line in open('NewCodes.txt')]
for code in list:
    code = code[2:]

def testcode(code):
    if code[:2] == "03":
        return "3"
    elif code[:2] == "05":
        return "5"
    elif code[:2] == "10":
        return "10"
    else:
        return "1"
class Testcode123(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://veronicatangfringe.ticketleap.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_code123(self):
        driver = self.driver
        driver.get("http://www.ticketleap.com/login/?next=http%3A//veronicatangfringe.ticketleap.com/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("chenk21@mit.edu")
        driver.find_element_by_id("id_password").clear()
        #sub in your password here you stupid Pikachu
        driver.find_element_by_id("id_password").send_keys("screw you")
        driver.find_element_by_id("email_login_button").click()
        time.sleep(1)
        for code in list:
            driver.get("about:home")
            time.sleep(1)
            driver.get("https://veronicatangfringe.ticketleap.com/admin/promote/discount-codes/#dialog=/admin/promote/discount-code/add")
            driver.find_element_by_id("id_assigned_to_0").click()
            time.sleep(1)
            driver.find_element_by_id("id_code").clear()
            driver.find_element_by_id("id_code").send_keys(code)
            driver.find_element_by_id("id_description").clear()
            driver.find_element_by_id("id_description").send_keys(testcode(code)+ desc)
            #we never do amount off anymore, so this next part gets to go
            #driver.find_element_by_id("id_type_1").click()
            #driver.find_element_by_xpath("//table[@id='discount_code_type_toggle']/tbody/tr/td[2]/div/label[2]").click()
            #driver.find_element_by_id("id_amount").clear()
            driver.find_element_by_id("id_amount").send_keys("100")
            #start date
            driver.find_element_by_id("id_start_date").send_keys(startdate)
            driver.find_element_by_id("id_start_date").click()
            driver.find_element_by_id("id_start_time").clear()
            driver.find_element_by_id("id_start_time").send_keys(starttime)
            Select(driver.find_element_by_id("id_start_ampm")).select_by_visible_text(startampm)
            #end date
            driver.find_element_by_id("id_end_date").send_keys(enddate)
            driver.find_element_by_id("id_end_date").click()
            driver.find_element_by_id("id_end_time").clear()
            driver.find_element_by_id("id_end_time").send_keys(endtime)
            Select(driver.find_element_by_id("id_end_ampm")).select_by_visible_text(endampm)
            #excluding certain ones
            Select(driver.find_element_by_id("id_scope")).select_by_visible_text("Specific Events")
            driver.find_element_by_css_selector("div.tl-fs-select").click()
            driver.find_element_by_css_selector("span.tl-fs-dd-header-label").click()
            for x in range (0, len(tagnum)):
                driver.find_element_by_xpath("//*[@id='undefined-dropdown']/div/ul[2]/li["+str(tagnum[x])+"]/label/input").click()
                #print(tagnum[x])
            driver.find_element_by_css_selector("button.tl-fs-dd-done.secondary-button").click()
            if(testcode(code)!="Unlimited"):
                #selecting limit uses
                driver.find_element_by_id("id_limit_uses_2").click()
                driver.find_element_by_xpath("//form[@id='discount-code-form']/div[2]/table[11]/tbody/tr/td[2]/div/label[3]").click()
                #max uses
                driver.find_element_by_id("id_maximum_ticket_uses").clear()
                driver.find_element_by_id("id_maximum_ticket_uses").send_keys(testcode(code))
            driver.find_element_by_name("submit").click()
            print(code)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

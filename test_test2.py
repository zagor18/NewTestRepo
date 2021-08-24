# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test2(self):
    self.driver.get("https://the-internet.herokuapp.com/")
    self.driver.set_window_size(947, 970)
    self.driver.find_element(By.LINK_TEXT, "Inputs").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("77")
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("76")
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("75")
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "input")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("74")
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
  

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_check(browser):
  browser.get(link)

  time.sleep(30)

  assert  browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket"), "Кнопки добавления в корзину нет"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getURL():
    StockQuoteWebsite = "https://money.rediff.com/"
    return StockQuoteWebsite

def getSearchTextBox(driver):
    SearchTextBoxElement = driver.find_element_by_id('srchword')
    return SearchTextBoxElement

def getSearchButton(driver):
    SearchButton = driver.find_element_by_xpath('//*[@id="queryTop"]/div/div[3]/div/input')
    return SearchButton

def getStockPriceLabel(driver):
    StockPriceLabel = driver.find_element_by_id('ltpid')
    return StockPriceLabel



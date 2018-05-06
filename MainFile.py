from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import PageObjectFunc
import ExcelFuncs

class StockPricesScrapping(object):
    def Main_Scrapping(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(PageObjectFunc.getURL())
        StockList = ExcelFuncs.getStocksList('C:\Users\user\PycharmProjects\WebScrappingStockPrices\ExcelSheet\Target.xlsx')
        CurrentPriceList = list()
        Counter = 1
        for stock in StockList:
            Counter = Counter + 1
            SearchTextBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'srchword')))
            SearchTextBox.send_keys(stock)
            print stock
            SearchButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="queryTop"]/div/div[3]/div/input')))
            SearchButton.click()
            #CurrentPriceList.append(float(PageObjectFunc.getStockPriceLabel(driver).text.replace(",", "")))
            ExcelFuncs.writeStockPrices(float(PageObjectFunc.getStockPriceLabel(driver).text.replace(",", "")),'C:\Users\user\PycharmProjects\WebScrappingStockPrices\ExcelSheet\Target.xlsx',Counter)
            print PageObjectFunc.getStockPriceLabel(driver).text.replace(",", "")
            SearchTextBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'srchword')))
            SearchTextBox.clear()
        driver.close()

if __name__ == "__main__":
    test = StockPricesScrapping()
    test.Main_Scrapping()

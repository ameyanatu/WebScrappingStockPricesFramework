from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from openpyxl import Workbook

import pandas as pd

def getStocksList(FilePath):
    ExcelSheet = pd.read_excel(FilePath,sheet_name='Sheet1')
    StockList = ExcelSheet['Stock Name']
    return StockList

def writeStockPrices(Price, FilePath, Counter):
    WB = load_workbook(FilePath)
    WS = WB.active
    WS['F' + str(Counter)] = Price
    WB.save(FilePath)



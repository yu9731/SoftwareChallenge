# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:16:00 2022

@author: PC
"""

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

def GetHTMLInformation1(url1):         ###提取信息
    try:
        r = requests.get(url1, headers = {'user-agent':'Chorme/10.0'})     
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Fehler!"

def GetHTMLInformation2(url2):
    try:
        r = requests.get(url2, headers = {'user-agent':'Chorme/10.0'})     
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Fehler!"
    
def GetHTMLInformation3(url3):
    try:
        r = requests.get(url3, headers = {'user-agent':'Chorme/10.0'})     
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Fehler!"
    
def GetDMCInformation(html1,ulist1):   
    soup = BeautifulSoup(html1,'html.parser')
    string1 = str(soup.find_all('span',attrs = {'class':'product-price-amount'}))
    price = re.findall(r"\d+.?\d*",string1)
    ulist1.append(price[0])

    string2 = str(soup.find_all('span',attrs = {'class':'stock-green'}))
    delivery = re.findall(r">(.*?)<",string2)
    if delivery == []:
        ulist1.append(0)
    else:
        ulist1.append(1)

    string3 = str(soup.find_all(id="ContentPlaceHolder1_upPanelTemplateValues"))
    material = re.findall(r'Zusammenstellung</td><td>(.*?)<',string3)
    ulist1.append(material[0])

    string4 = str(soup.find_all(id="ContentPlaceHolder1_upPanelTemplateValues"))
    size = re.findall(r'Nadelstärke</td><td>(.*?)<',string4)
    ulist1.append(size[0]) 

def GetDrop1Information(html2,ulist2):
    r = requests.get(url2, headers = {'user-agent':'Chorme/10.0'})     
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text

    soup = BeautifulSoup(html,'html.parser')
    string1 = str(soup.find_all('span',attrs = {'class':'product-price-amount'}))
    price = re.findall(r"\d+.?\d*",string1)
    ulist2.append(price[0])

    string2 = str(soup.find_all('span',attrs = {'class':'stock-green'}))
    delivery = re.findall(r">(.*?)<",string2)
    if delivery == []:
        ulist2.append(0)
    else:
        ulist2.append(1)

    string3 = str(soup.find_all(id="ContentPlaceHolder1_upPanelTemplateValues"))
    material = re.findall(r'Zusammenstellung</td><td>(.*?)<',string3)
    ulist2.append(material[0])

    string4 = str(soup.find_all(id="ContentPlaceHolder1_upPanelTemplateValues"))
    size = re.findall(r'Nadelstärke</td><td>(.*?)<',string4)
    ulist2.append(size[0]) 

def GetDrop2Information(html3,ulist3):
    r = requests.get(url3, headers = {'user-agent':'Chorme/10.0'})     
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text 

    soup = BeautifulSoup(html,'html.parser')
    string1 = str(soup.find_all('span',attrs = {'class':'product-price-amount'}))
    price = re.findall(r"\d+.?\d*",string1)
    ulist3.append(price[0])

    string2 = str(soup.find_all('span',attrs = {'class':'stock-green'}))
    delivery = re.findall(r">(.*?)<",string2)
    if delivery == []:
        ulist3.append(0)
    else:
        ulist3.append(1)

    string3 = str(soup.find_all(id="ContentPlaceHolder1_upPanelTemplateValues"))
    material = re.findall(r'Zusammenstellung</td><td>(.*?)<',string3)
    ulist3.append(material[0])

    string4 = str(soup.find_all(id="ContentPlaceHolder1_upPanelTemplateValues"))
    size = re.findall(r'Nadelstärke</td><td>(.*?)<',string4)
    ulist3.append(size[0])
    
def WriteInFile(ulist1,ulist2,ulist3):
    list1 = ['name','price','delivery','neddle size','composition']
    list2 = [ulist1,ulist2,ulist3]
    df = pd.DataFrame(list2,columns=list1)
    df.to_html('data.html')

if __name__ == '__main__':
    url1 = 'https://www.wollplatz.de/wolle/dmc/dmc-natura-xl'
    url2 = 'https://www.wollplatz.de/wolle/drops/drops-safran'
    url3 = 'https://www.wollplatz.de/wolle/drops/drops-baby-merino-mix'
    html1 = GetHTMLInformation1(url1)
    html2 = GetHTMLInformation2(url2)
    html3 = GetHTMLInformation3(url3)
    ulist1 = ['dmc-natura-xl']
    ulist2 = ['drops-safran']
    ulist3 = ['drops-baby-merino-mix']
    GetDMCInformation(html1,ulist1)
    GetDrop1Information(html2,ulist2)
    GetDrop2Information(html3,ulist3)
    WriteInFile(ulist1,ulist2,ulist3)
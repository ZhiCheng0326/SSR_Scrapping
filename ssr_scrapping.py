# -*- coding: utf-8 -*-
import bs4
import requests

def main():
    url = "https://fangeqiang.com/408.html"
    page = requests.get(url)    
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    
    #extract the ssr address out of the other VPN addresses
    Alladdress = soup.find_all('div',attrs={'class':'xContent'})  
    SSRaddress = Alladdress[3]
    str_SSRaddress = SSRaddress.pre.text               #convert into string format
    
    
    #extract the ssr address
    keyword = 'ssr://'
    index = str_SSRaddress.find(keyword)
    addressList = []
    
    while str_SSRaddress[index] != '\r':
        addressList.append(str_SSRaddress[index])
        index += 1
    
    SSR = "".join(addressList)
    print (SSR)
    
main()
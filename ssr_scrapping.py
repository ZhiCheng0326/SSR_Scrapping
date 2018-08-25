# -*- coding: utf-8 -*-
import bs4
import requests

def getPage():
    url = "https://fangeqiang.com/408.html"
    page = requests.get(url)    
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    return soup


#extract the ssr address out of the other VPN addresses
def getSSRdiv(soup):
    Alladdress = soup.find_all('div',attrs={'class':'xContent'})
    
    for address in Alladdress:
        if 'ssr' in address.text:
            return address.pre.text     #convert into string format
    
    if SSRaddress == None:
        return None

    
#extract the ssr address
def getSSRstring(str_SSRaddress):
    keyword = 'ssr://'
    index = str_SSRaddress.find(keyword)
    addressList = []
    
    while str_SSRaddress[index] != '\r':
        addressList.append(str_SSRaddress[index])
        index += 1
    
    SSR = "".join(addressList)
    return SSR


def main():
    soup = getPage()
    str_SSRaddress = getSSRdiv(soup)
    
    if str_SSRaddress == None:
        print('SSR link not found')
        return
    
    SSR = getSSRstring(str_SSRaddress)
    print(SSR)
    
main()

def main():
    soup = getPage()
    str_SSRaddress = getSSRdiv(soup)
    
    if str_SSRaddress == None:
        print('SSR link not found')
        return
    
    SSR = getSSRstring(str_SSRaddress)
    print(SSR)

if __name__ == "__main__":
    main()

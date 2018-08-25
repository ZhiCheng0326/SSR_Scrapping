def main():
    soup = getPage()
    str_SSRaddress = getSSRdiv(soup)
    
    if str_SSRaddress == None:
        print('SSR link not found')
        return
    
    SSR = getSSRstring(str_SSRaddress)
    config = decoder(SSR)
    updateConfig(config)
 
if __name__ == "__main__":
    from ssr_scrapping import*
    from decoder import decoder
    from update import updateConfig
    main()

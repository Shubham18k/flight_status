from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def res(main):
    #status
    status=main.find('span',class_="oEvMnb")
    if status==None:
        status="-"
    else:
        status=status.text.strip()

    #time
    time=main.find('span',class_="DveFte")
    if time==None:
        time="-"
    else:
        time=time.text

    FT=main.find_all('div',class_="N64Mld")
    if FT==None:
        From="-"
        to="-"
    else:
        From=FT[0].text
        to=FT[1].text

    Terminal=main.find_all('div',class_="KUI09c")
    if Terminal==None:
        Sch_term='-'
        Arv_term='-'
        Gate_sch='-'
        Gate_arv='-'
        Sch_time='-'
        Arv_time='-'
    else:
        Sch_time=Terminal[0].text
        Arv_time=Terminal[3].text
        Sch_term=Terminal[1].text
        Arv_term=Terminal[4].text
        Gate_sch=Terminal[2].text
        Gate_arv=Terminal[5].text

    txt=f'''

Status - {status} 
Duration - {time}
-----------------------
From - {From}
To - {to}
-----------------------
Scheduled departure - {Sch_time}
Departure Terminal - {Sch_term}
Departure Gate - {Gate_sch}
-----------------------
Scheduled Arrival - {Arv_time}
Arrival Terminal - {Arv_term}
Arrival Gate - {Gate_arv}
    '''
    
    return txt

def search(no):
    try:
        url='https://www.google.com/search?q=flight+status+'+no
        options=Options()
        options.headless=True
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        main=soup.find('div',class_='BmP5tf')
        txt=res(main)
        return txt

        
    except Exception as e:
        print(e)
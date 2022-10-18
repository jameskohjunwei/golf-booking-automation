import camelot
import pandas as pd
import time
import os
import requests
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
from selenium import webdriver
from pathlib import Path
from datetime import datetime
import os
import shutil
import smtplib
from email import message
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # added chrome options to run it headless
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PyPDF2 import PdfReader
import pdfplumber
import numpy as np

stored_messsages = []

def download_pdf():

    #server version just uncomment the one with local host and comment out the chromedrivermanager.install() version
    # web = webdriver.Remote('http://localhost:4444/wd/hub', options=webdriver.ChromeOptions())
    chrome_options = Options()
    web = webdriver.Chrome(options=chrome_options)
    # left this website blank intentionally for privacy reasons
    url = web.get("***website***") 
    web.implicitly_wait(20)


    #left the xpath blank intentionally
    push_url = web.find_element('xpath','***xpath***')
    push_url.click()

    time.sleep(8)

    web.switch_to.window(web.window_handles[1])
    download_url = web.current_url

    #download file
    date = datetime.now()
    filename = Path('metadata_{}.pdf'.format(date))
    response = requests.get(download_url)
    file_download = filename.write_bytes(response.content)
    file_download
    
    #give time to download the pdf
    time.sleep(5)
    
    return filename

def clean_data_v2(filename):
    
    loop_range = list(range(15)) 
    filelist = []
    full_filelist = pd.DataFrame()
    
    #import pdf
    table = camelot.read_pdf(str(filename), pages='all')   

    # loop to find all the available tables in all the available pages
    for x in loop_range:
        try:
            table[x].df
            string = str(f'table[{x}].df')
            filelist.append(string)
        except:
            break
    filelist #at this section if you remove the eval below, you can call this var for strings of available tables.

    # to turn the strings table[x].df to variables
    for i, item in enumerate(filelist):
        filelist[i] = eval(item)

    # loop to concat all available tables from pdf
    for z in loop_range:
        try:
            y=z+1
            full_filelist = pd.concat([full_filelist, filelist[z]],axis=0,ignore_index=True)
        except:
            break

    total_table = full_filelist[0].str.split('\n',expand=True)
    total_table[0] = total_table[0].str.replace(' ','')
    total_table[0] = total_table[0].apply(lambda x:str.casefold(x))

    return total_table

def find_membership(filename, total_table, member):   
       
    #find my membership no.
    game = total_table.loc[total_table[0] == member.lower()] # OR [1] to have membership number as well
    find_member = game[0].tolist()


    if member in find_member:

        #extract column information
        game_member = game[0].values[0]
        game_course = game[1].values[0]
        game_day = game[2].values[0]
        game_time = game[3].values[0]
        game_tee = game[4].values[0]

        #print
        stored_value= str(f'\n*****************\nMembership: {game_member}\n{game_course}\n{game_day}\n{game_time}\n{game_tee}\n*****************\n')
        print(stored_value)
        stored_messsages.append(stored_value)
           
    else:
        
        stored_value = str(f'\n{member} no game\n*****************')
        print(stored_value)
        stored_messsages.append(stored_value)

def send_telegram(stored_messages):
    # left this blank intentionally
    base_url = '***telegram bot api***'.format(a=''.join(stored_messages))
    requests.get(base_url)
        
    
filename = download_pdf()
total_table = clean_data_v2(filename)

# find the membership numbers of interest, this can scale according to however many members i do this for
find_membership(filename, total_table,'***membership no***')
find_membership(filename, total_table,'***membership no***')
find_membership(filename, total_table,'***membership no***')
send_telegram(stored_messsages)

#give the pdf some time before you delete
time.sleep(2)

#delete pdf after done
if os.path.exists(filename):
    os.remove(filename) # one file at a time
else:
    print('no file to delete')
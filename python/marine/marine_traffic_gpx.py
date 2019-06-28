from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
import pandas as pd

#os.chdir('./Ship Data')

MSSI_numbers = input ("Enter the Vessel's MSSI number: ")
MSSI_numbers = int(MSSI_numbers)
URL = "https://www.marinetraffic.com/en/ais/details/ships/mmsi:{}".format(MSSI_numbers)

chrome_path = './chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get(URL)
driver.implicitly_wait(2)
#driver.get("https://www.marinetraffic.com/")
#driver.implicitly_wait(8)
#driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[2]/div/div[2]/input').send_keys(MSSI_numbers)
#driver.implicitly_wait(4)
#driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[2]/ul/li/a/div/div[2]/span[2]').click()
#driver.implicitly_wait(6)

try:
    details=driver.find_element_by_xpath('//*[@id="vessel_details_general"]/div/ul').text
    details=details.split('\n')
    details=[dtls.split(':') for dtls in details]

    Vessel_Name=details[1][1]
    Vessel_Name=Vessel_Name.strip()
    print(Vessel_Name)

    position=driver.find_element_by_xpath('//*[@id="tabs-last-pos"]/div/div/div[1]').text
    position=position.split('\n')
    position=[pos.split(':') for pos in position]
    Position_Received=':'.join(position[0][1:3])

    lat_long=position[3][1]
    latitude=lat_long.split("/")[0]
    latitude=latitude[:-2]
    longitude=lat_long.split("/")[1]
    longitude=longitude[:-2]
    print(latitude)
    print(longitude)

    Speed_Course=position[5][1]
    print(Speed_Course)

    d=Position_Received.split(' (')
    d=d[1].replace(' ', '-')
    formated_date=d.replace(':', '')
    print(formated_date)
    Vessel_Name = Vessel_Name.replace(' ', '_')
    print(Vessel_Name)

    data_string = '''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
    <gpx version="1.1" creator="name" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"> 
        <wpt lat="{}" lon="{}">
        <name>{}_{}</name>
        <desc>Speed/Course: {}</desc>
        <sym>Marks-Race-Tetrahedron-Mark1</sym>
        </wpt>
    </gpx>'''.format(latitude, longitude, Vessel_Name, formated_date, Speed_Course)

    file = open("{}_{}.txt".format(Vessel_Name, formated_date), 'w')
    file.write(data_string)
    file.close()

    import glob, os

    for filename in glob.iglob(os.path.join('C:\\Users\\winedoze\\Desktop', '*.txt')):
        os.rename(filename, filename[:-4] + '.gpx')
        
except:
    details=driver.find_element_by_xpath('//*[@id="vessel_details_general"]/div/ul').text
    details=details.split('\n')
    details=[dtls.split(':') for dtls in details]

    Vessel_Name=details[1][1]
    Vessel_Name=Vessel_Name.strip()
    print(Vessel_Name)

    position=driver.find_element_by_xpath('//*[@id="tabs-last-pos"]/div/div/div[1]').text
    position=position.split('\n')
    position=[pos.split(':') for pos in position]
    Position_Received=':'.join(position[0][1:3])

    lat_long=position[3][1]
    latitude=lat_long.split("/")[0]
    latitude=latitude[:-2]
    longitude=lat_long.split("/")[1]
    longitude=longitude[:-2]
    print(latitude)
    print(longitude)

    Speed_Course=position[5][1]
    print(Speed_Course)

    d=Position_Received.split(' (')
    d=d[0].strip()
    d=d.replace(' ', '-')
    formated_date=d.replace(':', '')
    print(formated_date)
    Vessel_Name = Vessel_Name.replace(' ', '_')
    print(Vessel_Name)

    data_string = '''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
    <gpx version="1.1" creator="name" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"> 
        <wpt lat="{}" lon="{}">
        <name>{}_{}</name>
        <desc>Speed/Course: {}</desc>
        <sym>Marks-Race-Tetrahedron-Mark1</sym>
        </wpt>
    </gpx>'''.format(latitude, longitude, Vessel_Name, formated_date, Speed_Course)

    file = open("{}_{}.txt".format(Vessel_Name, formated_date), 'w')
    file.write(data_string)
    file.close()

    import glob, os

    for filename in glob.iglob(os.path.join('C:\\Users\\winedoze\\Desktop', '*.txt')):
        os.rename(filename, filename[:-4] + '.gpx')
from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
import pandas as pd

MSSI_numbers = input ("Enter a number: ")
MSSI_numbers = int(MSSI_numbers)
URL = "https://www.marinetraffic.com/en/ais/details/ships/mmsi:{}".format(MSSI_numbers)

chrome_path = './chromedriver'
driver = webdriver.Chrome(chrome_path)
## I have improved webpage URL so this is no longer needed
#driver.get("https://www.marinetraffic.com/")
driver.get(URL)

## I remove the following lines because they are not needed any more...
#driver.implicitly_wait(8)
#driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[2]/div/div[2]/input').send_keys(MSSI_numbers)
#driver.implicitly_wait(4)
#driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[2]/ul/li/a/div/div[2]/span[2]').click()
#driver.implicitly_wait(6)

details=driver.find_element_by_xpath('//*[@id="vessel_details_general"]/div/ul').text
details=details.split('\n')
details=[dtls.split(':') for dtls in details]
IMO=int(details[0][1])
print(IMO)

Vessel_Name=details[1][1]
Vessel_Name=Vessel_Name.strip()
print(Vessel_Name)

MMSI=int(details[2][1])
print(MMSI)

details_2=driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div[6]/div[1]/div[1]/div').text
details_2=details_2.split('\n')
details_2=[det2.split(':') for det2 in details_2]
Call_Sign=details_2[2][1]
Call_Sign=Call_Sign.strip()
print(Call_Sign)

Flag=details_2[3][1]
Flag=Flag.strip()
print(Flag)

AIS_Vessel_Type=details_2[4][1]
AIS_Vessel_Type=AIS_Vessel_Type.strip()
print(AIS_Vessel_Type)

position=driver.find_element_by_xpath('//*[@id="tabs-last-pos"]/div/div/div[1]').text
position=position.split('\n')
position=[pos.split(':') for pos in position]
Position_Received=[':'.join(position[0][1:3])]
print(Position_Received)

lat_long=position[3][1]
latitude=lat_long.split("/")[0]
longitude=lat_long.split("/")[1]
print(latitude)
print(longitude)

Speed_Course=position[5][1]
print(Speed_Course)

import pandas as pd
dict_1={'Vessel_Name':Vessel_Name, 'IMO':IMO, 'Vessel_Name':Vessel_Name, 'MMSI':MMSI, 'Call_Sign':Call_Sign,
        'Flag':Flag, 'AIS_Vessel_Type':AIS_Vessel_Type, 'Position_Received':Position_Received,
        'latitude':latitude, 'longitude':longitude, 'Speed_Course':Speed_Course}
df=pd.DataFrame(data=dict_1)
print(df)
df.to_excel('C:\\Users\\winedoze\\Desktop\\shipdata.xls', index=False)
from bs4 import BeautifulSoup
import requests
import re

response=requests.get('https://www.flightstats.com/v2/flight-tracker/arrivals/UDR?year=2019&month=6&date=4&hour=6')

soup= BeautifulSoup(response.text,'html.parser')




   #getting the status out of the flight     
flights_status=soup.find_all(class_="text-helper__TextHelper-s8bko4a-0 kWxgTv")
for flight_status in flights_status:
  print(flight_status.get_text())            
            
            
            
            
            
            
            
            
           flight_links=soup.find_all(class_='table__A-s1x7nv9w-2 flrJsE')
           
           for flight_link in flight_links:
               tempLink=flight_link['href']
               
               tempResp=requests.get('https://www.flightstats.com'+tempLink)
               tempSoup=BeautifulSoup(tempResp.text,'html.parser')
               print('https://www.flightstats.com'+tempLink)
               
               str='https://www.flightstats.com'+tempLink
               str=str.replace("tracker","details")
               tempResp2=requests.get(str)
               tempSoup2=BeautifulSoup(tempResp2.text,'html.parser')
               
               
               tail_numbers=tempSoup2.find_all(class_='col-xs-12 col-sm-6 tailNumberBlock')
               
               for tail_number in tail_numbers:
                   Tail_number.append(tail_number.get_text())
                   
               
               
               flights_status=tempSoup.find_all(class_='ticket__StatusContainer-s1rrbl5o-17 fWLIvb')
               for flight_status in flights_status:
                   Flight_status(flight_status.get_text())   
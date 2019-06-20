#Processing the web page using json object


#import statements
import requests
from bs4 import BeautifulSoup
import json
import csv

Hour = ['0', '6', '12', '18']
a='__NEXT_DATA__ = '
b='module'
fly='flights'


flight_number=[]
arrival_time=[]
origin_time=[]
origin=[]
airlines=[]
Flight_Data=[]

for h in Hour:

    

    response = requests.get('https://www.flightstats.com/v2/flight-tracker/arrivals/DEL/?year=2019&month=6&date=8&hour='+h)  
    #getting the input from the web page

    
    #creating an instance of soup from the input data
    soup=BeautifulSoup(response.text,'html.parser')
    
    #seperating the json object out of the complete html
    scripts=soup.find_all('script')
    text=scripts[2].get_text()
    
    jason=(text.split(a))[1].split(b)[0]
    jason=(jason.split(fly))[2].split(',"showCodeshares')[0]
    jason='{"flights'+jason+'}'
    
    #working out with jason and extracting the data
    wjson=json.loads(jason)
    
    
    
  
    
    for i in range(len(wjson['flights'])):
        origin_time.append(wjson['flights'][i]['departureTime']['time24'])
        arrival_time.append(wjson['flights'][i]['arrivalTime']['time24'])
        airlines.append(wjson['flights'][i]['carrier']['name'])
        flight_number.append(wjson['flights'][i]['carrier']['fs'] +' - '+wjson['flights'][i]['carrier']['flightNumber'])
        origin.append(wjson['flights'][i]['airport']['city'])
        

Flight_Data=[[flight_number[i],origin[i],origin_time[i],arrival_time[i],airlines[i]] for i in range(0,len(flight_number))]        

with open('flightsData.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    headers =['Flight Number','Origin of Flight','Origin Time','Arrival Time','Airlines']
    writer.writerow(headers)
    writer.writerows(Flight_Data)

csvFile.close()
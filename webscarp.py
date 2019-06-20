import requests 
from bs4 import BeautifulSoup
from csv import writer
import csv


tail_number=[]
flight_number=[]
arrival_time=[]
origin_time=[]
origin=[]
airlines=[]
Flight_status=[]
Tail_number=[]
flag=0
arrivalCount=0
Hour = ['0', '6', '12', '18']

for h in Hour:

    

    response = requests.get('https://www.flightstats.com/v2/flight-tracker/arrivals/DEL/?year=2019&month=6&date=7&hour='+h)
    
    soup=BeautifulSoup(response.text,'html.parser')
    
    
    
    flights=soup.find_all(class_='table__SubText-s1x7nv9w-16 fRijCQ')
    
    for flight in flights:
    
        if flag==0:
            airlines.append(flight.get_text())
            flag=1
        else:
            origin.append(flight.get_text())
            flag=0
        

            
            
    arrivals=soup.find_all(class_="table__CellText-s1x7nv9w-15 KlAnq")
    
    for arrival in arrivals:
       
        arrivalCount=(arrivalCount+1)%4
        if arrivalCount==1:
           flight_number.append(arrival.get_text())
        if arrivalCount==2:
           origin_time.append(arrival.get_text())
        if arrivalCount==3:
           arrival_time.append(arrival.get_text())
       
      
    flight_links=soup.find_all(class_='table__A-s1x7nv9w-2 flrJsE')
           
    for flight_link in flight_links:
        tempLink=flight_link['href']
               
        tempResp=requests.get('https://www.flightstats.com'+tempLink)
        tempSoup=BeautifulSoup(tempResp.text,'html.parser')
        str='https://www.flightstats.com'+tempLink
        str=str.replace("tracker","details")
        tempResp2=requests.get(str)
        tempSoup2=BeautifulSoup(tempResp2.text,'html.parser')
       
        tail_numbers=tempSoup2.find_all(class_='col-xs-12 col-sm-6 tailNumberBlock')
        for tail_number in tail_numbers:
            Tail_number.append(tail_number.get_text())
        
        flights_status=tempSoup.find_all(class_='ticket__StatusContainer-s1rrbl5o-17 fWLIvb')
        for flight_status in flights_status:
            Flight_status.append(flight_status.get_text())   

   
   
   
   
   
Flight_Data=[[flight_number[i],origin[i],origin_time[i],arrival_time[i],airlines[i],Flight_status[i],Tail_number[i]] for i in range(0,len(flight_number))]






with open('flightsData.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    headers =['Flight Number','Origin of Flight','Origin Time','Arrival Time','Airlines','Flight Status','Tail Number']
    writer.writerow(headers)
    writer.writerows(Flight_Data)

csvFile.close()

import requests  
import datetime
current_time = datetime.datetime.now()
User_location = requests.get('https://ipinfo.io/')
Data = User_location.json()
city = Data['city']
Current_location = Data['loc'].split(',')
lattitude = Current_location[0]
longitude = Current_location[1]

print("City :" ,city)
print("Lattitude :",lattitude)
print("Longitude :", longitude)
print("Date and time is",current_time)


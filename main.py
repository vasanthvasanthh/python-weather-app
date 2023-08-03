import requests
print("---------WEATHER APP-------------")
print("press 1 to get temperature")
print("press 2 to get wind speed")
print("press 3 to get pressure")
print("press 4 to change country")
print("press 0 to exit()")
print("--------------------------------")
api_key = "410e7a22ccc465e98e4bd2b3551413eb"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
cityname = input("Enter city name : ")
metric="metric"
final_url = base_url + "appid=" + api_key + "&q=" + cityname + "&units=" + metric
response = requests.get(final_url)
data = response.json()
y=data["main"]
x=data["wind"]
input1=int(input("Enter your input:"))
while True:
  if(input1==1):
    print(f"  Temperature: {y['temp']}°C")
  elif(input1==2):
    print(f"  Wind speed: {x['speed']}m/s")
  elif(input1==3):
    print(f"  Pressure:   {y['pressure']}hPa")
  elif(input1==0):
    print("   Program terminated")
    quit()
  input1=int(input("Enter your input:"))

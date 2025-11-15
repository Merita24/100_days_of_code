import requests

def fetch_data(url,params=None,headers=None):
  response=requests.get(url,params=params,headers=headers)
  return response.json()

def parse_data(data):
    
    current_time=data['current']['time']
    current_temp=data['current']['temperature_2m']
    wind_speed=data['current']['wind_speed_10m']
    
    return {

        "time":current_time,
        "current_temperature":current_temp,
        "wind-speed":wind_speed
    }




def main():
  url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
  params = {
        "latitude": -1.286389,        
        "longitude": 36.817223,
        "current": "temperature_2m,wind_speed_10m"
    }

  data=fetch_data(url)
  parsed=parse_data(data)

  print("time:", parsed['time'])
  print("temperature:",parsed['current_temperature'])
  print("wind:",parsed['wind-speed'])



main()
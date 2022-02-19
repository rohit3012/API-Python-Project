import requests
from datetime import datetime
# from datetime module we are importing datetime package

# Stp1 is to import requests

My_LAT = -33.868820
MY_LONG = 151.209290
Format = 0
# here we have assigned a optional parameter to 0 to get data in ISO 8601 format

parameters = {
    "lat": My_LAT,
    "lng": MY_LONG,
    "formatted": Format,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# Stp 2 Call the end point using request get and put in response

response.raise_for_status()
# stp3 create a exception request

# stp 6 search your lat and lon on lat-long.com and then Assign lat long to as floating pt number
data = response.json()

# stp4 parse the data with json
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# output without split sunrise - 2022-02-12T19:26:58+00:00 sunset - 2022-02-13T08:51:43+00:00
# explaining split("T")[1].split(":")[0], so where ever I get T spit the rest, t
# cont till how much till 1 array pos, then find: till 0 array pos
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# output with split sunrise 19
# sunset 08

print(sunrise)
print(sunset)

time_now = datetime.now()
# from datetime package we have fetched now() fucntion
print(time_now)
# display the data
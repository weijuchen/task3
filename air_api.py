import requests
from configparser import ConfigParser
import csv

# Config Parse

config = ConfigParser()
config.read("config.ini")
from configparser import ConfigParser

key = config["Environment"]["KEY"]

# url = f"https://data.moenv.gov.tw/api/v2/aqx_p_488?format=json&api_key={key}&filters=SiteName,EQ,土城|datacreationdate,GR,2024-10-01 00:00:00|datacreationdate,LE,2024-10-15 23:00:00"


url = f"https://data.moenv.gov.tw/api/v2/aqx_p_488?format=json&limit=2000&api_key={key}&filters=SiteName,EQ,土城|datacreationdate,GR,2024-10-01 00:00:00|datacreationdate,LE,2024-10-15 23:00:00"


r = requests.get(url)

# print(r.json()["records"])

# use for loop to get two values, datacreationdate and pm2.5_avg
data = {}

def get_pm25():
    for time in r.json()["records"]:
        data[time["datacreationdate"]] = time["pm2.5"]
        # print("here is the data",data)
    pm25 = data
    with open("pm25.csv", "w") as f:
        writer = csv.writer(f)
        for time, value in pm25.items():
            writer.writerow([time, value])


get_pm25()


# print(get_pm25().json())
# print(get_pm25())

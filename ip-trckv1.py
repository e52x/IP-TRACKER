# "CODE BY ERICK"
# "https://github.com/e52x"
# "FACK You KANG RECODE"
import json
from urllib import request
url = "https://ipapi.co/"
ip = input("Masukan IP Target : ")
request = request.urlopen(url + ip + "/json")
data_json = json.loads(request.read() )

print("IP : " + str(data_json['ip']))
print("Negara : " + str(data_json['country_name']))
print("Wilayah : " + str(data_json['region']))
print("Kota : " + str(data_json['city']))
print("Postal Code : " + str(data_json['postal']))
print("Latitude : " + str(data_json['latitude']))
print("Longitude : " + str(data_json['longitude']))
print("ISP : " + str(data_json['org']))

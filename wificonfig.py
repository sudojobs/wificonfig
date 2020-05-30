import json
import requests
import os
#POST api/getWifiDetail
#Accept: application/json
#Content-Type: application/json
#{
#"hardware_id": "202481595041676"
#}
f= open("interfaces","w+")

url = 'http://dapirpi.rozcomapp.com/api/getWifiDetail'
object = {'hardware_id': '202481595041676'}
filepath='/etc/network/interfaces'
interface = 'wlan0'
output = requests.post(url, data = object)
values = output.json()
ssid=values['wifi_id']
password=values['wifi_password']
os.system('iwconfig ' + interface + ' essid ' + name + ' key ' + password)
#f.write("auto wlan0\n")
#f.write("iface wlan0 inet dhcp\n")
#f.write("wpa-ssid %s\n" % ssid)
#f.write("wpa-psk %s\n" % password)
#copy the interface file to default
#os.system('cp interfaces /etc/network/interfaces') 
#reboot network
#os.system('sudo wpa_cli -i wlan0 reconfigure')
#os.system('sudo ifdown --force wlan0')
#os.system('sudo ifup wlan0')
#os.system('sudo systemctl daemon-reload')
#if required WIFI Country

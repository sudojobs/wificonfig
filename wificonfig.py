import json
import requests
import os
import subprocess 

#ssid="MickeyMouse" passkey="MinnieMouse" 

#POST api/getWifiDetail
#Accept: application/json
#Content-Type: application/json
#{
#"hardware_id": "202481595041676"
#}

url = 'http://dapirpi.rozcomapp.com/api/getWifiDetail'
object = {'hardware_id': '202481595041676'}
filepath='/etc/network/interfaces'
interface = 'wlan0'
output = requests.post(url, data = object)
values = output.json()
ssid=values['wifi_id']
passkey=values['wifi_password']
p1 = subprocess.Popen(["wpa_passphrase", ssid, passkey], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["sudo","tee","-a","/etc/wpa_supplicant/wpa_supplicant.conf",">","/dev/null"], stdin=p1.stdout, stdout=subprocess.PIPE) 
p1.stdout.close() # Give p1 a SIGPIPE if p2 dies. 
output,err = p2.communicate()
#os.system('iwconfig ' + interface + ' essid ' + ssid + ' key ' + password)
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
#/etc/wpa_supplicant/wpa_supplicant.conf and make below entries in it.
#ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
#update_config=1
#country=YOUR COUNTRY CODE HERE 

# wificonfig

This script fetch the wifi details from Post 
Configure ssid and password on raspberry pi

import subprocess
ssid="MickeyMouse"
passkey="MinnieMouse"
p1 = subprocess.Popen(["wpa_passphrase", ssid, passkey], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["sudo","tee","-a","/etc/wpa_supplicant/wpa_supplicant.conf",">","/dev/null"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Give p1 a SIGPIPE if p2 dies.
output,err = p2.communicate()

import network
import socket
import select
import json
import time
import config

ssid = config.SSID
password = config.PASSWD

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

try:
    ip = connect()
    addr_info = socket.getaddrinfo(ip, 50222)
    addr = addr_info[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    
    while True:
        time.sleep(0.01)
        data, addr=s.recvfrom(1024)
        print(data)
        d = json.loads(data)
        print(d)
        
              
except KeyboardInterrupt:
    machine.reset()

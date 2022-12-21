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
    
        d = json.loads(data)
    
        
        if d['type'] == "obs_st":
            
            print("Time Epoch: " + str(d['obs'][0][0]) + " seconds")
            print("Wind Lull m/s: " + str(d['obs'][0][1]) + " m/s")
            print("Wind Avg m/s: " + str(d['obs'][0][2]) + " m/s")
            print("Wind Gust m/s: " + str(d['obs'][0][3]) + " m/s")
            print("Wind Direction: " + str(d['obs'][0][4]) + " degrees")
            print("Wind Sample Interval: " + str(d['obs'][0][5]) + " seconds")
            print("Station Pressure: " + str(d['obs'][0][6]) + " mb")
            print("Air Temperature: " + str(d['obs'][0][7]) + " C")
            print("Relative Humidity: " + str(d['obs'][0][8]) + "%")
            print("Illuminance: " + str(d['obs'][0][9]) + " lux")
            print("UV Index: " + str(d['obs'][0][10]))
            print("Solar Radiation: " + str(d['obs'][0][11]) + " W/m^2")
            print("Rain amount previous minute: " + str(d['obs'][0][12]) + " mm")
            print("Precipitation type: " + str(d['obs'][0][13]) + " 0=none,1=rain,2=hail,3=rain+hail experimental")
            print("Lightning Strike Avg Dist: " + str(d['obs'][0][14]) + " km")
            print("Lightning Strike Count: " + str(d['obs'][0][15]))
            print("Battery: "  + str(d['obs'][0][16]) + " volts")
            print("Report Interval: " + str(d['obs'][0][17]) + " minutes")
            print()
        
            
            
              
except KeyboardInterrupt:
    machine.reset()

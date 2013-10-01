#!/usr/bin/env python
import time
import serial
import requests

sio = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(3)

last = ''

while 1:
  r = requests.get('http://sign.willmason.me/message.txt')
  if r.status_code == 200 and last != r.text:
    sio.write(r.text)
    last = r.text
  time.sleep(1)  

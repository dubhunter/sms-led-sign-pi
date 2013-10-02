#!/usr/bin/env python
from time import sleep
import serial
import requests

sio = serial.Serial('/dev/ttyACM0', 9600)

sleep(3)

last = ''

while 1:
    try:
        r = requests.get('http://sign.willmason.me/message.txt')
        if r.status_code == 200 and last != r.text:
            sio.write(r.text)
            last = r.text
    except Exception:
        pass
    sleep(1)

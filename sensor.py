import time
import RPi.GPIO as gpio    
import Adafruit_DHT as Ada

PIN_AM2302 = 23

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(PIN_AM2302, gpio.IN, pull_up_down=gpio.PUD_OFF)

while True:
    hum, temp = Ada.read_retry(Ada.AM2302, PIN_AM2302)    
    print("T={0:4.1f}°C, RH={1:4.1f}%".format(temp, hum))
    time.sleep(1)
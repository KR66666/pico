import machine
import dht
import time

sensor = dht.DHT11(machine.Pin(1))
led1 = machine.Pin(2, machine.Pin.OUT)
led2 = machine.Pin(3, machine.Pin.OUT)
led3 = machine.Pin(4, machine.Pin.OUT)
led4 = machine.Pin(5, machine.Pin.OUT)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
while True:
    sensor.measure()
    teplota = sensor.temperature()
    print("Temperature:", teplota , "°C")
    print("Humidity:", sensor.humidity(), "%")
    if teplota < 20:
       
       led1.value(1)
       time.sleep(0.5)
       led1.value(0)

    elif teplota < 22:
        led2.value(1)
        time.sleep(0.5)
        led2.value(0)
    
    elif teplota < 24:
        led3.value(1)
        time.sleep(0.5)
        led3.value(0)

    elif teplota < 26:
        led4.value(1)
        time.sleep(0.5)
        led4.value(0)



  

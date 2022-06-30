from time import sleep
import paho.mqtt.client as mqtt
import random

broker_address="192.168.1.89" 

client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker

while True:
    i = random.randrange(15, 20)
    print(i)
    client.publish("esp/ds18b20/temperature",i)#publish

    sleep(1)
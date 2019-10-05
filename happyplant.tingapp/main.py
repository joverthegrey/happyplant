import paho.mqtt.client as mqtt
import tingbot
from tingbot import *

# setup code here
message = 'waiting'
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    global message
    message = 'connected'
    client.subscribe("plants/#")

def on_message(client, userdata, msg):
    global message
    message = msg.topic + ' ' + str(msg.payload)

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_start()

@every(seconds=1.0/30)
def loop():
    # drawing code here
    screen.fill(color='black')
    screen.text(message)

tingbot.run()
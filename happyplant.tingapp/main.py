import paho.mqtt.client as mqtt
import tingbot
from tingbot import *

# setup code here
message = 'waiting'
client = mqtt.Client()
plant_state = 0
plant_image = 'sad.png'

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

@every(seconds=10.0)
def image():
    global plant_state
    global plant_image
    if plant_state == 0:
        plant_image = 'sad.png'
        plant_state = 1
    elif plant_state == 1:
        plant_image = 'neutral.png'
        plant_state = 2
    else:
        plant_image = 'happy.png'
        plant_state = 0

@every(seconds=1.0/30)
def loop():
    # drawing code here
    # background
    screen.fill(color='green')
    
    # topbar
    screen.rectangle(xy=(0,0), size=(320,20), color='olive', align='topleft')
    screen.line(start_xy=(0,21), end_xy=(320,21), color='black', width=2)
    
    # message window
    screen.rectangle(xy=(157,37), size=(145,185), color='black', align='topleft')
    screen.rectangle(xy=(155,35), size=(145,185), color='olive', align='topleft')
    
    # plant state image
    screen.image(plant_image, xy=(0,20), align='topleft')
    screen.text(message)

tingbot.run()

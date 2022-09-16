from datetime import datetime
from sound_playback_helper.sound_player import SoundPlayer
import paho.mqtt.client as mqtt

player = SoundPlayer('sounds/')

def on_message_received(client, userdata, message):
    message_text = message.payload.decode('utf-8')
    print('Received message ' + message_text + ' from topic ' + str(message.topic) + '.')
    if message_text == 'detected':
        print('Motion detected, playing sound...')
        player.play(player.list_sounds()[0])
    else:
        print('No motion detected')

def setup_client(brokerAddress):
    client = mqtt.Client()
    client.connect(brokerAddress)
    client.subscribe('porch/doorbell/movement/status')
    client.on_message = on_message_received
    return client

if (__name__ == "__main__"):
    mqttBroker = '192.168.1.100'
    client = setup_client(mqttBroker)
    client.loop_forever()

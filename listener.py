import os
from datetime import datetime
from sound_playback_helper.sound_player import SoundPlayer
import paho.mqtt.client as mqtt

mqtt_broker_address = os.environ['MQTT_BROKER_ADDR']
trigger_topic = os.environ['FRANKENSTEINS_DOORBELL_TRIGGER_TOPIC']
sound_file_dir = 'sounds/'
player = SoundPlayer(sound_file_dir)

def on_message_received(client, userdata, message):
    message_text = message.payload.decode('utf-8')
    print('Received message ' + message_text + ' from topic ' + str(message.topic) + '.')
    if message_text == 'on':
        print('Motion detected, playing sound...')
        player.play(player.list_sounds()[0])
    else:
        print('No motion detected')

def setup_client():
    client = mqtt.Client()
    client.connect(mqtt_broker_address)
    client.subscribe(trigger_topic)
    client.on_message = on_message_received
    return client

if (__name__ == "__main__"):
    client = setup_client()
    client.loop_forever()

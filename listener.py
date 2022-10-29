import os
import time
from sound_playback_helper.sound_player import SoundPlayer
import paho.mqtt.client as mqtt

mqtt_broker_address = os.environ['MQTT_BROKER_ADDR']
trigger_topic = os.environ['F_DB_TRIGGER_TOPIC']
main_sound_name = os.environ['F_DB_MAIN_SOUND_NAME']
heartbeat_sound_name = os.environ['F_DB_HEARTBEAT_SOUND_NAME']
old_time = time.time()
sound_file_dir = 'sounds/'
player = SoundPlayer(sound_file_dir)

def on_message_received(client, userdata, message):
    message_text = message.payload.decode('utf-8')
    print('Received message ' + message_text + ' from topic ' + str(message.topic) + '.')
    if message_text == 'on':
        print('Motion detected, playing sound...')
        player.play(main_sound_name)
        old_time = time.time()
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
    while True:
        curTime = time.time();
        if curTime - old_time > 60:
            player.play(heartbeat_sound_name)
            old_time = curTime
        client.loop(30);

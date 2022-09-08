from ast import If
import paho.mqtt.client as mqtt
import time

def publish_message(client, topic, message):
    client.publish(topic, message)
    print("Published " + message + " to topic " + topic + ".")
    time.sleep(1)

def on_message_received(client, userdata, message):
    print('Received message ' + str(message.payload) + ' from topic ' + str(message.topic) + '.')
    if message.payload == 'detected':
        print('Motion detected, playing sound...')
    else:
        print('No motion detected')

def setup_client(brokerAddress):
    client = mqtt.Client()
    client.connect(brokerAddress)
    client.subscribe('porch/dorbell/movement/status')
    client.on_message = on_message_received
    return client

if (__name__ == "__main__"):
    mqttBroker = '192.168.1.100'
    heartbeatTopic = 'porch/frankensteinsdoorbell/heartbeat'
    client = setup_client(mqttBroker)
    while True:
        publish_message(client, heartbeatTopic, str(time.localtime))
        time.sleep(10)

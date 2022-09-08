import paho.mqtt.client as mqtt
import time

def publish_message(client, message):
    client.publish("test_topic", message)
    print("Published " + message + " to topic 'TEST_TOPIC'")
    time.sleep(1)

if (__name__ == "__main__"):
    mqttBroker = '192.168.1.100'
    client = mqtt.Client()
    client.connect(mqttBroker)

    message = input('Enter message: ')
    publish_message(client, message)

import smbus2
import paho.mqtt.client as mqtt

I2C_ADDR = 0x08  # Arduino Nano  I2C 
bus = smbus2.SMBus(1)  # Raspberry Pi I2C-1 

# MQTT 
MQTT_BROKER = "192.168.1.205"  
MQTT_PORT = 1883 
MQTT_TOPIC = "buzzer/ON"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode().strip()
    print(f"Received message: {payload}")
    if msg.topic == MQTT_TOPIC and payload == "ON":
        try:
            bus.write_byte(I2C_ADDR, ord('O'))  #  ASCII 'O'  Arduino
            print("Sent 'O' to Arduino via I2C")
        except Exception as e:
            print(f"Failed to send I2C message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)  
    client.loop_forever()  
except Exception as e:
    print(f"MQTT connection error: {e}")

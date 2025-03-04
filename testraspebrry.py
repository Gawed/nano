import smbus2
import paho.mqtt.client as mqtt

I2C_ADDR = 0x08  # Arduino 的 I2C 地址
bus = smbus2.SMBus(1)  # Raspberry Pi 默认使用 I2C-1

def on_message(client, userdata, msg):
    if msg.topic == "buzzer/ON" and msg.payload.decode() == "O":
        bus.write_byte(I2C_ADDR, ord('O'))  # 发送 ASCII 'O' 给 Arduino
        print("Sent 'O' to Arduino via I2C")

client = mqtt.Client()
client.on_message = on_message

client.connect("mqtt_broker_address", 1883, 60)  # 修改 MQTT 服务器地址
client.subscribe("buzzer/ON")

client.loop_forever()

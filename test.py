import paho.mqtt.client as mqtt
import serial
import time

# MQTT 配置
MQTT_BROKER = "192.168.1.205"  # 如果你的 MQTT Broker 在树莓派上，使用 "localhost"
MQTT_TOPIC = "buzzer"
MQTT_PORT = 1883

# 串口配置
SERIAL_PORT = '/dev/ttyUSB0'  # 根据树莓派与 Arduino 连接的串口端口修改
BAUD_RATE = 9600

# 初始化串口
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# MQTT 回调函数
def on_message(client, userdata, message):
    # 处理接收到的消息
    msg = message.payload.decode()
    if msg == "ON":
        # 向 Arduino 发送命令
        ser.write(b"ON")  # 向 Arduino 发送 'ON' 命令

# 配置 MQTT 客户端
client = mqtt.Client()
client.on_message = on_message

# 连接到 MQTT Broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# 订阅主题
client.subscribe(MQTT_TOPIC)

# 开始 MQTT 客户端循环
client.loop_start()

# 保持程序运行
while True:
    time.sleep(1)

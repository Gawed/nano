import smbus
bus = smbus.SMBus(1)
address = 0x08  # 确保与Arduino代码中的地址一致

try:
    bus.write_byte(address, 0x00)  # 发送1字节数据
    print("Write succeeded")
except Exception as e:
    print("Error:", e)  # 捕获超时或无应答错误

import smbus
bus = smbus.SMBus(1)

# 方案1：使用7位地址（需库支持）
address_7bit = 0x04
try:
    bus.write_byte(address_7bit, 0x00)  # smbus可能自动左移为8位地址
    print("Success (7-bit)")
except Exception as e:
    print("Error:", e)

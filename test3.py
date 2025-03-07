
import smbus
bus = smbus.SMBus(1)

# 方案2：直接使用8位写地址（0x04 << 1 = 0x08）
address_8bit_write = 0x08
try:
    bus.write_byte(address_8bit_write, 0x00)
    print("Success (8-bit write)")
except Exception as e:
    print("Error:", e)

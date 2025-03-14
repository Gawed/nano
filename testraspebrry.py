if msg.topic == MQTT_TOPIC and payload == "ON"
  try：
  bus.write_byte(I2C_ADDR, ord('O'))
  print("envoye 'O' ver Arduino via i2c")

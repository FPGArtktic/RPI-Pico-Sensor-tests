# Mateusz Okulanis
# FPGArtktic@outlook.com

from machine import Pin, I2C
from micropython import const
# PIN 17 - GP17
# PIN 16 - GP16
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=100000)                         

sensor_addr = i2c.scan()
print("Sens address ", sensor_addr)

_ADDR_MPU6500_PWR_MGMT_1 = 0x6B
_ADDR_MPU6500_SAMPLE_DIV = 0x19
_ADDR_MPU6500_CONFIG = 0x1A
_ADDR_MPU6500_GYRO_CONFIG = 0x1B
_ADDR_MPU6500_ACCEL_CONFIG1 = 0x1C

_VAL_MPU6500_PWR_MGMT_1 = b'\x01' 
_VAL_MPU6500_SAMPLE_DIV = b'\x07' 
_VAL_MPU6500_CONFIG = b'\x06' 
_VAL_MPU6500_GYRO_CONFIG = b'\x10' 
_VAL_MPU6500_ACCEL_CONFIG1 = b'\x01' 

i2c.readfrom_mem(sensor_addr[0], 0x3b, 16)

i2c.writeto_mem(sensor_addr[0], _ADDR_MPU6500_PWR_MGMT_1,_VAL_MPU6500_PWR_MGMT_1)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_PWR_MGMT_1, 1)
i2c.writeto_mem(sensor_addr[0], _ADDR_MPU6500_SAMPLE_DIV,_VAL_MPU6500_SAMPLE_DIV)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_SAMPLE_DIV, 1)
i2c.writeto_mem(sensor_addr[0], _ADDR_MPU6500_CONFIG,_VAL_MPU6500_CONFIG)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_CONFIG, 1)
i2c.writeto_mem(sensor_addr[0], _ADDR_MPU6500_GYRO_CONFIG,_VAL_MPU6500_GYRO_CONFIG)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_GYRO_CONFIG, 1)
i2c.writeto_mem(sensor_addr[0], _ADDR_MPU6500_ACCEL_CONFIG1,_VAL_MPU6500_ACCEL_CONFIG1)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_ACCEL_CONFIG1, 1)

i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_PWR_MGMT_1, 1)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_SAMPLE_DIV, 1)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_CONFIG, 1)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_GYRO_CONFIG, 1)
i2c.readfrom_mem(sensor_addr[0], _ADDR_MPU6500_ACCEL_CONFIG1, 1)

i2c.readfrom_mem(sensor_addr[0], 0x3b, 16)

# TODO DECODE
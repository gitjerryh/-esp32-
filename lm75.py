from machine import I2C,Pin  
import lm75a  
import time  
import ssd1306  
# lm75a I2C地址0x49  
address = 0x4e
# 创建I2C对象LM75A  
i2c = I2C(1, scl=Pin(12), sda=Pin(13), freq=400000)  
# 创建lm75a  
lm = lm75a.LM75A(i2c, address)  
  
def main():  
    # 显示I2C扫描的地址和数量  
    print("i2c addr: 0x%x num: %d" % (i2c.scan()[0], len(i2c.scan())))  
  
    while True:  
        # 显示温度值（现在只在shell中打印）  
        print("temp: %.2f℃" % lm.temp())  
        time.sleep(1)  # 可以根据需要调整时间间隔  
  
if __name__ == "__main__":  
    main()

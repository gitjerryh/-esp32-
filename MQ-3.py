from machine import Pin, ADC, PWM, SoftI2C  
import time  
from ssd1306 import SSD1306_I2C   

# 初始化OLED屏幕  
i2c = SoftI2C(sda=Pin(22), scl=Pin(21))    
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)    
  
# 假设 MQ-3 连接到 ADC1 的 GPIO4    
MQ3_PIN = 4    
# 假设舵机连接到 PWM 通道的 GPIO2    
SERVO_PIN = 2    
    
# 设定酒精浓度的阈值    
ALCOHOL_THRESHOLD = 4094  # 替换为你设定的阈值    
    
# 初始化 ADC    
adc = ADC(Pin(MQ3_PIN))    
adc.atten(ADC.ATTN_11DB)    
adc.width(ADC.WIDTH_12BIT)    
    
# 初始化 PWM    
servo = PWM(Pin(SERVO_PIN), freq=50)    
    
# 舵机角度到PWM duty值的映射    
def set_servo_angle(angle):    
    if angle == 0:    
        servo.duty_u16(1638)  # 0度    
    elif angle == 90:    
        servo.duty_u16(4915)  # 90度    
    elif angle == 180:    
        servo.duty_u16(8192)  # 180度    
    
# 读取MQ-3并控制舵机，同时在OLED屏幕上显示信息  
def read_mq3_and_control_servo():    
    # 读取50次ADC值并求平均值    
    sum_values = 0    
    for i in range(50):    
        sum_values += adc.read()    
    average_value = sum_values / 50    
  
    # 清除OLED屏幕上的内容  
    oled.fill(0)  
      
    # 在OLED屏幕上显示MQ-3的值  
    oled.text("MQ-3 Value: " + str(average_value), 0, 0)  
  
    # 假设我们设定当酒精浓度超过阈值时，舵机转动到180°  
    if average_value > ALCOHOL_THRESHOLD:    
        set_servo_angle(180)  # 转动舵机到 180°  
        oled.text("Drunk driving", 0, 16)  # 在OLED屏幕上显示警告信息  
    else:    
        set_servo_angle(0)  # 返回舵机到 0°  
        oled.text("Drive safely", 0, 16)  # 在OLED屏幕上显示正常信息  
  
    # 显示OLED屏幕上的内容  
    oled.show()  
  
# 主循环，持续读取并处理 MQ-3 的值    
while True:    
    read_mq3_and_control_servo()    
    time.sleep(1)  # 每秒读取一次

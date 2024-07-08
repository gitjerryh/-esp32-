import time
 
class HCSRX(object):
    
    def __init__(self,trig,echo):
        
        self.trig = trig
        self.echo = echo
     #mode 模式选择mode = 0：声速 mode = 1：厘米 
    def Gethcsr(self,mode):
        
        #触发信号
        self.trig.value(0)
        time.sleep_us(2)
        
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        
        #检测回响信号
        number = 0
        while self.echo.value() == 0:
            pass
            high = time.ticks_us()
        
        while self.echo.value() == 1:
            pass
            low  = time.ticks_us()
        
        if mode:
            number = (low - high) / 58  # cm
        else:
            number = ((low - high) * 0.0340)/2  # 声速340/10000=0.0340
        
        time.sleep(0.1)#两次测量时间要间隔50ms以上
        if number > 400:number = 0
        
        return number

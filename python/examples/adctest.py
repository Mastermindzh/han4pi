import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
# lees SPI data uit de adc
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout

while True:
    value0= readadc(0) #lees poort AC0
    value1= readadc(1) #lees poort AC1
    value2= readadc(2) #lees poort AC2
    value3= readadc(3) #lees poort AC3
    #print alle values
    print "Value0 = %s  | Value1 = %s  | Value2 = %s  | Value3 = %s" %(value0,value1,value2,value3)
    #wacht een halve seconde tussen meetingen
    time.sleep(0.5)

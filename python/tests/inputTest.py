# This test code shows the values of the MCP3008 inputs (converted to 0..3.3V) 
#
# J.A. Korten 2017
# Based on http://www.thepicharmer.net/2015/02/mcp3008-with-10k-pot-on-raspberry-pi.html
# 
 
import spidev
import time

ch0 = 0
ch1 = 1
ch2 = 2
ch3 = 3

spi=spidev.SpiDev()
spi.open(0,0)

while True:
      resp0=spi.xfer([1, (8+ch0)<<4,0]) # 0<=channel<=7
      resp1=spi.xfer([1, (8+ch1)<<4,0]) # 0<=channel<=7
      resp2=spi.xfer([1, (8+ch2)<<4,0]) # 0<=channel<=7
      resp3=spi.xfer([1, (8+ch3)<<4,0]) # 0<=channel<=7

      # resp=spi.xfer([1,128,0])
      if 0<= resp0[1]<=3:
          v1=((resp0[1]*256)+resp0[2])* 0.0032
      if 0<= resp1[1]<=3:
          v2=((resp1[1]*256)+resp1[2])* 0.0032
      if 0<= resp2[1]<=3:
          v3=((resp2[1]*256)+resp0[2])* 0.0032
      if 0<= resp3[1]<=3:
          v4=((resp3[1]*256)+resp1[2])* 0.0032
      print v1, " V | ", v2, "V | ", v3, "V  | ", v4, "V"
      

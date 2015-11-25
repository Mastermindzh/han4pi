import spidev
import time
import os

# Debug print meer testgegevens
DEBUG = 1

# Open spi op poort...
spi=spidev.SpiDev()
spi.open(0,0)


# Pin nummer van de POT 
potpin = 0;
last_read =0;
tolerance = 5;

# Methode om pot mee te lezen
def readadc(adcnum):
	if((adcnum > 7) or (adcnum < 0)):
		return -1
	r = spi.xfer2([1,(8+adcnum)<<4,0])
	adcout = ((r[1]&3)<< 8) +r[2]
	return adcout

# Lees pot uit
while True:
	trim_pot_changed = False
	trim_pot = readadc(potpin)
	pot_adjust = abs(trim_pot - last_read)
	
	if DEBUG:
		print "Trim pot = ", trim_pot
		print "Pot adjust = ", pot_adjust
		print "Last read = ", last_read
	
	if(pot_adjust > tolerance):
		trim_pot_changed = True

	if DEBUG:
		print "Did pot change? ", trim_pot_changed

	if(trim_pot_changed):
		print "Trim pot", trim_pot		

	last_read = trim_pot
	time.sleep(0.5)

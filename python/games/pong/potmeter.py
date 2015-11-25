import spidev
import time
import os
import sys

class PotMeter():
	def __init__(potmeter, spelernummer, spelergrootte, schermhoogte):
		potmeter.potmeternummer=spelernummer
		potmeter.vorigewaarde=1023/2
		potmeter.spelergrootte=spelergrootte
		potmeter.schermhoogte=schermhoogte
		
	def waardePot(potmeter):
		return potmeter.readadc(potmeter.potmeternummer)
		
	def veranderingPot(potmeter):
		potmeterWaarde = potmeter.waardePot()
		veranderingPot= potmeterWaarde-potmeter.vorigewaarde
		potmeter.vorigewaarde= potmeterWaarde
		return veranderingPot
		
	def positieVerandering(potmeter):
		return potmeter.veranderingPot()/1023.00*(potmeter.schermhoogte-potmeter.spelergrootte)
		
	# Methode om potentiometer mee te lezen
	def readadc(potmeter, adcnum):
		if((adcnum > 7) or (adcnum < 0)):
			return -1
		r = spi.xfer2([1,(8+adcnum)<<4,0])
		adcout = ((r[1]&3)<< 8) +r[2]
		return adcout

if __name__ == '__main__':
	sys.stderr.write("Doe me niks aan! Ik ben maar een simpele potentiometer. Je kunt veel beter pong.py draaien man.")
	sys.exit()

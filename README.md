![han4pi header](http://i.imgur.com/t5m5nSy.png)

Han4pi is een groep enthusiaste studenten die samen met 1 leraar (Johan Korten) workshops organiseren met de Raspberry pi microcomputer. Dit doen zij voor de Hogeschool van Arnhem en Nijmegen.

Gebruik een van de volgende links om door dit document te bladeren:

- [De installatie van het han4pi pakket](#user-content-install)
- [Raspbian installeren](#user-content-raspbian-install)
	- [Raspbian installatie op Linux](#user-content-linux-raspbian-install)
	- [Raspbian installatie op Windows](#user-content-windows-raspbian-install)


**Organisatie:**
- Simon Baars
- Johan Korten
- Rick van Lieshout
- Ron nabuurs
- Thomas Nobel

<div id = "install"></div>
## De installatie van het han4pi pakket
Voordat u het han4pi pakket kunt installeren zult u een sd kaartje moeten voorbereiden met de "RASPBIAN" software. U kunt de laatste versie van RASPBIAN downloaden op [deze](https://www.raspberrypi.org/downloads/raspbian/) website. Tevens is er een internetverbinding nodig voor de installatie.

1. Stel het root account in door de volgende commando's in de terminal te geven: <br />`sudo passwd root`<br /> En vervolgens tweemaal een root wachtwoord in te geven.

2. Klik linksboven in de hoek op "Menu" en kies voor "Shutdown". Uit het menu wat opspringt kiest u "Logout"

3. Log vervolgens in met de root account en open een terminal.

4. Geef vervolgens het volgende commando in: <br />`git clone https://github.com/Mastermindzh/han4pi.git`<br />

5. Open vervolgens het bestand "install.sh" met een teksteditor. Dit kan in de terminal bijv. met het commando: <br />`nano han4pi/install.sh`<br /> Na het wijzigen van de variabelen drukt u op ctrl + x en vervolgens op y gevolgd door enter om het bestand op te slaan.

6. Pas de variabelen onder het kopje **#Gebruikers variabelen** aan zoals u wilt.
7. Daarna kunt u de installatie starten door het volgende commando te geven:<br />`bash han4pi/install.sh`

8. Volg de instructies op het scherm.
9. Herstart de raspberry pi met het `reboot` commando.

<div id = "raspbian-install"></div>
##Raspbian installeren

Om Raspbian te installeren heeft u een image nodig van het Raspbian OS. Om de laatste versie te downloaden klikt u [hier.](http://downloads.raspberrypi.org/raspbian_latest)


<div id = "linux-raspbian-install"></div>
#####Met een Linux host

<div id = "windows-raspbian-install"></div>
#####Met een Windows host


![han4pi header](http://i.imgur.com/t5m5nSy.png)

Han4pi is een groep enthousiaste studenten die samen met 1 leraar (Johan Korten) workshops organiseren met de Raspberry Pi microcomputer. Dit doen zij voor de Hogeschool van Arnhem en Nijmegen.

Gebruik een van de volgende links om door dit document te bladeren:

- [De installatie van het han4pi pakket](#user-content-install)
- [Raspbian installeren](#user-content-raspbian-install)
	- [Vervolginstructie voor Linux](#user-content-linux-raspbian-install)
	- [Vervolginstructie voor Windows](#user-content-windows-raspbian-install)
	- [Vervolginstructie voor Mac OS](#user-content-mac-raspbian-install)


**Organisatie:**

Voor eventuele vragen zijn alle projectleden laagdrempelig te mailen. U krijgt dan zo spoedig mogelijk reactie op uw vraag. Hieronder volgt een lijst met alle projectleden:

- Simon Baars -- simon.mailadres@gmail.com
- Johan Korten -- Johan.Korten@han.nl
- Rick van Lieshout -- Rick@mi-soft.nl
- Ron nabuurs -- nabuurs.ron@gmail.com
- Thomas Nobel -- thomas_nobel_2@hotmail.com

<div id = "install"></div>
## De installatie van het han4pi pakket
Voordat u het han4pi pakket kunt installeren zult u een sd kaartje moeten voorbereiden met de "RASPBIAN" software. U kunt de laatste versie van RASPBIAN downloaden op [deze](https://www.raspberrypi.org/downloads/raspbian/) website. Tevens is er een internetverbinding nodig voor de installatie.

1. Stel het root account in door de volgende commando's in de terminal te geven: <br />`sudo passwd root`<br /> En vervolgens tweemaal een root wachtwoord in te geven.

2. Klik linksboven in de hoek op "Menu" en kies voor "Shutdown". Uit het menu wat opspringt kiest u "Logout"

3. Log vervolgens in met de root account en open een terminal.

4. Geef vervolgens het volgende commando in: <br />`git clone https://github.com/Mastermindzh/han4pi.git`<br />

5. Open vervolgens het bestand "install.sh" met een teksteditor. Dit kan in de terminal bijv. met het commando: <br />`nano han4pi/install.sh`<br /> 

6. Pas de variabelen onder het kopje **#Gebruikers variabelen** aan zoals u wilt. Na het wijzigen van de variabelen drukt u op ctrl + x en vervolgens op y gevolgd door enter om het bestand op te slaan.

7. Daarna kunt u de installatie starten door het volgende commando te geven:<br />`bash han4pi/install.sh`

8. Volg de instructies op het scherm.
9. Herstart de raspberry pi met het `reboot` commando.

<div id = "raspbian-install"></div>
##Raspbian installeren

Om Raspbian te installeren heeft u een image nodig van het Raspbian OS. Om de laatste versie te downloaden klikt u [hier.](http://downloads.raspberrypi.org/raspbian_latest) Pak de zip uit door er met de rechtermuisknop op te drukken en te kiezen voor "uitpakken" of een dergelijke optie.

Als u het .zip bestand heeft uitgepakt kunt u hieronder verdergaan met de installatieinstructies die bij uw systeem passen.

<div id = "linux-raspbian-install"></div>
###Vervolginstructie voor Linux
Als eerste stap gaan we het pad naar het sd kaartje waar we Raspbian op installeren zoeken. Dit kunnen we doen door het volgende commando in de terminal in te geven:<br />`lsblk`<br />

U krijgt dan een venster met een aantal gegevens (onderstaande afbeelding). De belangrijkste gegevens hier zijn de "NAME" en "SIZE". Meestal is de "SIZE" kolom genoeg om uw sd kaartje te vinden. Dit omdat andere block apparaten (zoals een hdd) vaak veel groter zijn. Kunt u echter niet door alleen de kolom "SIZE" te gebruiken achterhalen welke regel uw sd kaartje betreft dan kunt u simpelweg de sd kaart eruit halen en dan het commando intypen. Vervolgens stopt u de sd kaart terug en voert u het commando nog eens uit. De verandering in het tweede resultaat is dan uw sd kaartje. Op de afbeelding hieronder is te zien dat mijn sd kaart op plek "sdc" zit.

![lsblk](http://i.imgur.com/zooJC6x.png)

Zodra u de regel van het sd kaartje heeft gevonden kijkt u bij de kolom "NAME". De naam zonder nummer is uw apparaat. In het voorbeeld hierboven is dit sdc omdat die als enige 8gb is (en de sd kaart is 8gb). Dat wil zeggen dat het apparaat zich op de locatie "/dev/sdc" bevindt.

U kunt nu middels het volgende commando de img op de sd kaart zetten. Let er dan wel op dat alle gegevens die nu op de sd kaart staan gewist zullen worden.<br />`sudo dd if=/pad/naar/het/.img/bestand of=/dev/sdc` <br />
Waar sdc de lettercombinatie is die u hierboven middels `lsblk` heeft gevonden.

Na het uitvoeren van het commando dient u te wachten tot het commando klaar is. Tot die tijd kunt u geen andere commando's in de terminal typen.
Als u de status wilt opvragen van de transactie opent u een tweede terminal en geeft u het volgende commando in `sudo kill -USR1 $(pidof dd)`


<div id = "windows-raspbian-install"></div>
###Vervolginstructie voor Windows

Als eerste stap moet het programma Win 32 Diskimager gedownload worden. klik [hier](http://sourceforge.net/projects/win32diskimager/files/latest/download) om dat te doen.
Nadat de installatie van het programma voltooid is kunt u het programma opstarten. Om het programma op te starten navigeert u naar "C:\Program Files (x86)\ImageWriter" (standaard installatie locatie) en dubbel klikt u op Win32DiskImager.exe.

Zodra het programma is gestart klikt u op het blauwe mapje en navigeert u naar het eerder gedownloade img bestand. Selecteer nu bij devices het sd kaartje waar Raspbian op geinstalleerd moet worden.
Klik vervolgens op "write" om raspbian om de sd kaart te installeren.

<div id = "mac-raspbian-install"></div>
###Vervolginstructie voor Mac OS
Als eerste stap gaan we het pad naar het sd kaartje waar we Raspbian op installeren zoeken. Dit kunnen we doen door het volgende commando in de terminal in te geven:<br />`diskutil list`<br />

U krijgt dan een venster met een aantal gegevens (onderstaande afbeelding). De belangrijkste gegevens hier zijn de "IDENTIFIER" en "SIZE". Meestal is de "SIZE" kolom genoeg om uw sd kaartje te vinden. Dit omdat andere block apparaten (zoals een hdd) vaak veel groter zijn. Kunt u echter niet door alleen de kolom "SIZE" te gebruiken achterhalen welke regel uw sd kaartje betreft dan kunt u simpelweg de sd kaart eruit halen en dan het commando intypen. Vervolgens stopt u de sd kaart terug en voert u het commando nog eens uit. De verandering in het tweede resultaat is dan uw sd kaartje. Op de afbeelding hieronder is te zien dat mijn sd kaart op plek "sdc" zit.

![diskutil list](http://i.imgur.com/J6Omy4Z.png)


Vervolgens zal u de sd kaart moeten "unmounten" dit kunt u doen met het volgende commando: <br />`diskutil unmountDisk /dev/disk4`<br />
waar 'disk4' de "IDENTIFIER" is die u bij de vorige stap heeft gevonden.

U kunt nu middels het volgende commando de img op de sd kaart zetten. Let er dan wel op dat alle gegevens die nu op de sd kaart staan gewist zullen worden.<br />`sudo dd bs=1m if=/pad/naar/het/.img/bestand of=/dev/disk4` <br />
waar 'disk4' de "IDENTIFIER" is die u bij de vorige stap heeft gevonden.


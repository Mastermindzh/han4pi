# ![han4pi header](http://i.imgur.com/t5m5nSy.png)

Han4pi is een groep van enthousiaste studenten die samen met 1 leraar (Johan Korten) workshops organiseren met de Raspberry pi microcomputer. Dit doen zij voor de Hogeschool van Arnhem en Nijmegen (HAN).

### Inhoud spelhandleiding:                                 
* Opbouw programmeercode
* Instellingen
* Hardware 
* Organisatie
* Speldoel

### Opbouw programmeercode: 
De code is gebaseerd op het object georiënteerde principe. Dit houdt in dat het hele programma is gebaseerd op klassen die bepaalde functies bezitten. Bijvoorbeeld De klasse bal heeft een functie om de bal te laten bewegen en een functie om de hoek te berekenen op het moment dat hij van een speler afketst. Een klasse is een soort blauwdruk van een bepaalde object. Met deze blauwdruk kan een instantie van het object (dus een variabele van het object) alle functies aanroepen die van toepassing zijn op het object.

Het pong spel bevat een aantal codebestanden. Programmeurs noemen deze bestanden klassen. Het pong spel bevat de volgende klassen: 
* Pong: Als het spel wordt afgespeeld, begint het spel in de pong klasse. Hier wordt het menu aangeroepen, en bepaald welke actie er moet plaatsvinden als de speler een optie van het menu kiest.
Speler: Deze klasse regelt alle acties van de speler. Denk bijvoorbeeld aan het bewegen van het padje, of het bijhouden van de punten.
* Bal: De bal zorgt ervoor dat de positie en beweging van de bal(len) word(en) bijgehouden. Raakt de bal een zijkant, dan zorgt deze dat er een nieuwe hoek wordt berekend.
* Hoofdmenu: Deze klasse tekent het hoofdmenu. Denk hierbij bijvoorbeeld aan het pijltje voor de geselecteerde optie.
Scherm: De scherm klasse bevat alles wat op het scherm wordt getekend. Deze klasse regelt het tekenen van afbeeldingen, tekst en objecten (de bal en de speler).
* Pongspel: Als de speler op "Start spel" drukt, wordt vervolgens de pongspel klasse aangeroepen. Deze zorgt ervoor dat het spel begint te draaien en de input van het toetsenbord wordt gelezen.
* potMeter: Deze klassen regelt de input van de potentiometer (kort: potmeter). Een potentiometer is een spanningsdeler die een analog einput terug geeft van 10 bits groot. Deze 10 bits (met de waarde van 0 tot 1023, dus 1024 waarden = 2^10) moeten worden omgezet zodat de locatie van de speler op het scherm wordt aangepast op basis van de input van de potmeter. Omdat het scherm waar de speler over beweegt geen 1024 pixels groot is moet de input van de potmeter worden omgezet naar pixels. 


### Instellingen:
De volgende twee opties zijn configureerbaar in het spel:
* Aantal ballen: De speler kan in het hoofdmenu het aantal gebruikte ballen instellen. 
* Spellengte: De maximale duur van het spel is in te stellen in het hoofdmenu. 

### Hardware:
De hub en de controllers zijn zelf bedacht, gebouwd en gesoldeerd. Door middel van het laten uitsnijden van de doosjes, het ontwerpen en bouwen van een klein printplaatje en het zelf bouwen van de onderdelen zijn de hub en de controllers tot stand gekomen. Het gebruik van telefoonkabels (RJ11) is voor het datatransport van de potentiometers naar de Raspberry Pi toe. De Raspberry Pi is de gebruikte microcontroller. Op deze microcontroller draait ook het programma en deze zorgt voor het uitlezen van de data uit de controllers. De waarde (spanning eigenlijk) die de controllers teruggeven wordt omgezet in een decimale waarde en op basis daarvan worden de spelers bewogen over het veld heen. Voor het spelen van de game is dus standaard een Raspberry Pi nodig (met de juiste software), minimaal 2 controllers, een hub en afhankelijk van het aantal controllers zijn er een aantal telefoonkabels nodig. 

### Organisatie:
Johan Korten (docent informatica aan de HAN) is de initiatiefnemer van dit project. Hij heeft aan twee studenten informatica (Rick van Lieshout en Ron Nabuurs) en aan twee studenten technische informatica (Simon Baars en Thomas Nobel) gevraagd of zij hem wilden helpen bij dit project. Gezamenlijk hebben zij ervoor gezorgd dat dit project tot stand is gekomen.

### Speldoel: 
Het doel van het spel is om een (of meerdere) ballen heen en weer te slaan. Het spel heeft veel overeenkomsten met tafeltennis vandaar ook de naam van het spel 'Pong'. Het doel voor elke speler dient te zijn om het balletje terug te slaan voordat hij de grens van zijn kant van het speelveld is gepasseerd. Indien dit toch gebeurd dan wordt het balletje gereset en krijgt de andere speler (die gescoord heeft) een punt erbij. De kunst van het spel is dus om de bal op een dergelijke manier te spelen dat de tegenspeler niet in staat is om de bal op tijd terug te spelen. 

Het spel was razend populair in de jaren 70 en 80 van de vorige eeuw. De naam van 'pong' is afgeleid van ping pong, wat zelf weer een synoniem is voor tafeltennis. Pong is een van de eerst uitgebrachte computerspellen. Het was tevens een van de eerste computerspellen die een (groot) commercieel succes is geworden.





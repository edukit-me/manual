Primul Program în IDE
=====================

1. Deschideți IDE-ul. Iconița programului arată așa: |ide-icon|

2. Schimbați limbla IDE-ului în Română.

    1. Intrați în meniul **File > Preferences**

    |ide-menu-preferences|

    2. Selectați limba Română și apesați OK

    |ide-menu-change-lang|

    3. Închideți IDE-ul și porniți-l din nou *(faceți restart)*.

    Acum toate textele sunt în limba Română.

3. Indicați modelul plăcii Arduino care e conectată la calculator.

    Găsiți meniul **Instrumente > Placă** și alegeți modelul.

|ide-menu-arduino-model|

4. Indicați portul prin care e conectat Arduino.

    Găsiți meniul **Instrumente > Port** și alegeți portul.

|ide-menu-port|

5. Găsiți și faceți click pe meniul

    **Fișier > Exemple > Basics > Blink**

|ide-menu-blink|

.. _ide-upload:

6. Apesați pe butonul **Încarcă** pentru a compila și a trimite programul pe Arduino.

|ide-upload-blink|

7. Priviți la Arduino să observați cum clipește led-ul.

|arduino-blink|

.. note::

    Led-ul poate fi de altă culoare (nu ca în imagine). Led-ul este marcat cu litera ``L``.

.. note::

    Pe sistemul de operare Linux/Ubuntu poate apărea următoarea eroare:

    .. code-block:: text

        avrdude: ser_open(): can't open device "/dev/ttyUSB0": Permission denied

    pentru a o rezolva, deschideți consola de sistem (în engleză se numește Terminal),
    o puteți găsi în meniul principal sau încercați să apesați pe combinația de taste Ctrl+Alt+T.
    Scrieți în consolă următoarele două comenzi:

    .. code-block:: sh

        sudo usermod -a -G dialout `whoami`

    Dacă în eroare nu e textul ``/dev/ttyUSB0`` dar ``/dev/ttyUSB1`` sau orice alt ``/dev/tty...``,
    înlocuiți în comanda de mai jos textul să fie la fel ca în eroare.

    .. code-block:: sh

        sudo chmod a+rw /dev/ttyUSB0

Inspectarea Programului
-----------------------

La început codul programului poate să vă pară complicat,
mai ales dacă nu aveți deloc cunoștințe în domeniu.
Nu vă faceți grji, peste cîteva pagini citirea și scrierea programelor vi se va da mult mai ușor.
Mai jos este explicat programul: din ce este compus și ce face fiecare rând.

.. warning::

    În explicație sunt folosiți termeni noi care cel mai probabil să nu îi cunoașteți,
    nu e o problemă, pur și simplu citiți textul.
    La moment scopul este să vă creați o viziune cum funcționează lucrurile,
    mai tîrziu absolut orice termen nou va fi explicat în detaliu.

.. code-block:: cpp

    void setup() {
        pinMode(13, OUTPUT);
    }

    void loop() {
        digitalWrite(13, HIGH);
        delay(1000);
        digitalWrite(13, LOW);
        delay(1000);
    }

1. Toate programele pe Arduino sunt compuse din 2 funcții: ``setup()`` și ``loop()``.
2. Funcția ``setup()`` se execută doar o singură dată
   și scopul ei este de a seta niște parametri înainte de execuția programului.
3. ``pinMode(13, OUTPUT);`` se traduce în română ca: setează pin-ul cu numărul 13 în mod de emitere.
   Inițial toți pinii sunt în mod de citire. Led-ul de pe placa Arduino este mereu pe pinul 13.
4. Funcția ``loop()`` se execută după ``setup()`` și se repetă la infinit
   atîta timp cît Arduino e conectat la o sursă de curent electric.
5. ``digitalWrite(13, HIGH);`` se traduce în română ca: trimite pinului 13 valoarea ce mai mare posibilă.
   Asta înseamnă că led-ul va primi curent electric și va lumina.
6. ``delay(1000);`` se traduce ca: oprește execuția programului pe 1 secundă (1000 milisecunde).
7. ``digitalWrite(13, LOW);`` înseamnă: trimite pinului 13 valoarea cea mai mică.
   Astfel led-ul nu va primi deloc curent electric și se va stinge.

Sper că ați prins deja ideea cum se execută codul programelor.
Dar pentru a scrie cod calitativ și a putea construi ceva interesant cu Arduino,
este nevoie să cunoașteți mai bine bazele programării.

.. |ide-icon| image:: _static/ide-icon.png
.. |ide-menu-preferences| image:: _static/ide-menu-preferences.png
.. |ide-menu-change-lang| image:: _static/ide-menu-change-lang.png
.. |ide-menu-blink| image:: _static/ide-menu-blink.png
.. |ide-upload-blink| image:: _static/ide-upload-blink.png
.. |arduino-blink| image:: _static/arduino-blink.gif
.. |ide-menu-arduino-model| image:: _static/ide-menu-arduino-model.png
.. |ide-menu-port| image:: _static/ide-menu-port.png

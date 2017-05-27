Salutare, RoboCrafter!
######################

Acesta este un ghid pentru începătorii în robotehnică.
Te va ajuta să înțelegi ce este un microcontroler, ce este programarea și cum să programezi un microcontroler.
Cu aceste cunoștințe poți să faci un bec să se aprindă cînd e întuneric în cameră, un semafor,
o mașină care merge singură și se ferește de obiecte, și multe altele.

.. important::

    Ghidul este conceput pentru a fi citit de la început pînă la capăt, pas cu pas.
    Treptat se explică definiții noi, lucruri mai complicate și interesante.

Ce este un microcontroler
-------------------------

Microcontroler este un cip care primește date, le procesează și generează alte date.
Modul în care datele sunt procesate este programat prin comenzi.
Există cipuri simple care suportă doar cîteva comenzi, și sunt cipuri avansate, de exemplu procesorul unui calculator.

|cip|

Ce este Arduino
---------------

Arduino este o placă mică și ieftină, creată special pentru începători în robotehnică
pentru a putea învăța și crea mecanisme simple automatizate.
La aceasta pot fi conectați ușor diferiți senzori, leduri, motoare și alte dispozitive.

|arduino-in-hand|

Ce este un program
------------------

Microcontrolerul nu înțelege limba română, nu putem să îi explicăm prin cuvinte ce și cum să facă.
Acesta înțelege doar un număr limitat de comenzi și primește date doar sub formă de ``1`` și ``0``,
sau diferite combinații de ``1`` și ``0`` care le interpretează ca litere și cifre,
de exemplu ``00110111`` este cifra ``7`` iar ``01100101`` este litera ``e`` -
acesta se numește **Format Binar**.
Nu e comod să scrii programe doar cu ``1`` și ``0``, de aceea au fost inventate limbajele de programare,
care îți dau posibilitatea să scrii programe folosind cuvinte și simboluri pe întelesul oamenilor,
care mai apoi se transformă în format binar și se trimit microcontrolerului pentru a fi executate.
Într-un program îi explici procesorului cum să primească niște date, ce să facă cu ele și unde să le trimită.

|pc-to-microcontroller|

Ce este Scratch
---------------

`Scratch <http://s4a.cat/>`__ *(se pronunță: Scrătci)* este un limbaj de programare grafic pentru copii,
prin care puteți crea programe doar din elemente grafice, fără a scrie cod.

|s4a|

.. include:: images.rst.txt

.. toctree::
    :hidden:

    prepare-tools/index
    first-program/index
    programming/index
Testarea Programelor
====================

Uneori aveți nevoie să vedeți ce se întîmplă în interiorul unui program
pentru ca să înțelegeți mai bine cum acesta se execută
sau să îl inspectați în caz că ceva nu merge.
Pentru a verifica dacă un senzor funcționează corect,
trebuie să vedeți ce valoare trimite acesta.
De exemplu senzorul de lumină vă trimite intensitatea luminii sub formă de număr
și doriți să verificați dacă valoarea se schimbă cînd stingeți lumina în cameră.

În IDE puteți trimite un număr (sau un text) din Arduino la calculator
și să îl vedeți pe ecran, scriind în cod:

.. code-block:: cpp

    Serial.println(123);
    Serial.println("Salutare!");

Toate valorile trimise prin ``Serial.println(...);`` sunt vizibile în Serial Terminal,
care poate fi deschis din meniul **Instrumente > Terminal serial**

.. _open-serial-terminal:

|ide-menu-serial-terminal|

Testarea senzorului de lumină
-----------------------------

Conectați la Arduino senzorul de lumină și un rezistor la fel ca în imaginea de mai jos.

.. important::

    Benzile colorate de pe rezistor trebuie să fie exact ca în imagine.

.. _arduino-and-light-sensor:

|arduino-uno-and-light-sensor|

.. note::

    Rezistorul este obligatoriu pentru ca senzorul să funcționeze corect.
    Fiecare senzor are o anumită rezistență și pentru a egala instensitatea curentului în circuit
    este nevoie de rezistor. Rezistența se calculează după o formulă din fizică.
    Despre electricitate veți învăța puțin mai tirziu, scopul acestui capitol să înțelegeți bazele programării.

Deschideți un fișier nou în IDE

|ide-menu-new-file|

Ștergeți tot codul existent și scrieți următorul cod:

.. code-block:: cpp

    void setup() {
      Serial.begin(9600);
    }

    void loop() {
      int intensitateaLuminii = analogRead(5);
      Serial.println(intensitateaLuminii);
      delay(1000);
    }

Încărcați programul în Arduino, apesând :ref:`butonul Încarcă <ide-upload>`.
Deschideți :ref:`Terminal serial <open-serial-terminal>`
și urmăriți cum se schimbă numărul cînd acoperiți senzorul cu mîna.

|ide-serial-monitor-light-sensor|

.. rubric:: Inspectarea programului

.. note::

    Mai jos sunt cîțiva termeni noi care cel mai probabil nu îi cunoașteți.
    Totul va fi explicat puți mai tîrziu, la moment nu este obligatoriu să înțelegeți tot codul,
    pur și simplu citiți textul pentru a vă crea o viziune cum funcționează lucrurile.

1. Programul este format din două părți: ``setup()`` (se execută o singură dată) și ``loop()`` (se repetă la infinit).
2. ``Serial.begin(9600);`` pornește conexiunea cu **Terminal serial**.
3. ``int intensitateaLuminii = analogRead(5);`` se traduce ca:
   Citește valoarea de la senzorul conectat la pinul analog 5 *(marcat pe placă ca A5)*
   și păstreaz-o în variabila sub numele ``intensitateaLuminii``.
4. ``Serial.println(intensitateaLuminii);`` se traduce ca:
   Trimite în terminal serial valoarea din variabila ``intensitateaLuminii``.
5. ``delay(1000);`` înseamnă: Oprește execuția programului timp de o secundă (1000 milisecunde).

.. include:: /images.rst.txt
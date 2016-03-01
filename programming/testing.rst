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

...

.. include:: /images.rst.txt
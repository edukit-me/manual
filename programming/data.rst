Datele
======

Toate dispozitivele conectate la Arduino trimit și primesc informație.
De exemplu, de la senzorul de lumină primiți un număr care semnifică intensitatea luminii.
Cît de tare să lumineze un led sau cît de rapid să se rotească un motor la fel se indică cu numere.
Deci este esențial să cunoașteți cum să lucrați cu datele.

În limbajele de programare cele mai simple date sunt numerele și textele.
Numerele se reprezintă simplu ``123``, iar tot ce se află între ghilimele este text ``"Salut!"``.

Textele
-------

Testați următorul cod:

.. code-block:: cpp

    void setup() {
        "Salut, Lume!";
    }

    void loop() {}

Codul de mai sus a creat un text dar nu a făcut nimic cu el.
Pentru a afișa datele, în Arduino se folosește funcția ``Serial.printl(...);``.

.. note::

    În C++ după orice comandă trebuie de pus ``;``

Testați următorul cod:

.. code-block:: cpp

    void setup() {
        Serial.begin(9600);

        Serial.println("Salut, Lume!");
    }

    void loop() {}

Deschideți :ref:`Terminal serial <open-serial-terminal>` pentru a vedea textul afișat de program.

|ide-test-text|

.. note::

    Codul ``Serial.begin(9600);`` este obligatoriu pentru că ``Serial.println(...);`` să funcționeze.

Numerele
--------

Numerele sunt folosite pentru a face calcule.

Testați următorul cod:

.. code-block:: cpp

    void setup() {
        Serial.begin(9600);

        Serial.println(2);
        Serial.println(7 + 3);
    }

    void loop() {}

În terminal serial ar trebuie să arate:

|ide-test-numbers|

Cu numerele puteți face adunarea ``+``, scăderea ``-``, înmulțirea ``*``, împărțirea ``/`` și alte operații.

.. |ide-test-numbers| image:: _static/ide-test-numbers.png
.. |ide-test-text| image:: _static/ide-test-text.png
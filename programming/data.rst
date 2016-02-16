Datele
======

Toate dispozitivele conectate la Arduino trimit și primesc informație.
De exemplu, de la senzorul de lumină primiți un număr care semnifică intensitatea luminii,
cît de tare să lumineze un led sau cît de rapid să se rotească un motor la fel se indică cu numere.
Deci este esențial să cunoașteți cum să lucrați cu datele.

În limbajele de programare cele mai simple date sunt numerele și textele.
Numerele se reprezintă simplu ``123``, iar tot ce se află între ghilimele este text ``"Salut!"``.

:ref:`Testați <test>` următorul cod:

.. code-block:: cpp

    "Salut, Lume!";

.. note::

    În C++ după orice comandă trebuie de pus ``;``

Codul de mai sus a creat un text dar nu a făcut nimic cu el.
Pentru a afișa datele, în C++ se folosește comanda ``cout <<``.

.. code-block:: cpp

    cout << "Salut, Lume!";

Felicitări! Ați creat un program care afișează un text.

Numerele sunt folosite pentru a face calcule.

.. code-block:: cpp

    cout << 7 + 3;

Puteți face adunarea ``+``, scăderea ``-``, înmulțirea ``*``, împărțirea ``/`` și alte operații.
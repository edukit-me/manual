Ciclurile
=========

Ciclurile sunt niște grupuri de instrucțiuni (bucăți de cod)
care se execută repetat atîtat timp cît o condiție este îndeplinită.
De exemplu:

* Adună la un număr +1 atîta timp cît numărul este mai mic decît 10.
* Mișcă mașina înainte atîta timp cît nu este nici un obstacol la 10cm distanță.
* Ține led-ul aprins atîta timp cît în cameră e întuneric.

Acum o să învățați 2 cicluri (``while`` și ``for``).
Acestea au structură diferită dar elementele de bază sunt aceleași:
ambele au o condiție care decide dacă ciclul trebuie să continue să se repete
și ambele au un grup de comenzi care se execută la fiecare ciclu.

while
-----

Din engleză ``while`` (se pronunță: *uail*) se traduce ca: atîta timp cît. Structura instrucțiunii ``while`` este:

.. code-block:: text

    while (condiție) {
        instrucțiuni...
    }

Codul de mai sus se traduce ca: Atîta timp cît condiția este satisfăcută
(are valoarea :ref:`boolean <cpp-base-types>` ``true``)
execută instrucțiunile care se află între acolade ``{   }``.

:ref:`Exemplul precedent <eg-next-numbers-not-optimized>` poate fi scris mai compact:

.. _cpp-comments:

.. note::

    În limbajul C++ totul ce este scris dupa două slashuri ``//`` (două bare oblice)
    este interpretat ca **comentariu** și nu afectează deloc programul.
    Comentariile sunt folosite pentru a scrie notițe în codul programului
    ca să fie înțeles mai ușor de alți programatori.

.. code-block:: cpp

    void setup() {
        Serial.begin(9600);

        int x = 7; // numărul care va fi incrementat (mărit)
        int i = 3; // numărul de incrementări (cicluri)

        while (i > 0) { // aîtat timp cît variabila i este un număr pozitiv
            x = x + 1; // mărește numărul cu 1
            Serial.println(x); // afișează numărul în terminal serial

            i = i - 1; // scade numărul de cicluri rămase
        }
    }

    void loop() {}

for
---

...
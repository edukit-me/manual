Cicluri
=======

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

Din engleză ``while`` (se pronunță: *uail*) se traduce ca: atîta timp cît.
Structura instrucțiunii ``while``:

.. code-block:: text

    while (condiție) {
        instrucțiuni...
    }

Codul de mai sus se traduce ca: Atîta timp cît condiția este satisfăcută
(are valoarea :ref:`boolean <cpp-base-types>` ``true``)
execută instrucțiunile din acolade ``{   }``.

:ref:`Exemplul precedent <eg-next-numbers-not-optimized>` poate fi scris mai compact:

.. _cpp-comments:

.. note::

    În limbajul C++ totul ce este scris dupa două slashuri ``//`` (două bare oblice)
    este interpretat ca **comentariu** și nu afectează deloc programul.
    Comentariile sunt folosite pentru a scrie notițe în codul programului
    ca să fie înțeles mai ușor de alți programatori.

.. _eg-next-numbers-with-while:

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

Instrucțiunea ``for``, pe lîngă condiție și blocul cu instrucțiuni, mai conține încă două componente:
inițializarea (instrucțiune care se execută inainte de primul ciclu) și
contor (instrucțiunea care se execută după fiecare ciclu).
Structura instrucțiunii ``for``:

.. code-block:: text

    for (inițializare; condiție; contor) {
        instrucțiuni...
    }

Codul de mai sus se traduce ca: Execută **inițializarea**.
Atîta timp cît **condiția** este îndeplinită (are valoarea ``true``),
execută **instrucțiunile** din acolade ``{   }`` și instrucțiuniea **contor**.

|for-loop|

:ref:`Exemplul precedent <eg-next-numbers-with-while>` poate fi scris cu ``for``:

.. _eg-next-numbers-with-for:

.. code-block:: cpp

    void setup() {
        Serial.begin(9600);

        int x = 7;

        for (int i = 0; i < 3; ++i) {
            ++x;
            Serial.println(x);
        }
    }

    void loop() {}

.. note::

    ``++i`` este varianta prescurtată a ``i = i + 1``.
    La fel poate fi scris ``--i`` care înseamnă ``i = i - 1``.

Codul de mai sus se traduce așa: Creză variabila ``x`` și atribuie-i valoarea ``7``;
Crează variabila ``i`` și atribuie-i valoare ``0``;
Atîta timp cît valoarea din ``i`` este mai mică decît ``3``,
mărește valoarea din ``x`` cu ``1``, afișeaz-o în terminal serial și mărește valoarea din ``i`` cu ``1``.

.. |for-loop| image:: _static/for-loop.svg

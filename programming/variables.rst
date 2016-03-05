Variabilele
===========

Datele pot fi scrise direct în cod, dar o metodă mai comodă este păstrarea lor în variabile.
O variabilă este un nume care păstrează date.
La fel ca în matematică sau fizică cînd înălțimea se notează ca litera ``h``,
``Pi`` semnifică numărul ``3.14...``, etc.

De exemplu, pentru a afișa următoarele 3 numere mai mari decît numărul 7,
fără variabilă programul arată așa:

.. code-block:: cpp

    void setup() {
        Serial.begin(9600);

        Serial.println(7 + 1);
        Serial.println(7 + 2);
        Serial.println(7 + 3);
    }

    void loop() {}

Acum schimbați programul să afișeze următoarele 3 numere mai mari decît numărul 9.
O să observați că programul are un neajuns:
de fiecare dată o să trebuiască să schimbați aceeași cifră în 3 locuri.
Soluția este să folosiți o variabilă.

Variabila mai întîi trebuie definită, adică să îi explicați calculatorului cum se numește variabila
și ce tip de date o să conțină.

Tipurile de bază în C++ sunt:

* ``int`` - număr întreg: ``1``, ``7``, ``1``
* ``float`` - număr rațional: ``2``, ``3.1``, ``1.007``
* ``string`` - text: ``"Salutare!"``

De exemplu:

.. code-block:: cpp

    int numar_intreg = 2;
    float numar_rational = 3.6;
    string text = "Salut!";

Deci programul care afișează următoarele 3 numere mai mari decît numărul 7,
folosind variabile, arată în felul următor:

.. code-block:: cpp

    void setup() {
        Serial.begin(9600);

        int x = 7;

        Serial.println(x + 1);
        Serial.println(x + 2);
        Serial.println(x + 3);
    }

    void loop() {}

Acum pentru a afla următoarele 3 numere mai mari decît numărul 9,
este nevoie de schimbat doar o variabilă: ``int x = 9;``.

Valoarea variabilei poate fi modificată oricînd, iar programul de mai sus poate fi scris altfel:

.. code-block:: cpp

    void setup() {
        Serial.begin(9600);

        int x = 7;

        x = x + 1;
        Serial.println(x);

        x = x + 1;
        Serial.println(x);

        x = x + 1;
        Serial.println(x);
    }

    void loop() {}

**Exercițiu**: Modificați programul să arate următoarele 10 numere mai mari decît variabila ``x``.

Observați că programul conține cod care se repetă.
Acesta e un indiciu că programul poate fi îmbunătățit.
Continuați să citiți pentru a afla cum să scrieți programul de mai sus mai compact.
Variabilele
===========

Datele pot fi scrise direct în cod, dar o metodă mai comodă este păstrarea lor în variabile.
O variabilă este un text, o denumire, care obligatoriu trebuie să înceapă cu o literă.

De exemplu, pentru a face un program care afișează următoarele 3 numere ale numărului 7, fără variabilă ar fi așa:

.. code-block:: cpp

    cout << 7 + 1;
    cout << " ";
    cout << 7 + 2;
    cout << " ";
    cout << 7 + 3;

Acum schimbați programul să afișeze următoarele 3 numere ale numărului 9.
O să observați că programul are un neajuns: trebuie să schimbați aceeași cifră în 3 locuri.
Soluția este să folosiți o variabilă.

Variabila mai întîi trebuie definită, adică să îi explicați calculatorului cum se numește variabila
și ce tip de date o să conțină. Tipurile de bază în C++ sunt:

* ``int`` - număr întreg (``1``, ``7``, ``1``)
* ``float`` - număr rațional (``2``, ``3.1``, ``1.007``)
* ``string`` - text

De exemplu:

.. code-block:: cpp

    int numar_intreg = 2;
    float numar_rational = 3.6;
    string text = "Salut!";

Deci un programul care afișează următoarele 3 numere ale numărului 9, folosind variabile, arată în felul următor:

.. code-block:: php

    int x = 9;

    cout << x + 1;
    cout << " ";
    cout << x + 2;
    cout << " ";
    cout << x + 3;

Acum pentru a afla următoarele 3 numere ale altui număr, este nevoie de schimbat doar o cifră în cod.

Valoarea variabilei poate fi schimbată, iar exemplul de mai sus poate fi scris altfel:

.. code-block:: php

    int x = 9;

    x = x + 1;
    cout << x;

    cout << " ";

    x = x + 1;
    cout << x;

    cout << " ";

    x = x + 1;
    cout << x;

Programul de mai sus poate fi îmbunătățit pentru că mult cod se repetă, continuați să citiți pentru a afla cum.
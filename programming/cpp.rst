Limbajul de Programare C++
==========================

C++ *(se pronunță: si plus plus)* este un limbaj de programare avansat care vă permite să scrieți orice tip de programe pentru orice dispozitiv.
În această carte vor fi explicate doar cîteva subiecte elementare
cu ajutorul cărora veți fi capabili să scrieți programe simple pentru a putea lucra cu dispozitivele conectate la Arduino.

Crearea programelor în C++ pentru Arduino decurge în 4 pași:

1. Scrierea programului sub formă de text
2. Compilarea - C++ verifică textul de erori apoi generează un fișier (cu ``1 0``)
   care poate fi înțeles și executat de microcontroler
3. Trimiterea programului pe Arduino
4. Executarea programului

Primul pas e cel mai important, restul pașilor de obicei decurg automat doar printr-o apăsare de buton.

.. _test:

Pentru ca să nu vă complicați cu instalarea C++ pe calculator,
e mult mai comod să folosiți un complilator C++ online, de exemplu http://cpp.sh/

.. important::

    Toate exemplele care urmează le puteți testa cu acest cod:

    .. code-block:: cpp

        #include <iostream>
        using namespace std;
        int main() {

            // Scrieți aici codul din exemple (puteți ștearge aceast rând)

            return 0;
        }

    Nu vă speriați de cuvintele și simbolurile stranii din codul de mai sus,
    ele sunt obligatorii ca programul să funcționeze, cu timpul veți înțelege pentru ce ele trebuiesc.
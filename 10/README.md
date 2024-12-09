# Laboratorul 10 - Model Test de Laborator

1. **\[Total 1.5 p]** Se citește de la tastatură o propoziție în care cuvintele sunt separate prin câte un spațiu.

    a. **\[0.75 p]** Să se afișeze care este lungimea maximă a unui cuvânt din propoziție.
    b. **\[0.75 p]** Să se afișeze cuvintele de lungime maximă din propoziție pe o linie, separate cu spațiu.

    **Exemplu:**
    
    | Input                                      | Output               |
    |--------------------------------------------|----------------------|
    | pentru acest exemplu avem lungime maxima 7 | 7<br>exemplu lungime |

2. **\[Total 2.5 p]**

    a. **\[0.5 p]** Scrieți o funcție fără parametri care citește de la tastatură o listă de numere naturale (un vector)
cu elementele date pe o linie separate cu spații și returnează această listă.

    b. **\[1 p]** Scrieți o funcție care primește ca parametru un număr natural `n` și returnează numărul de divizori proprii ai lui `n`.

    c. **\[1 p]** Folosind funcția de la a) să se citească o listă `v` de numere naturale.
Apoi se citește de la tastatură un număr natural `k`. Folosind funcția de la b) afișați pe ecran numerele din lista `v`
care au cel mult `k` divizori proprii, ordonate crescător, fără duplicate (un număr va fi scris o singură dată chiar dacă apare de mai multe ori în listă).

    **Exemplu:**

    | Input                     | Output    |
    |---------------------------|-----------|
    | 9 1 9 100 101 10 7 9<br>2 | 1 7 9 101 |


3. **\[1.5 p]** Se citește din fișierul `cuvinte.in` o listă de cuvinte.
Cuvintele sunt răsfirate pe un număr arbitrar de linii, cu spații între ele.
Să se afișeze cuvintele care se termină cu vocală, folosind comprehensiune.

    **Exemplu:**
    
    | cuvinte.in                                         | Output                 |
    |----------------------------------------------------|------------------------|
    | Acest exemplU<br>este<br>pe mai mult de<br>un rand | exemplU este pe mai de | 

4. **\[Total 3.5 p]** Fișierul text `produse.in` conține date despre vânzările unui magazin.
Fiecare linie din fișier are următoarea structură:

    `nume_produs % categorie % cantitate % pret`

    unde `nume_produs` este un șir de caractere reprezentând numele unui produs, `categorie` este numele categoriei din
care produsul face parte (numele categoriei și al produsului sunt formate din cuvinte separate prin câte un spațiu și nu
conțin caracterul `%`), `cantitate` reprezintă numărul (întreg) de bucăți vândute din produsul respectiv, iar `pret`
este un număr real ce reprezintă prețul de vânzare al produsului. Un exemplu de astfel de fișier este:

    ```
    Lapte % Alimente % 10 % 5.5
    Ciocolata % Dulciuri % 5 % 10.0
    Suc % Bauturi % 20 % 3.5
    Paine % Alimente % 15 % 4.0
    Lapte % Alimente % 5 % 5.5
    Apa % Bauturi % 10 % 2.0
    ```

    a. **\[1.5 p]** Scrieți o funcție `citire_produse` care să citească și să memoreze datele din fișierul `produse.in`
într-o structură de date astfel încât să se răspundă cât mai eficient la cerințele de la punctele următoare.
Funcția va întoarce structura de date creată.

    b. **\[1 p]** Scrieți o funcție `total_vanzari` care primește ca parametru structura de date în care s-au memorat datele la cerința a).
Funcția va întoarce suma totală ce a fost obținută din vânzarea tuturor produselor, indiferent de categoria din care fac parte.
Să se apeleze funcția `total_vanzari` pentru a calcula și afișa suma obținută din vânzarea tuturor produselor citite din fișier.

    c. **\[1 p.]** Folosind funcțiile de la punctele a) și b), citiți informațiile despre produse și afișați în fișierul
`vanzari.out` suma totală obținută din vânzări pentru fiecare categorie în parte, câte una pe fiecare linie,
în ordine descrescătoare a sumei obținute, iar la final, totalul vânzărilor.

    **Exemplu:**

    | produse.in                                                                                                                                                                          | vanzari.out                                                 |
    |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
    | Lapte % Alimente % 10 % 5.5<br>Ciocolata % Dulciuri % 5 % 10.0<br>Suc % Bauturi % 20 % 3.5<br>Paine % Alimente % 15 % 4.0<br>Lapte % Alimente % 5 % 5.5<br>Apa % Bauturi % 10 % 2.0 | Alimente 142.5<br>Bauturi 90<br>Dulciuri 50<br>Total: 282.5 |

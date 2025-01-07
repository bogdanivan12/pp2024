# Laboratorul 12

## Cerințe

### Divide et Impera

1. Se dă un vector `a = (a1, ..., an)` de tip munte (există un indice `i` astfel încât `a1 < a2 < ... < ai > ai+1 > ... > an`;  `ai` se numește vârful muntelui).
Propuneți un algoritm eficient care determină vârful muntelui (în calculul complexității algoritmului nu se consideră și citirea vectorului).  

| date.in     | date.out |
|-------------|----------|
| 4 8 10 11 5 | 11       |


2. De pe prima linie a fișierului `numere.txt` se citește un sir de numere naturale. Folosiți metoda Divide et Impera pentru a verifica dacă în șir exista numere prime.

### Backtracking

3. Să se afișeze `p` numere cu `n` cifre, cu proprietatea că fiecare număr afișat are toate cifrele nenule și nu are două cifre egale.

4. Să se afișeze `p` numere cu `n` cifre, cu proprietatea că fiecare număr afișat are toate cifrele nenule și nu are două cifre alăturate egale.

### Greedy

5. Se dă o sumă `S`  și avem la dispoziție bancnote cu valorile: `1`, `5`, `10`, `25`.
Să se determine o modalitate de a plăti suma `S` folosind un număr minim de bancnote.
Algoritmul propus mai funcționa și dacă aveam bancnote cu valorile `1`, `10`, `30`, `40`?

## Temă

### Divide et Impera

6. a) Scrieți o funcție care primește ca parametru o listă de numere întregi ordonată crescător și un număr `x`
și returnează prima poziție pe care apare `x` în listă (sau `-1` dacă nu apare)

    b) Scrieți o funcție care primește ca parametru o listă de numere întregi ordonată crescător și un număr `x`
și returnează ultima poziție pe care apare `x` în listă (sau `-1` dacă nu apare)
   
    c) Scrieți o funcție `nr_aparitii` eficientă care primește ca parametru o listă de numere întregi ordonată crescător
și un număr `x` și returnează numărul de apariții ale unei valori `x` în listă, folosind funcțiile de la a) și b).
De exemplu, `nr_aparitii([1, 1, 2, 2, 2, 2, 6, 9, 9, 20], 2)` va returna `4`.

### Backtracking

7. [PbInfo - permutari_pfp](https://www.pbinfo.ro/probleme/3150/permutari-pfp)

8. Într-o clasă sunt `n` fete identificate prin numerele naturale de la `1` la `n` și `m` băieți identificați prin
numerele naturale de la `n + 1` la `n + m`. Să se afișeze toate modalitățile de a forma echipe de câte `2k` elevi din
clasă astfel încât în fiecare echipă să fie `k` fete și `k` băieți (`n, m, k > 2` se citesc de la tastatură).
În cadrul unei echipe nu contează ordinea membrilor.

### Greedy

9. Se dau `n` cuburi cu laturile diferite două câte două. Fiecare cub are o culoare, codificată cu un număr de la `1` la `p` (`p` dat). 
Să se construiască un turn de înălțime maximă de cuburi în care un cub nu poate fi așezat pe un cub de aceeași culoare
sau cu latură mai mică decât a sa – `O(n logn)`. Pe prima linie a fișierului de intrare se dau `n` şi `p`, iar pe
următoarele linii latura şi culoarea fiecărui cub. În fișierul de ieșire se vor afișa înălțimea turnului obținut şi
indicele cuburilor folosite (de la bază la vârf).

| date.in                          | date.out    |
|----------------------------------|-------------|
| 4 2<br>5 1<br>10 1<br>9 1<br>8 2 | 23<br>2 4 1 |

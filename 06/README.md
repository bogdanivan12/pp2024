# Laboratorul 06

[*Documentație Python - Liste*](https://docs.python.org/3/tutorial/datastructures.html)

## Cerințe

### Comprehensiune

1. Se citește o propoziție cu cuvintele separate prin spații. Să se creeze o listă cu cuvintele care încep cu o vocală.

2. Să se obțină, pentru o listă de numere dată, lista conținând elementele care au aceeași paritate cu poziția pe care se află.
**Exemplu:** pentru lista `[2, 4, 1, 7, 5, 1, 8, 10]` se va obține lista `[2, 7, 1, 8]`.

3. Se citește de la tastatură un text. Se cere să se “traducă” în limba păsărească textul dat, astfel:
după fiecare vocală se adaugă litera `p` și încă o dată acea vocală (după `a`, `e`, `i`, `o`, `u` se adaugă respectiv `pa`, `pe`, `pi`, `po`, `pu`).
**Exemplu:** `Ana are mere.` devine `Apanapa aparepe meperepe.`

### Operații cu liste

4. Se dă o listă de numere naturale. Să se șteargă din listă subsecvența delimitată de primele două zerouri din listă (inclusiv zerourile).

5. Se dă o listă de numere naturale și un număr natural `k`.
Să se elimine din listă subsecvența de lungime `k` de sumă minimă (dacă sunt mai multe se va elimina prima, adică cea mai din stânga),
fără a folosi liste suplimentare.

6. Se dă o listă de numere reale (toate elementele sale se vor da pe o linie separate prin spațiu).
Să se insereze câte un 0 după fiecare element negativ, fără a folosi liste suplimentare.

### Algoritmi fundamentali

7. [Leetcode - Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/)

8. [PbInfo - Numarare6](https://www.pbinfo.ro/probleme/547/numarare6)

9. [PbInfo - Proportionale](https://www.pbinfo.ro/probleme/296/proportionale)

## Temă

10. Se dă o listă de numere. 
    - Să se obțină lista cu elementele impare din lista dată.
    - Să se obțină lista cu elementele aflate pe poziții impare în lista dată.

11. Să se genereze lista literelor de la `a` la `z` (folosind `ord`, `chr`, comprehensiune).

12. Cifrul lui Cezar ([Laborator 04 - Problema 9](https://github.com/bogdanivan12/pp2024/tree/main/04)) folosind comprehensiune.

13. Se dau două liste `L1` și `L2` de lungime `n`. Să se înlocuiască elementele de pe poziții pare din `L1` cu cele de pe poziția corespunzătoare din `L2` folosind feliere (slice).

14. Dată o listă de numere naturale și un număr `k`, propuneți mai multe modalități de a șterge primele `k` elemente din listă.

15. Se dă o listă de numere naturale ordonată crescător (toate elementele sale se vor da pe o linie separate prin spațiu). Să se elimine duplicatele din listă.

16. Se citește un vector. Să se afișeze care este valoarea minimă din vector și  pe ce poziții apare aceasta.

17. Se dă un număr natural `n > 2`. Să se afișeze primele `n` linii din triunghiul lui Pascal. **Exemplu:** pentru `n = 6` se va afișa:
    ```
    1
    1  1
    1  2  1
    1  3  3  1
    1  4  6  4  1
    1  5 10 10  5  1
    ```

18. [PbInfo - MinPal](https://www.pbinfo.ro/probleme/2923/minpal)

19. [Leetcode - Move Zeroes](https://leetcode.com/problems/move-zeroes/description/)

20. [Leetcode - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

21. [Leetcode - Next Permutation](https://leetcode.com/problems/next-permutation/description/)

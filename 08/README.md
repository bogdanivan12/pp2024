# Laboratorul 08

## Cerințe
1. În fișierul text `test.in` se află testul unui elev de clasa a II-a la matematică, conținând `9` înmulțiri scrise pe rânduri distincte.
Un calcul corect este notat cu un punct, iar unul incorect cu `0` puncte. Să se realizeze un program care să evalueze testul dat, astfel:
în dreptul fiecărui calcul corect se va scrie mesajul `Corect`, iar în dreptul fiecărui calcul greșit se va scrie mesajul `Gresit`
și rezultatul corect, iar la final se va scrie nota *(un punct se acordă din oficiu!)*.
Rezultatul evaluării testului se va afișa în fișierul `test.out`.

    | test.in                                                                                                | test.out                                                                                                                                                                                   |
    |--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | 3\*4=11<br>2\*10=20<br>5\*5=24<br>7\*4=28<br>2\*6=12<br>10\*10=100<br>3\*9=27<br>6\*7=33<br>0\*9=1<br> | 3\*4=11 Gresit 12<br>2\*10=20 Corect<br>5\*5=24 Gresit 25<br>7\*4=28 Corect<br>2\*6=12 Corect<br>10\*10=100 Corect<br>3\*9=27 Corect<br>6\*7=33 Gresit 42<br>0\*9=1 Gresit 0<br>Nota 6<br> |

2. Instituția “Carpe diem” are `n` angajați (`n` citit de pe prima linie a fișierului `cd.in`).
Instituția are program de lucru intre orele `a`, `b` (citite din fișier, date fiecare pe o linie).
Pentru fiecare angajat se citește ora la care are o activitate în instituție și activitatea durează exact o ora.
Șeful dorește să organizeze o ședință de o oră din timpul programului de lucru, care să nu se suprapună cu nicio activitate din instituție
(astfel încât să poată participa toți angajații). Care sunt orele libere (dacă există) dintre care șeful poate alege să organizeze ședința?

    | cd.in                                                   | Ecran                                       |
    |---------------------------------------------------------|---------------------------------------------|
    | 7  <br>9<br>17<br>12<br>10<br>14<br>14<br>10<br>15<br>9 | Seful poate alege dintre orele: 11, 13, 16. |

3. Se citește din fișier un vector (elementele date pe o linie a fișierului, separate cu spațiu) și un număr `k` (dat pe o linie nouă în fișier).
Să se afișeze elementele distincte din vector care au cel puțin `k` cifre (folosind și comprehensiune pentru mulțimi), ordonate crescător.

4. Pe fiecare linie din fișierul multimi.in se află elementele unei mulțimi. Să se afişeze cardinalul minim al unei mulțimi din  fișier,
mulțimile care au cardinal minim și reuniunea acestora.

5. Se citește din fișier o matrice. 
   - Să se afişeze elementele din matrice care au exact `k` divizori proprii ordonate decrescător, fără duplicate. 
   - Să se afișeze liniile din matrice cu număr maxim de elemente distincte.

6. Se dă un fișier care are pe fiecare linie elementele unei mulțimi separate prin spațiu. Mulțimile se pot repeta.
Să se afișeze numărul de mulțimi distincte care apar. *(Hint: set de frozenset)*


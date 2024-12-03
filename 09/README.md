# Laboratorul 09

## Cerințe
1. Andrei lucrează într-un magazin de șosete, iar fiecare șosetă are asociat un număr întreg ce aparţine intervalului `[1,100]` pentru a o identifica mai ușor din ce model face parte.
Dându-se un vector neordonat de astfel de coduri, aflați câte perechi de șosete se pot forma.

2. În fișierul `elevi.in` sunt memorate informații despre elevii unei clase, astfel: pe o linie a fișierului se dau următoarele informații despre un elev:
CNP, nume și prenume și lista de note, de exemplu:

    ```
    2501910000034 Ionescu Ion 10 8 7 8
    2402900000041 Marinica Maria 9 10 8 8 8
    1412900000041 Petrescu Petrica 8 10 4 7
    ```
   
   - Memorați lista de elevi din fișier astfel încât să se poată răspunde cât mai eficient la întrebări de tipul celor de la subpunctele următoare
   (dat CNP elev, care sunt notele, să se modifice lista de note a elevului). 
   - Scrieți o funcție care primește ca parametri un CNP și structura de date în care s-au memorat datele despre elevi la punctul a) și crește cu `1` prima notă a elevului cu CNP-ul primit ca parametru.
   Funcția returnează nota după modificare sau `None` dacă CNP-ul nu există. Apelați funcția pentru un CNP citit de la tastatură.
   - Scrieți o funcție care primește ca parametri un CNP, o listă de note și structura de date în care s-au memorat datele despre elevi la punctul a) și adaugă lista de note la notele elevului cu CNP-ul primit ca parametru.
   Funcția returnează lista de note după modificare sau `None` dacă CNP-ul nu există. Apelați funcția pentru un CNP citit de la tastatură si lista `l_note=[10, 8]`.

3. Scrieți un program care să determine grupurile de cuvinte dintr-un fișier text care p-rimează între ele, adică au aceleași ultime p-litere, adică același p-sufix (`p` citit de la tastatura).
Pentru aceasta se va scrie o funcție care primește ca parametru un nume de fișier și un număr `p` și returnează un dicționar cu grupurile de cuvinte din fișier sub următoarea formă:
fiecare cheie din dicționar este un p-sufix, iar valoarea asociată este lista cuvintelor cu acel sufix.
Numele fișierului de intrare se va citi de la tastatură, iar grupurile se vor scrie în fișierul text `rime.txt`,
câte un grup pe o linie, în ordine descrescătoare în raport cu numărul de elemente din grup.
Cuvintele din fiecare grup vor fi sortate lexicografic descrescător.

   **Exemplu:** Pentru `p = 2` și fișierul `rime.in`:

   | rime.in                                                          | rime.txt                                                            |
   |------------------------------------------------------------------|---------------------------------------------------------------------|
   | ana dana<br>mere pere prune<br>bune<br>banana si gutui amare are | pere mere are amare<br>dana banana ana<br>prune bune<br>si<br>gutui |

4. Se citește de la tastatură un număr natural `n`. Se citesc apoi, pentru `n` persoane, numele și data nasterii,
   pe câte o linie. Să se afișeze, pentru fiecare lună în parte, persoanele născute în acea lună și anul nașterii lor.

   | Input                                                                                      | Output                                                                                              |
   |--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
   | 3<br>Pop-Ionescu Diana 21.03.2000<br>Danila Mara 03.03.2002<br>Toma Laura-Elena 12.02.2000 | Martie:<br>Pop-Ionescu Diana, 2000<br>Danila Mara, 2002<br><br>Februarie:<br>Toma Laura-Elena, 2000 |

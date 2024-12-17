# Laboratorul 11

## Cerințe

### Sortări
1. Să se implementeze un program care primește ca intrare o propoziție și sortează cuvintele din aceasta în funcție de
numărul de vocale din fiecare cuvânt. Dacă două cuvinte au același număr de vocale, acestea vor fi sortate lexicografic
în ordine crescătoare.

### Recursivitate și functii cu număr variabil de parametrii
2. Creați modulul `algoritmi_elementari` care să conțină câte o funcție pentru fiecare din următoarele cerințe:
    
    a. calculează numărul de cifre ale unui număr (iterativ);
    
    b. calculează numărul de cifre ale unui număr (recursiv);

    c. calculează numărul de cifre divizibile cu 3 (iterativ);

    d. calculează numărul de cifre divizibile cu 3 (recursiv);

   Importați modulul `algoritmi_elementari` și folosiți apeluri ale funcțiilor definite.

3. Implementați o funcție care primește un *număr variabil de numere naturale* și un număr `c` și returnează câte dintre
numerele întregi primite ca parametru au numărul de cifre cel puțin `c` (folosind funcția de la subpunctul *b)*
din modulul `algoritmi_elementari`). Apelați funcția pentru numerele `15`, `19`, `178` și `2856` și cu valoarea
parametrului `c` egală cu `2` (parametrul actual corespunzător lui `c` la apel este `2`).

4. Scrieți o funcție recursivă care calculează suma elementelor unui vector.

5. Scrieți o funcție care calculează suma elementelor unui vector folosind metoda Divide et Impera

### Transmiterea parametrilor. Variabile locale și globale
6. Ce se afişează în urma rulării următorului fragment de cod:
   ```
   def f(lista):
       a = b 
       lista.append(a) 
       lista.sort() 
       lista = lista[:-1] 
       lista.append(a + b)
       print(lista)
   
   
   l = [4, 2, 5, 10]
   a = 1
   b = 3
   f(l)
   print(l)
   print(a)
   print(b)
   ```

## Temă
7. Considerăm o listă de tupluri care conțin informații despre filme, fiecare tuplu având următoarele elemente:
`(nume_film, rating, an_aparitie, gen)`. Implementați un program care să ofere opțiuni pentru sortarea listei de filme
în funcție de diferite criterii. Aveți de implementat mai multe subpuncte:

   a. Sortați lista de filme în ordine descrescătoare în funcție de rating. Pentru filme cu acelaşi rating,
sortați-le în ordine lexicografică descrescătoare în funcție de numele filmului.

   b. Sortați lista de filme în ordine crescătoare după gen. Pentru filmele cu același gen, sortați-le în ordine
descrescătoare în funcție de rating.

   c. Sortați lista de filme în ordine crescătoare după anul de apariție. Pentru filmele cu același an de apariție,
sortați-le în ordine lexicografică crescătoare în funcție de numele filmului.

8. Creați modulul `algoritmi_elementari` care să conțină câte o funcție pentru fiecare din următoarele cerințe:

   e. să verifice dacă un număr este palindrom (returnând `True` / `False`);

   f. să verifice dacă un număr este prim (returnând `True` / `False`);

   g. să returneze o listă cu toate numerele prime mai mici decât o valoare dată;

   h. șterge prima / ultima apariție dintr-un număr `x` a unei cifre (implicit se șterge cifra `0`);
**ex.:** `x = 324238367`, `c = 3` => `x = 32423867` (pentru ștergerea ultimei apariții); `x = 324238367`, `c = 3` =>
`x = 24238367` (pentru ștergerea primei apariții);

   i. returnează valoarea obținută prin mutarea la final a primei cifre a unui număr;
**ex.:** `x = 324238367` => `x = 24238673`;

   Importați modulul `algoritmi_elementari` și folosiți apeluri ale funcțiilor definite.

9. Scrieți o funcție care calculează cel mai mare divizor comun pentru elementele unui vector folosind metoda Divide et
Impera.

10. a) Scrieți o funcție `alipire` cu *număr variabil de parametri* care să furnizeze numărul natural obținut prin
alipirea cifrelor maxime ale numerelor naturale nenule primite ca parametri. 

   De exemplu, pentru numerele `4251`, `73`, `8` și `133` funcția trebuie să returneze numărul `5783`. 

   b) Scrieți o funcție cu `3` parametri nenuli de tip întreg `a`, `b` și `c` care să verifice dacă aceștia pot fi 
   considerați ca fiind numere scrise în baza `2` sau nu, folosind apeluri utile ale funcției definite anterior.
   
   De exemplu, pentru numerele `1001`, `11` și `100` funcția trebuie să returneze valoarea `True`, iar pentru numerele
   `1001`, `17` și `100` trebuie să returneze valoarea `False`.

   (Indicatie – `alipire(alipire(a, b, c)) = 1`)

11. Fișierul text `studenti.txt` conține date despre studenți. Fiecare linie a fișierului conține informații despre un
student în formatul următor: `nume, medie, an_studiu, specializare`. Implementați un program care să ofere opțiuni
pentru sortarea studenților în funcție de diferite criterii, citind datele din fișierul specificat.
Aveți de implementat mai multe subpuncte:
    - Sortați lista de studenți în ordine crescătoare după specializare. Pentru studenții cu aceeași specializare, sortați-i în ordine descrescătoare în funcție de medie.
    - Sortați lista de studenți în ordine crescătoare după anul de studiu. Pentru studenții cu același an de studiu, sortați-i în ordine lexicografică crescătoare în funcție de numele lor.
    - Sortați lista de studenți în ordine descrescătoare în funcție de media lor. Pentru studenții cu aceeași medie, sortați-i în ordine lexicografică crescătoare în funcție de numele lor.

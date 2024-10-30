# Laboratorul 04

## Cerințe

1. Fie şirul `s = "petrecere"`. Scrieţi felieri astfel încât să obţineţi valorile: `"cere"`, `"eee"`, `"rece"`.

2. Se citește un șir de caractere în care după fiecare literă a fost introdus caracterul `x`. Afișați șirul inițial.

3. Se citește un șir de caractere reprezentând o propoziție în care cuvintele sunt despărțite între ele prin spații.
Să se numere câte cuvinte din propoziție se termină cu o vocală şi au minim `3` litere.

4. Se citește un cuvânt `s`. Să se determine cel mai mare prefix al acestuia care este palindrom.

5. Scrieți un program care să poată cripta un text folosind Cifrul Atbash.
Cifrul Atbash este o formă simplă de criptare în care literele alfabetului sunt inversate.
Acesta înseamnă că litera `A` este înlocuită cu `Z`, litera `B` cu `Y`, și tot așa.
Textul de criptat conţine doar litere mari.

6. Se citește un șir de cuvinte în care cuvintele sunt separate între ele printr-o virgulă urmată de un spațiu.
Să se afișeze lungimea maximă a unui cuvânt din șir.

7. - Se citește un cuvânt `w`, un număr natural nenul `p`, un număr natural `n` și un șir format din `n` cuvinte, date fiecare pe o linie.
Să se afișeze toate cuvintele care sunt p-rime cu `w` (adică ultimele `p` caractere din cuvânt coincid cu ultimele `p` caractere ale lui `w`) și au lungime cel puțin `p + 2`.
De exemplu, pentru `w = "mere"`, `p = 2` , `n = 4` și cuvintele `"pere"`, `"teste"`, `“are”` și `"programare"`,
trebuie să fie afișate cuvintele `"pere"` și `"programare"` (`“are”` rimează cu `“mere”`, dar are lungime mai mică decât `p + 2`).
   - Aceeași cerință, dar pentru cuvintele dintr-o propoziție în care cuvintele sunt despărțite între ele prin spații.
   De exemplu, pentru `w = "cere"`, `p = 2`, `n = 4` și propoziția `"Ana are mere si pere si banane de mancare"`,
   trebuie să se afișeze următorul rezultat: `2-rimele cuvântului 'cere' sunt: are mere pere mancare`.

8. Se citește un șir de caractere `s`. Să se verifice dacă există un șir `t`, diferit de `s`,
astfel încât `s` să se poată obține prin concatenarea de un număr arbitrar de ori (`𝑘 > 1`) a șirului `t` (adică să se verifice dacă șirul `s` este periodic).
Dacă există mai multe astfel de șiruri `t` se va determina cel mai lung.
**Exemplu:** șirul `s = abbaabbaabbaabba` se obține prin concatenarea șirului `t = abbaabba` de două ori.

9. Cifrul lui Cezar
   - Se citește un text și un număr natural `k`.
   Să se afișeze textul cifrat cu cifrul lui Cezar, prin care fiecare literă *(! doar literele !)* este înlocuită cu litera aflată peste `k` poziții la dreapta în alfabet în mod circular
   (valoarea `k` reprezintă cheia secretă comună pe care trebuie să o cunoască atât expeditorul, cât și destinatarul mesajului criptat).
   De exemplu, pentru textul `"O zi frumoasa!"` și `k = 9` se va afișa `“X ir oadvxjbj!"`
   - Se citește un număr natural `k` și text criptat cu cifrul lui Cezar cu cheia `k`. Să se afișeze textul decriptat.

## Temă
10. Ce valoare au pentru șirul `s = "acest exemplu"` felierile: `s[0:4]`, `s[0:4:2]`, `s[0:4:-2]`, `s[0::2]`, `s[::100]`,
`s[::-100]`, `s[-3:-1]`, `s[-1:4]`, `s[-12:4]`, `s[len(s):]`? Cum se poate accesa prin feliere subsecvența `"exe"` folosind indici pozitivi?
Dar folosind indici negativi?

11. [pbinfo.ro - acronim](https://www.pbinfo.ro/probleme/2828/acronim)
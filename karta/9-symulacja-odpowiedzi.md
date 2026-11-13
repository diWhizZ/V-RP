# 9. Symulacja odpowiedzi obywateli

Jakie odpowiedzi na 30 pytań z [dokumentu 8](8-pytania-do-obywateli.md)
dają układ, w którym żadna grupa poglądów nie przegrywa wyraźnie.

> **To nie jest sondaż ani prognoza.** Nikt nie pytał żadnego obywatela.
> Symulacja liczy wyłącznie skutki założeń wpisanych przez autorów: ocen
> wariantów i wag siedmiu umownych profili. Zmiana założeń zmienia wynik.
> Założenia są jawne w pliku [symulacja.py](../narzedzia/symulacja.py)
> i każdy może je poprawić.

---

## 1. Jak to policzono

1. **Warianty.** Każde pytanie dostało 2–4 możliwe odpowiedzi. W części A
   pierwszą jest zawsze rozwiązanie projektu.
2. **Osiem kryteriów.** Każdy wariant oceniono od −2 do +2 pod względem:
   wolności osoby, wpływu obywateli, ochrony mniejszości, trwałości
   i bezpieczeństwa państwa, sprawności i kosztu, odwracalności,
   solidarności, dziedzictwa i tożsamości.
3. **Siedem profili.** Każdy przykłada do kryteriów inne wagi: wolnościowy,
   wspólnotowy, solidarystyczny, państwowy, obywatelski, praworządnościowy,
   pragmatyczny (równe wagi). To typy idealne, nie grupy społeczne ani
   partie; ich liczebność w społeczeństwie jest nieznana.
4. **Równowaga** to wariant, przy którym profil oceniający go najgorzej
   traci najmniej. Nie jest to wariant „najlepszy” ani większościowy.
5. **Próba odporności.** 4000 powtórzeń; w każdym oceny są losowo
   przesuwane o jeden stopień, wagi profili o do 50 %, a udziały profili
   w społeczeństwie losowane od nowa. „Stabilność” to odsetek powtórzeń,
   w których równowaga wypada na ten sam wariant. „Większość” to wariant
   najczęściej wygrywający głosowanie i odsetek powtórzeń, w których wygrał.

Ocena: **stabilna** — stabilność co najmniej 60 % i ten sam wariant wygrywa
głosowanie; **chwiejna** — ten sam wariant, ale stabilność poniżej 60 %;
**spór** — równowaga stabilna, lecz większość wybiera co innego;
**brak równowagi** — ani jedno, ani drugie.

---

## 2. Wynik pytanie po pytaniu

| Nr | Sprawa | Odpowiedź równowagi | Stabilność | Większość | Najmniej zyskuje | Ocena |
|---|---|---|---|---|---|---|
| 1 | Obowiązek głosowania | obowiązek bez sankcji | 45% | obowiązek z opłatą (73%) | państwowy | brak równowagi |
| 2 | Referenda wiążące | raz w roku | 87% | raz w roku (60%) | państwowy | stabilna |
| 3 | Ustawy ustrojowe | referendum na żądanie | 56% | zawsze referendum (50%) | wolnościowy | brak równowagi |
| 4 | Losowani w parlamencie | głos doradczy i sprzeciw | 36% | 120 z równym głosem (53%) | państwowy | brak równowagi |
| 5 | Wybór posłów | imiennie, z odwołaniem | 78% | imiennie, z odwołaniem (78%) | praworządnościowy | stabilna |
| 6 | Kadencja i pensja posła | dwie kadencje, pensja przeciętna | 79% | dwie kadencje, pensja przeciętna (54%) | wolnościowy | stabilna |
| 7 | Głowa państwa | z wyboru, strażnik | 81% | z wyboru, strażnik (70%) | państwowy | stabilna |
| 8 | Sąd konstytucyjny | losowanie spośród zgłoszonych | 67% | losowanie spośród zgłoszonych (72%) | państwowy | stabilna |
| 9 | Druga kadencja sędziego konst. | tak, za zgodą obywateli | 61% | tak, za zgodą obywateli (63%) | praworządnościowy | stabilna |
| 10 | Sędziowie lokalni | konkurs i losowani ławnicy | 81% | konkurs i losowani ławnicy (69%) | państwowy | stabilna |
| 11 | Nadzór nad policją lokalną | komendant mianowany | 49% | rzecznik z wyboru (64%) | solidarystyczny | brak równowagi |
| 12 | Szefowie organów kontroli | samo losowanie | 65% | samo losowanie (60%) | wspólnotowy | stabilna |
| 13 | Progi zmiany konstytucji | 2/3 dla całości | 68% | 2/3 dla całości (52%) | obywatelski | stabilna |
| 14 | Głosowanie elektroniczne | najpierw próba lokalna | 52% | najpierw próba lokalna (45%) | państwowy | chwiejna |
| 15 | Minimum godnego bytu | z urzędu, forma w ustawie | 96% | z urzędu, forma w ustawie (96%) | państwowy | stabilna |
| 16 | Fundusz obywatelski | fundusz jako rezerwa, bez wypłat | 52% | fundusz jako rezerwa, bez wypłat (49%) | wolnościowy | chwiejna |
| 17 | Automatyzacja urzędu | automat i odwołanie do człowieka | 66% | odmawia tylko człowiek (55%) | wspólnotowy | spór: równowaga ≠ większość |
| 18 | Naród w preambule | wszyscy obywatele + kultura i historia | 85% | wszyscy obywatele + kultura i historia (63%) | obywatelski | stabilna |
| 19 | Odwołanie w preambule | do obu | 69% | do obu (35%) | obywatelski | stabilna |
| 20 | Małżeństwo i rodzina | ustawa, możliwe referendum | 96% | ustawa, możliwe referendum (91%) | wspólnotowy | stabilna |
| 21 | Ochrona życia | konstytucja daje ramy, reszta ustawa | 78% | konstytucja daje ramy, reszta ustawa (69%) | państwowy | stabilna |
| 22 | Państwo a religia | współpraca przy autonomii | 60% | ścisły rozdział (62%) | praworządnościowy | spór: równowaga ≠ większość |
| 23 | Kompetencje nieprzekazywalne | wąskie jądro | 96% | wąskie jądro (92%) | solidarystyczny | stabilna |
| 24 | Zasady niezmienialne | brak | 51% | wąskie jądro (56%) | państwowy | brak równowagi |
| 25 | Granica wolności słowa | także zniesławienie i nienawiść, wąsko, przed sądem | 82% | także zniesławienie i nienawiść, wąsko, przed sądem (67%) | państwowy | stabilna |
| 26 | Powiadomienie o inwigilacji | zawsze, odroczenie tylko za zgodą sądu | 89% | zawsze (49%) | wspólnotowy | spór: równowaga ≠ większość |
| 27 | Zawartość minimum | oraz podstawowa opieka zdrowotna | 60% | oraz podstawowa opieka zdrowotna (56%) | wolnościowy | chwiejna |
| 28 | Granica długu | z wyjątkiem obronności, 3/5 | 84% | z wyjątkiem obronności, 3/5 (79%) | solidarystyczny | stabilna |
| 29 | Zasoby strategiczne | wody, lasy, złoża publiczne; sieci pod nadzorem | 66% | wody, lasy, złoża publiczne; sieci pod nadzorem (50%) | wolnościowy | stabilna |
| 30 | Obowiązek obrony | powszechne krótkie szkolenie, szeroka służba zastępcza | 73% | powszechne krótkie szkolenie, szeroka służba zastępcza (63%) | wolnościowy | stabilna |

Podsumowanie: 19 odpowiedzi stabilnych, 3 chwiejne, 3 sporne, 5 bez
równowagi (pytanie 3 leży na granicy i przy innym losowaniu wypada jako
chwiejne).

---

## 3. Wynik dla całego pakietu

Zadowolenie profilu: 0 % — we wszystkich 30 sprawach dostał wariant dla
siebie najgorszy; 100 % — we wszystkich najlepszy.

| Pakiet odpowiedzi | wolnościowy | wspólnotowy | solidarystyczny | państwowy | obywatelski | praworządnościowy | pragmatyczny | najniższe |
|---|---|---|---|---|---|---|---|---|
| Projekt 2.0 w części A, równowaga w części B | 73% | 87% | 94% | 61% | 92% | 79% | 92% | **61%** |
| Najwyższa średnia w każdym pytaniu | 82% | 87% | 94% | 78% | 87% | 94% | 100% | **78%** |
| Równowaga w każdym pytaniu osobno | 79% | 86% | 83% | 80% | 83% | 86% | 95% | **79%** |
| Równowaga całego pakietu | 80% | 85% | 81% | 80% | 81% | 86% | 94% | **80%** |
| Wszystko po myśli profilu: wolnościowy | 100% | 48% | 80% | 50% | 90% | 87% | 88% | **48%** |
| Wszystko po myśli profilu: wspólnotowy | 60% | 100% | 77% | 85% | 69% | 71% | 83% | **60%** |
| Wszystko po myśli profilu: solidarystyczny | 80% | 62% | 100% | 41% | 93% | 85% | 88% | **41%** |
| Wszystko po myśli profilu: państwowy | 51% | 90% | 55% | 100% | 49% | 65% | 70% | **49%** |
| Wszystko po myśli profilu: obywatelski | 83% | 48% | 84% | 36% | 100% | 73% | 82% | **36%** |
| Wszystko po myśli profilu: praworządnościowy | 85% | 62% | 86% | 70% | 73% | 100% | 89% | **62%** |
| Wszystko po myśli profilu: pragmatyczny | 84% | 90% | 94% | 75% | 87% | 91% | 100% | **75%** |

Co z tego wynika:

- **Układ równowagi istnieje.** Przy odpowiedziach z tabeli 2 każdy profil
  dostaje co najmniej 79 % tego, co mógłby dostać, a rozpiętość między
  profilami wynosi 16 punktów.
- **Projekt 2.0 jest przechylony.** Bardzo dobrze służy profilom
  obywatelskiemu i solidarystycznemu (92–94 %), wyraźnie gorzej państwowemu
  (61 %) i wolnościowemu (73 %). Powód: projekt konsekwentnie wybiera wpływ
  obywateli kosztem sprawności i bezpieczeństwa.
- **Żaden profil nie może dostać wszystkiego bez ciężkiej straty innych.**
  Pakiet ułożony pod jeden profil spycha najsłabszy do 36–75 %.
- **Dopasowanie całego pakietu naraz prawie nic nie dodaje** (80 % wobec
  79 %) i wymagałoby zmiany tylko odpowiedzi w pytaniu 1.

---

## 4. Gdzie równowaga odbiega od projektu

| Nr | Projekt 2.0 | Równowaga | Pewność | Co projekt by zyskał | Co by stracił |
|---|---|---|---|---|---|
| 2 | Referenda dwa razy w roku | Raz w roku | stabilna | Mniej zmęczenia, niższy koszt | Wolniejsza korekta błędów; dłuższe czekanie na weto ludowe |
| 6 | Jedna kadencja posła | Dwie kadencje | stabilna | Więcej doświadczenia w parlamencie | Wraca zachęta do głosowania pod reelekcję |
| 10 | Sędzia lokalny z wyboru | Konkurs i losowani ławnicy | stabilna | Mniej orzekania pod publiczność | Mieszkańcy nie wybierają sędziego |
| 12 | Losowanie pięciu i wybór | Samo losowanie | stabilna | Brak kampanii o urząd bezstronny; prościej | Obywatele nie wybierają osoby |
| 13 | Progi 3/4 i 3/5 | 2/3 dla całości | stabilna | Jeden próg; mniejsze ryzyko blokady | Słabsza ochrona zasad i praw |
| 17 | Odmawia tylko człowiek | Automat z odwołaniem do człowieka | spór | Szybciej i taniej | Człowiek rozpatruje sprawę dopiero po odwołaniu |
| 14 | E-głosowanie obok papieru | Najpierw próba lokalna | chwiejna | Błąd wyjdzie na małą skalę | Opóźnienie |
| 16 | Fundusz z równą wypłatą | Fundusz jako rezerwa | chwiejna | Większe bezpieczeństwo finansów | Obywatel nie dostaje udziału do ręki |
| 1 | Obowiązek z opłatą | Obowiązek bez sankcji | brak równowagi | Mniej przymusu | Obowiązek staje się deklaracją |
| 3 | Ustawy ustrojowe zawsze w referendum | Referendum na żądanie | brak równowagi | Mniej głosowań | Zmiana reguł gry może przejść niezauważona |
| 4 | 120 losowanych z równym głosem | Głos doradczy i sprzeciw | brak równowagi | Decydują tylko osoby z mandatem | Losowani tracą realny wpływ |
| 11 | Rzecznik bezpieczeństwa z wyboru | Komendant mianowany | brak równowagi | Mniej polityki wokół policji | Mieszkańcy tracą nadzór |

Projekt i równowaga są zgodne w pytaniach 5, 7, 8, 9 i 15.

Trzy z tych rozbieżności dotyczą spraw, które rozstrzygnął współautor
projektu: wyboru sędziów lokalnych (10), wyboru osób na urzędy kontrolne
(12) i progu 3/4 (13). Symulacja nie jest powodem, żeby je zmieniać —
pokazuje tylko, które profile ponoszą ich koszt.

W pytaniach 1, 3, 4, 11 i 17 większość w symulacji popiera rozwiązanie projektu,
a równowaga wskazuje co innego. Tu wynik nie daje podstaw do
zmiany.

---

## 5. Pytania światopoglądowe (18–24)

Symulacja ocenia w nich wyłącznie skutki ustrojowe: odwracalność, wpływ
obywateli, ochronę mniejszości. **Nie ocenia, co jest dobre**, więc nie
zastępuje odpowiedzi obywateli. Pokazuje jedno: w sprawach małżeństwa (20)
i ochrony życia (21) najmniej przegranych zostawia pozostawienie
rozstrzygnięcia ustawie i referendum albo zapisanie w konstytucji samych
ram. Wynika to wprost z założenia, że odwracalność jest zaletą; kto uważa,
że pewne sprawy powinny być właśnie nieodwracalne, odrzuci to założenie
i wynik razem z nim.

W pytaniach 22 (państwo a religia) i 24 (zasady niezmienialne) równowagi
nie ma: wynik zależy od tego, ilu jest obywateli o danych poglądach.
To trzeba po prostu policzyć w głosowaniu.

---

## 6. Ograniczenia

1. **Oceny są subiektywne.** Około 700 ocen wpisał model AI. Inny autor
   wpisałby inne.
2. **Metoda sprzyja wariantom pośrednim.** Wariant środkowy z definicji
   nikogo mocno nie krzywdzi, więc często wygrywa. Kompromis bywa jednak
   gorszy od obu skrajności — na przykład obowiązek bez sankcji może nie
   mieć zalet ani przymusu, ani dobrowolności.
3. **Pytania są liczone osobno.** Symulacja nie widzi, że rozwiązania się
   zazębiają: jedna kadencja ma sens razem z odwołaniem posła, a próg 3/4
   razem z brakiem zasad niezmienialnych.
4. **Profile to nie społeczeństwo.** Nie wiadomo, ilu obywateli jest
   któremu bliskich; prawdziwi ludzie łączą poglądy inaczej.
5. **Kryteriów jest osiem i są równe co do skali.** Rzeczy, których nie
   ujęto (na przykład prostota), nie wpływają na wynik.

Symulacja nadaje się do jednego: wskazania, o które pytania warto spierać
się najpierw. Nie nadaje się do rozstrzygania.

---

*Tabele wygenerowano poleceniem `python3 narzedzia/symulacja.py`
(ziarno 2026, 4000 powtórzeń).*

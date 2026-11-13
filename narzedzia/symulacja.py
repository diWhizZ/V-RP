#!/usr/bin/env python3
"""Symulacja odpowiedzi na 30 pytań do obywateli (dokument 9).

To NIE jest sondaż ani prognoza. Oceny wariantów i wagi profili są
założeniami autorów; każdy może je zmienić i uruchomić skrypt ponownie:

    python3 narzedzia/symulacja.py            # tabele w Markdown
    python3 narzedzia/symulacja.py --seed 7   # inne losowanie

Kryteria (ocena wariantu od -2 do +2, 0 = bez wpływu):
  W wolność osoby            O wpływ obywateli na decyzje
  M ochrona mniejszości      T trwałość i bezpieczeństwo państwa
  S sprawność i koszt        K odwracalność (możliwość korekty)
  L solidarność              D dziedzictwo i tożsamość
"""
import random, sys

KRYT = "WOMTSKLD"

# Profile: wagi kryteriów (suma 1). Typy idealne, nie grupy społeczne.
PROFILE = {
    "wolnościowy":      dict(W=.35, O=.10, M=.15, T=.05, S=.15, K=.10, L=.00, D=.10),
    "wspólnotowy":      dict(W=.05, O=.10, M=.05, T=.20, S=.05, K=.05, L=.15, D=.35),
    "solidarystyczny":  dict(W=.10, O=.15, M=.15, T=.05, S=.05, K=.10, L=.35, D=.05),
    "państwowy":        dict(W=.05, O=.05, M=.05, T=.35, S=.20, K=.05, L=.10, D=.15),
    "obywatelski":      dict(W=.15, O=.35, M=.10, T=.05, S=.05, K=.20, L=.05, D=.05),
    "praworządnościowy":dict(W=.10, O=.05, M=.30, T=.15, S=.15, K=.20, L=.05, D=.00),
    "pragmatyczny":     {k: .125 for k in KRYT},
}

def o(**kw):
    return [kw.get(k, 0) for k in KRYT]

# Pytanie -> lista wariantów (etykieta, oceny). W części A wariant
# pierwszy to zawsze rozwiązanie projektu.
PYTANIA = {
 1: ("Obowiązek głosowania", [
    ("obowiązek z opłatą", o(W=-1,O=2,M=1,T=1,S=-1,L=1)),
    ("udział dobrowolny", o(W=1,M=-1,S=1,L=-1)),
    ("obowiązek bez sankcji", o(O=1))]),
 2: ("Referenda wiążące", [
    ("dwa razy w roku", o(O=2,M=-1,T=-1,S=-1,K=2)),
    ("raz w roku", o(O=1,K=1)),
    ("tylko na wniosek władz", o(O=-2,T=1,S=1,K=-1))]),
 3: ("Ustawy ustrojowe", [
    ("zawsze referendum", o(O=2,M=1,T=1,S=-1,K=1)),
    ("referendum na żądanie", o(O=1,M=1,T=1,K=1)),
    ("sam parlament 3/5", o(O=-1,M=-1,S=1,K=-1))]),
 4: ("Losowani w parlamencie", [
    ("120 z równym głosem", o(O=2,M=1,T=-1,S=-1,L=1)),
    ("głos doradczy i sprzeciw", o(O=1,S=-1)),
    ("bez losowanych", o(O=-1,T=1,S=1))]),
 5: ("Wybór posłów", [
    ("imiennie, z odwołaniem", o(O=2,M=-1,T=1,S=1,K=1)),
    ("listy proporcjonalne", o(O=-1,M=2,K=-1)),
    ("system mieszany", o(O=1,M=1,S=-1))]),
 6: ("Kadencja i pensja posła", [
    ("jedna kadencja, pensja przeciętna", o(O=1,T=-1,S=-1,K=1,L=1)),
    ("dwie kadencje, pensja przeciętna", o(O=1,L=1)),
    ("bez ograniczeń", o(O=-1,T=1,S=1,K=-1,L=-1))]),
 7: ("Głowa państwa", [
    ("z wyboru, strażnik", o(O=1,M=1,S=-1,K=1,D=1)),
    ("wybierana przez parlament", o(O=-1,S=1)),
    ("z wyboru, kieruje rządem", o(O=1,M=-2,T=1,S=1,K=-1,D=1))]),
 8: ("Sąd konstytucyjny", [
    ("losowanie spośród zgłoszonych", o(W=1,M=2,S=-1)),
    ("wybór przez parlament", o(M=-1,S=1)),
    ("wybór przez obywateli", o(O=2,M=-2,T=-1))]),
 9: ("Druga kadencja sędziego konst.", [
    ("tak, za zgodą obywateli", o(O=1,M=-1,S=1,K=1)),
    ("jedna długa kadencja", o(M=2,K=-1))]),
 10: ("Sędziowie lokalni", [
    ("wybór przez mieszkańców", o(W=-1,O=2,M=-1,S=-1,K=1)),
    ("konkurs i losowani ławnicy", o(W=1,O=1,M=1)),
    ("powołanie przez radę sądownictwa", o(W=1,O=-1,M=1,S=1,K=-1))]),
 11: ("Nadzór nad policją lokalną", [
    ("rzecznik z wyboru", o(W=1,O=2,S=-1,K=1)),
    ("komendant mianowany", o(T=1,S=1))]),
 12: ("Szefowie organów kontroli", [
    ("losowanie 5 i wybór", o(O=1,M=1,S=-1,K=1)),
    ("samo losowanie", o(M=2,S=1)),
    ("wybór przez parlament", o(O=-1,M=-1,S=1,K=-1))]),
 13: ("Progi zmiany konstytucji", [
    ("3/4 i 3/5", o(O=-1,M=2,T=1,S=-1,K=-1,D=1)),
    ("2/3 dla całości", o(M=1,T=1)),
    ("3/5 dla całości", o(O=1,M=-1,T=-1,S=1,K=1))]),
 14: ("Głosowanie elektroniczne", [
    ("obok papieru, pod warunkami", o(W=1,O=1,T=-1,S=1)),
    ("tylko papier", o(T=1,S=-1)),
    ("najpierw próba lokalna", o(O=1,K=1))]),
 15: ("Minimum godnego bytu", [
    ("z urzędu, forma w ustawie", o(M=1,S=-1,K=1,L=2)),
    ("na wniosek, po sprawdzeniu", o(W=-1,S=-1,L=-1)),
    ("konkretne świadczenie w konstytucji", o(T=-1,S=-2,K=-2,L=2))]),
 16: ("Fundusz obywatelski", [
    ("fundusz z równą wypłatą", o(T=1,S=-1,L=1)),
    ("bez funduszu, niższy dług", o(W=1,S=1,L=-1)),
    ("fundusz jako rezerwa, bez wypłat", o(T=2))]),
 17: ("Automatyzacja urzędu", [
    ("odmawia tylko człowiek", o(W=1,M=2,S=-2,K=1,L=1)),
    ("automat i odwołanie do człowieka", o(M=1,S=1,K=1)),
    ("pełna automatyzacja", o(W=-1,M=-2,S=2,L=-1))]),
 18: ("Naród w preambule", [
    ("wszyscy obywatele, bez określeń", o(W=1,M=2,D=-1)),
    ("wszyscy obywatele + kultura i historia", o(M=1,T=1,D=2)),
    ("wspólnota kultury i pochodzenia", o(W=-1,M=-2,T=-1,D=2))]),
 19: ("Odwołanie w preambule", [
    ("do Boga", o(W=-1,M=-1,D=2)),
    ("do wartości uniwersalnych", o(W=1,M=1,D=-1)),
    ("do obu", o(M=1,D=1)),
    ("do żadnego", o(W=1,M=1,S=1,D=-2))]),
 20: ("Małżeństwo i rodzina", [
    ("definicja w konstytucji", o(W=-1,M=-1,K=-2,D=2)),
    ("ustawa, możliwe referendum", o(W=1,O=1,K=2,D=-1))]),
 21: ("Ochrona życia", [
    ("rozstrzyga konstytucja", o(O=-1,K=-2,D=1)),
    ("ustawa i referendum", o(O=2,M=-1,K=2,D=-1)),
    ("konstytucja daje ramy, reszta ustawa", o(O=1,M=1,K=1))]),
 22: ("Państwo a religia", [
    ("współpraca przy autonomii", o(D=2)),
    ("ścisły rozdział", o(W=1,M=1,S=1,D=-1))]),
 23: ("Kompetencje nieprzekazywalne", [
    ("szeroki katalog", o(O=1,M=-1,T=1,S=-1,K=1,D=2)),
    ("wąskie jądro", o(O=1,M=1,T=2,S=1,K=1,D=1)),
    ("bez katalogu", o(O=-1,M=1,T=-1,S=1,K=-1,D=-2))]),
 24: ("Zasady niezmienialne", [
    ("szeroki katalog", o(O=-2,M=2,T=1,K=-2)),
    ("wąskie jądro", o(O=-1,M=2,T=2,K=-1)),
    ("brak", o(O=2,M=-1,T=-1,K=2))]),
 25: ("Granica wolności słowa", [
    ("tylko nawoływanie do przemocy", o(W=2,O=1,M=-1,T=-1,K=1)),
    ("także zniesławienie i nienawiść, wąsko, przed sądem", o(W=1,O=1,M=1)),
    ("szerokie ograniczenia", o(W=-2,O=-1,T=1,K=-1))]),
 26: ("Powiadomienie o inwigilacji", [
    ("zawsze", o(W=2,M=2,T=-2,K=1)),
    ("zawsze, odroczenie tylko za zgodą sądu", o(W=1,M=1,K=1)),
    ("nie", o(W=-2,M=-2,T=1,S=1))]),
 27: ("Zawartość minimum", [
    ("żywność i schronienie", o(S=1)),
    ("oraz podstawowa opieka zdrowotna", o(M=1,L=1)),
    ("oraz mieszkanie i dochód", o(M=1,T=-1,S=-2,L=2))]),
 28: ("Granica długu", [
    ("twarda, bez wyjątków", o(S=1,K=-1,L=-1)),
    ("z wyjątkiem obronności, 3/5", o(T=2,S=1)),
    ("bez granicy w konstytucji", o(T=-1,S=-1,K=1,L=1))]),
 29: ("Zasoby strategiczne", [
    ("wszystkie publiczne", o(W=-1,T=2,S=-1,K=-1,L=1,D=1)),
    ("wody, lasy, złoża publiczne; sieci pod nadzorem", o(T=1,L=1,D=1)),
    ("bez zastrzeżeń", o(W=1,T=-1,S=1,K=1))]),
 30: ("Obowiązek obrony", [
    ("powszechna służba", o(W=-2,T=2,S=-1,L=1,D=1)),
    ("powszechne krótkie szkolenie, szeroka służba zastępcza", o(W=-1,M=1,T=1,L=1,D=1)),
    ("armia zawodowa i ochotnicy", o(W=2,T=-1,S=1,L=-1))]),
}

def uzyt(wagi, oceny):
    return sum(wagi[k] * s for k, s in zip(KRYT, oceny))

def tabela(pyt=PYTANIA, prof=PROFILE):
    """u[q][wariant][profil]"""
    return {q: [[uzyt(w, oc) for w in prof.values()] for _, oc in war]
            for q, (_, war) in pyt.items()}

def maximin(u):       # wariant, przy którym najgorzej oceniający traci najmniej
    return max(range(len(u)), key=lambda i: (min(u[i]), sum(u[i])))

def srednia(u):
    return max(range(len(u)), key=lambda i: sum(u[i]))

def wiekszosc(u, udzialy):   # zwycięzca porównań parami; brak -> najwięcej pierwszych miejsc
    n = len(u)
    for i in range(n):
        if all(sum(s for s, a, b in zip(udzialy, u[i], u[j]) if a > b) >
               sum(s for s, a, b in zip(udzialy, u[i], u[j]) if b > a)
               for j in range(n) if j != i):
            return i
    pierwsze = [0.0] * n
    for p, s in enumerate(udzialy):
        pierwsze[max(range(n), key=lambda i: u[i][p])] += s
    return max(range(n), key=lambda i: pierwsze[i])

def zadowolenie(U, wybor):
    """Dla każdego profilu: 0 = dostał wszędzie wariant najgorszy dla siebie,
    1 = wszędzie najlepszy."""
    wyn = []
    for p in range(len(PROFILE)):
        got = sum(U[q][wybor[q]][p] for q in U)
        lo = sum(min(v[p] for v in U[q]) for q in U)
        hi = sum(max(v[p] for v in U[q]) for q in U)
        wyn.append((got - lo) / (hi - lo))
    return wyn

def pakiet(U, start):
    """Pakiet maksymalizujący zadowolenie najmniej zadowolonego profilu
    (przeszukiwanie lokalne: zmiana jednej odpowiedzi naraz)."""
    wyb = dict(start)
    klucz = lambda w: (round(min(zadowolenie(U, w)), 9), sum(zadowolenie(U, w)))
    lepiej = True
    while lepiej:
        lepiej = False
        for q in U:
            for i in range(len(U[q])):
                if i == wyb[q]:
                    continue
                proba = dict(wyb); proba[q] = i
                if klucz(proba) > klucz(wyb):
                    wyb, lepiej = proba, True
    return wyb

def losowy_swiat(rng):
    """Zaburzone oceny (±1 z prawd. 1/3 każde) i wagi profili (±50 %)."""
    pyt = {q: (t, [(e, [max(-2, min(2, s + rng.choice((-1, 0, 0, 0, 0, 1)))) for s in oc])
                   for e, oc in war]) for q, (t, war) in PYTANIA.items()}
    prof = {}
    for n, w in PROFILE.items():
        z = {k: v * rng.uniform(.5, 1.5) for k, v in w.items()}
        s = sum(z.values()); prof[n] = {k: v / s for k, v in z.items()}
    return tabela(pyt, prof)

def main():
    seed = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else 2026
    N = 4000
    rng = random.Random(seed)
    U = tabela()
    mm = {q: maximin(U[q]) for q in U}
    sr = {q: srednia(U[q]) for q in U}
    licz_mm = {q: [0] * len(U[q]) for q in U}
    licz_w = {q: [0] * len(U[q]) for q in U}
    for _ in range(N):
        V = losowy_swiat(rng)
        ud = [rng.gammavariate(1, 1) for _ in PROFILE]; s = sum(ud); ud = [x / s for x in ud]
        for q in V:
            licz_mm[q][maximin(V[q])] += 1
            licz_w[q][wiekszosc(V[q], ud)] += 1
    proj = {q: 0 for q in U if q <= 17}

    print(f"<!-- seed={seed}, N={N} -->\n")
    print("| Nr | Sprawa | Odpowiedź równowagi | Stabilność | Większość | Najmniej zyskuje | Ocena |")
    print("|---|---|---|---|---|---|---|")
    naz = list(PROFILE)
    oceny = {}
    for q, (t, war) in PYTANIA.items():
        i = mm[q]
        st = licz_mm[q][i] / N
        wi = max(range(len(war)), key=lambda k: licz_w[q][k]); wp = licz_w[q][wi] / N
        slaby = naz[min(range(len(naz)), key=lambda p: U[q][i][p])]
        if st >= .6 and wi == i:
            oc = "stabilna"
        elif st >= .6:
            oc = "spór: równowaga ≠ większość"
        elif wi == i:
            oc = "chwiejna"
        else:
            oc = "brak równowagi"
        oceny[q] = oc
        print(f"| {q} | {t} | {war[i][0]} | {st:.0%} | {war[wi][0]} ({wp:.0%}) | {slaby} | {oc} |")

    print("\n| Pakiet odpowiedzi | " + " | ".join(naz) + " | najniższe |")
    print("|---|" + "---|" * (len(naz) + 1))
    def wiersz(nazwa, wyb):
        z = zadowolenie(U, wyb)
        print(f"| {nazwa} | " + " | ".join(f"{x:.0%}" for x in z) + f" | **{min(z):.0%}** |")
    wyb_proj = dict(mm); wyb_proj.update(proj)
    wiersz("Projekt 2.0 w części A, równowaga w części B", wyb_proj)
    wiersz("Najwyższa średnia w każdym pytaniu", sr)
    wiersz("Równowaga w każdym pytaniu osobno", mm)
    pk = pakiet(U, mm)
    wiersz("Równowaga całego pakietu", pk)
    for n in naz:
        p = naz.index(n)
        wiersz(f"Wszystko po myśli profilu: {n}", {q: max(range(len(U[q])), key=lambda i: U[q][i][p]) for q in U})

    print("\nRóżnice: równowaga pakietu wobec równowagi pytanie po pytaniu:")
    for q in U:
        if pk[q] != mm[q]:
            print(f"- {q}. {PYTANIA[q][0]}: „{PYTANIA[q][1][mm[q]][0]}” → „{PYTANIA[q][1][pk[q]][0]}”")
    print("\nCzęść A — gdzie równowaga odbiega od projektu:")
    for q in proj:
        if mm[q] != 0:
            print(f"- {q}. {PYTANIA[q][0]}: projekt „{PYTANIA[q][1][0][0]}”, równowaga „{PYTANIA[q][1][mm[q]][0]}” ({oceny[q]})")

if __name__ == "__main__":
    main()

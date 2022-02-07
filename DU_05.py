#from DU5_def_zobrazeni import

# uzivatel vybira zobrazeni
print("""Vyberte si z následujících zobrazení a napiště příslušnou zkratku!
La = Lambertovo azimutální
Br = Braunovo válcové tečné
Pt = Ptolemaiovo kuželové
Sa = Sansonovo nepravé""")
# osetreni vstupu
while True:
    try:
        zobrazeni = str(input("Zadejte zkratku: "))
        if zobrazeni not in ["La", "Br", "Pt", "Sa"]:
            print("Špatně zadané zobrazení. Zkuste to znovu")
            continue
        # pri korektnim vstupu vyskoci z cyklu
        break
    except ValueError:
        print("Chybný vstup! Zadej znovu!")
        continue

# uzivatel zadava meritko
print("""Zadejte měřítko, ve kterém bude zobrazení vytvořeno!
Zadává se jako celé číslo x, které bude odpovídat 1:x """)
while True:
    # osetri nekorektni vstupy
    try:
        meritko = float(input("Zadejte měřítko: "))
        if meritko <= 0:
            print("Špatně zadané číslo. Zkuste to znovu.")
            continue
    # pri korektnim vstupu vyskoci z cyklu
        break
    except ValueError:
        print("Chybný vstup! Zadej znovu!")
        continue

# uzivatel zadava polomer
print("""Zadejte poloměr Země, se kterým chcete počítat. Zadejte celé číslo v km!
Pokud zadáte 0, bude počítáno s poloměrem 6371,11 km.""")

# osetreni spravneho vstupu a prevedeni polomeru na cm
while True:
    try:
        polomer = float(input("Zadejte poloměr: "))
        if polomer < 0:
            print("Příliš malé číslo. Zkuste to znovu.")
            continue
        # pokud je polomer = 0, promenne je prirazena konstanta
        elif polomer == 0:
            R = 6371.11 * 100000
        else:
            R = polomer * 100000
    except ValueError:
        print("Chybný vstup! Zadej znovu!")
        continue
    break
# vypocet daneho polomeru dle meritka a velikosti pixelu
R = R/meritko/0.03
#print(R)

# uzivatel zadava zemepisnou sirku a delku bodu
while True:
    try:
        d = float(input("Zadej zeměpisnou délku ve stupních: "))
        s = float(input("Zadej zeměpisnou šířku ve stupních: "))
        if abs(d) > 180:
            print("Tento úhel nelze použít, zkus menší")
            continue
        if abs(s) > 90:
            print("Tento úhel nelze použít, zkus menší")
            continue
    except ValueError:
        print("Chybný vstup. Zadej celé číslo!")
        continue
    break

# vypocet bodu a vykresleni site dle zadani uzivatele










         
        #SOUŘADNICE BODŮ - ZEMĚPISNÁ DÉLKA A ŠÍŘKA
      

from turtle import setpos, speed, penup, pendown, exitonclick, screensize
from math import sin, cos, tan, radians

# funkce pro vypocty souradnic zvoleneho bodu a vytvoreni zemepisnych siti pro vybrana zobrazeni
# funkce pro vypocet bodu v Postelove azimutálním zobrazení
# vypocet sirky
def Po_s(s, R):
    x = R*radians(90-s)
    return x

# vypocet delky
def Po_d(d):
    y = radians(d)
    return y

# vypocet bodu
def Po_bod(d, s, R):
    delka = Po_s(s, R)*cos(Po_d(d))
    sirka = Po_s(s, R)*sin(Po_d(d))
    return delka, sirka

# funkce pro vykresleni zemepisne site v Postelove azimutálním zobrazení
def Po(poledniky, rovnobezky, R):
    zs = range(-90,91, rovnobezky)
    zd = range(-180, 181, poledniky)
    speed(0)
    screensize(canvwidth=1200, canvheight=891)
    for j in zs:
        penup()
        setpos(Po_s(j,R)*cos(Po_d(-180)), Po_s(j,R)*sin(Po_d(-180)))
        pendown()
        for i in zd:
            setpos(Po_s(j,R)*cos(Po_d(i)), Po_s(j,R)*sin(Po_d(i)))
    for j in zd:
        penup()
        setpos(Po_s(-90,R)*cos(Po_d(j)), Po_s(-90,R)*sin(Po_d(j)))
        pendown()
        for i in zs:
            setpos(Po_s(i,R)*cos(Po_d(j)), Po_s(i,R)*sin(Po_d(j)))

# funkce pro vypocet bodu v Braunově válcovém tečném zobrazení
def Br_bod(d, s, R):
    delka = R*(radians(d))
    sirka = 2*R*tan(radians(s)/2)
    return delka, sirka

# funkce pro vykresleni zemepisne site v Braunově válcovém tečném zobrazení
def Br(poledniky, rovnobezky, R):
    zs = range(-90, 91, rovnobezky)
    zd = range(-180, 181, poledniky)
    speed(0)
    screensize(canvwidth=1200, canvheight=891)
    for j in zs:
        penup()
        setpos(R*radians(-180), 2*R*tan(radians(j)/2))
        pendown()
        for i in zd:
            setpos(R*radians(i), 2*R*tan(radians(j)/2))
    for j in zd:
        penup()
        setpos(R*radians(j), 2*R*tan(radians(-90)/2))
        pendown()
        for i in zs:
            setpos(R*radians(j), 2*R*tan(radians(i)/2))

# funkce pro vypocet bodu v Ptolemaiově kuželovém zobrazení
# vypocet sirky
def Pt_s(s, R):
    x = R*(1/tan(radians(30))) + R*(radians(30-s))
    return x

# vypocet delky
def Pt_d(d):
    y = radians(d)*sin(radians(30))
    return y

# vypocet bodu
def Pt_bod(d, s, R):
    delka = radians(30) - Pt_s(s, R)*cos(Pt_d(d))
    sirka = Pt_s(s, R)*sin(Pt_d(d))
    return delka, sirka

# funkce pro vykresleni zemepisne site v Ptolemaiově kuželovém zobrazení
def Pt(poledniky, rovnobezky, R):
    zs = range(-90, 91, rovnobezky)
    zd = range(-180, 181, poledniky)
    speed(0)
    screensize(canvwidth=1200, canvheight=891)
    for j in zs:
        penup()
        setpos(radians(30) - Pt_s(j, R)*cos(Pt_d(-180)), Pt_s(j, R)*sin(Pt_d(-180)))
        pendown()
        for i in zd:
            setpos(radians(30) - Pt_s(j, R)*cos(Pt_d(i)), Pt_s(j, R)*sin(Pt_d(i)))
    for j in zd:
        penup()
        setpos(radians(30) - Pt_s(-90, R)*cos(Pt_d(j)), Pt_s(-90, R)*sin(Pt_d(j)))
        pendown()
        for i in zs:
            setpos(radians(30) - Pt_s(i, R)*cos(Pt_d(j)), Pt_s(i, R)*sin(Pt_d(j)))

# funkce pro vypocet bodu v Sansonově nepravém zobrazení
def Sa_bod(d, s, R):
    delka = R*radians(d)*cos(radians(s))
    sirka = R*radians(s)
    return delka, sirka

# funkce pro vykresleni zemepisne site v Sansonově nepravém zobrazení
def Sa(poledniky, rovnobezky, R):
    zs = range(-90, 91, rovnobezky)
    zd = range(-180, 181, poledniky)
    speed(0)
    screensize(canvwidth=1200, canvheight=891)
    for j in zs:
        penup()
        setpos(R*radians(-180)*cos(radians(j)), R*radians(j))
        pendown()
        for i in zd:
            setpos(R*radians(i)*cos(radians(j)), R*radians(j))
    for j in zd:
        penup()
        setpos(R*radians(j)*cos(radians(-90)), R*radians(-90))
        pendown()
        for i in zs:
            setpos(R*radians(j)*cos(radians(i)), R*radians(i))

# cast pro zadavani parametru uzivatelem

# uzivatel vybira zobrazeni
print("""Vyberte si z následujících zobrazení a napiště příslušnou zkratku!
Po = Postelovo azimutální
Br = Braunovo válcové tečné
Pt = Ptolemaiovo kuželové
Sa = Sansonovo nepravé""")
# osetreni vstupu
while True:
    try:
        zobrazeni = str(input("Zadejte zkratku: "))
        if zobrazeni not in ["Po", "Br", "Pt", "Sa"]:
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
        meritko = int(input("Zadejte měřítko: "))
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
        polomer = int(input("Zadejte poloměr: "))
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
poledniky = 10
rovnobezky = 10

if zobrazeni == "Po":
    Po(poledniky, rovnobezky, R)
    delka, sirka = Po_bod(d, s, R)
elif zobrazeni == "Br":
    Br(poledniky, rovnobezky, R)
    delka, sirka = Br_bod(d, s, R)
elif zobrazeni == "Pt":
    Pt(poledniky, rovnobezky, R)
    delka, sirka = Pt_bod(d, s, R)
else:
    zobrazeni == "Sa"
    Sa(poledniky, rovnobezky, R)
    delka, sirka = Sa_bod(d, s, R)

exitonclick()

print("Zvolený bod má souřadnice x: ",delka, "a y: ",sirka)

from turtle import setpos, speed, penup, pendown, exitonclick, screensize, dot
from math import sin, cos, tan, radians

# funkce pro vypocty novych souradnic zvoleneho bodu a vytvoreni zemepisnych siti pro vybrana zobrazeni

# funkce pro vypocet v Postelove azimutálním zobrazení
# vypocet sirky
def Po_s(s, R):
    x = R*radians(90-s)
    return x

# vypocet delky
def Po_d(d):
    y = radians(d)
    return y

# vypocet novych souradnic
def Po_bod(y, x, R):
    delka = Po_s(x, R)*cos(Po_d(y))
    sirka = Po_s(x, R)*sin(Po_d(y))
    return delka, sirka

# vypocet a vykresleni bodu
def vykresli_Po_bod(d, s, R):
    bod = Po_bod(d, s, R)
    setpos(bod[0], bod[1])

# vykresleni zemepisne site
def Po(poledniky, rovnobezky, R):
    zs = range(-90,91, rovnobezky)
    zd = range(-180, 181, poledniky)
    for j in zs:
        penup()
        vykresli_Po_bod(j, -180, R)
        pendown()
        for i in zd:
            vykresli_Po_bod(j, i, R)
    for j in zd:
        penup()
        vykresli_Po_bod(-90, j, R)
        pendown()
        for i in zs:
            vykresli_Po_bod(i, j, R)

# funkce pro vypocet v Braunově válcovém tečném zobrazení
# vypocet novych souradnic
def Br_bod(d, s, R):
    delka = R*(radians(d))
    sirka = 2*R*tan(radians(s)/2)
    return delka, sirka

# vypocet a vykresleni bodu
def vykresli_Br_bod(d, s, R):
    bod = Br_bod(d, s, R)
    setpos(bod[0], bod[1])

# vykresleni zemepisne site
def Br(poledniky, rovnobezky, R):
    zs = range(-90, 91, rovnobezky)
    zd = range(-180, 181, poledniky)
    for j in zs:
        penup()
        vykresli_Br_bod(-180, j, R)
        pendown()
        for i in zd:
            vykresli_Br_bod(i, j, R)
    for j in zd:
        penup()
        vykresli_Br_bod(j, -90, R)
        pendown()
        for i in zs:
            vykresli_Br_bod(j, i, R)

# funkce pro vypocet v Ptolemaiově kuželovém zobrazení
# vypocet sirky
def Pt_s(s, R):
    x = R*(1/tan(radians(30))) + R*(radians(30-s))
    return x

# vypocet delky
def Pt_d(d):
    y = radians(d)*sin(radians(30))
    return y

# vypocet novych souradnic
def Pt_bod(y, x, R):
    delka = radians(30) - Pt_s(x, R)*cos(Pt_d(y))
    sirka = Pt_s(x, R)*sin(Pt_d(y))
    return delka, sirka

# vypocet a vykresleni bodu
def vykresli_Pt_bod(y, x, R):
    bod = Pt_bod(y, x, R)
    setpos(bod[0], bod[1])
    
# vykresleni zemepisne site
def Pt(poledniky, rovnobezky, R):
    zs = range(-90, 91, rovnobezky)
    zd = range(-180, 181, poledniky)
    for j in zd:
        penup()
        vykresli_Pt_bod(-180, j, R)
        pendown()
        for i in zs:
            vykresli_Pt_bod(i, j, R)
    for j in zs:
        penup()
        vykresli_Pt_bod(-90, j, R)
        pendown()
        for i in zd:
            vykresli_Pt_bod(i, j, R)

# funkce pro vypocet v Sansonově nepravém zobrazení
# vypocet novych souradnic 
def Sa_bod(d, s, R):
    delka = R*radians(d)*cos(radians(s))
    sirka = R*radians(s)
    return delka, sirka

# vypocet a vykresleni bodu
def vykresli_Sa_bod(d, s, R):
    bod = Sa_bod(d, s, R)
    setpos(bod[0], bod[1])
        
# vykresleni zemepisne site
def Sa(poledniky, rovnobezky, R):
    zs = range(-90, 91, rovnobezky)
    zd = range(-180, 181, poledniky)
    for j in zs:
        penup()
        vykresli_Sa_bod(-180, j, R)
        pendown()
        for i in zd:
            vykresli_Sa_bod(i, j, R)
    for j in zd:
        penup()
        vykresli_Sa_bod(j, -90, R)
        pendown()
        for i in zs:
            vykresli_Sa_bod(j, i, R)

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

speed(0)
screensize(canvwidth = 1200, canvheight = 891)

if zobrazeni == "Po":
    Po(poledniky, rovnobezky, R)
    delka, sirka = Po_bod(d, s, R)
elif zobrazeni == "Br":
    Br(poledniky, rovnobezky, R)
    delka, sirka = Br_bod(d, s, R)
elif zobrazeni == "Pt":
    Pt(poledniky, rovnobezky, R)
    delka, sirka = Pt_bod(d, s, R)
elif zobrazeni == "Sa":
    Sa(poledniky, rovnobezky, R)
    delka, sirka = Sa_bod(d, s, R)

exitonclick()

print("Zvolený bod má souřadnice x: ", round(delka, 3), "a y: ", round(sirka, 3))
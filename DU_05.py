#from DU5_def_zobrazeni import

# uzivatel vybira zobrazeni
print("""Vyberte si z následujících zobrazení a napiště příslušnou zkratku!
La = Lambertovo azimutální
Br = Braunovo válcové tečné
Pt = Ptolemaiovo kuželové
Sa = Sansonovo nepravé""")
zobrazeni = input("Zadejte zkratku: ")
# osetreni vstupu

if zobrazeni in ["La", "Br", "Pt", "Sa"]:
    print("Vybrali jste", zobrazeni)
else:
    ("Špatně zadané zobrazení. Zkuste to znovu")
    zobrazeni = input("Zadejte zkratku: ")

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



#INPUT - HODNOTY ZOBRAZENÍ - La, Br, Pt, Sa
        #MĚŘÍTKO
        #SOUŘADNICE BODŮ - ZEMĚPISNÁ DÉLKA A ŠÍŘKA
        #POLOMĚR ZEMĚ


# DU_05
repozitar pro ukol 5

Co program dělá?

Tento program umožňuje uživateli z nabídky zvolit zobrazení, zadat měřítko a poloměr pro vykreslení sítě a vypsání souřadnic zadaného bodu. K výběru je vždy jedno zobrazení z azimutálního, válcového tečného, kuželového a nepravého. Nakonec je síť vykreslena pomocí želví grafiky.

Vstupní parametry

Nejprve je uživatel vyzván k výběru zobrazení.
Vybírá z následujících: 
Po = Postelovo azimutální
Br = Braunovo válcové tečné
Pt = Ptolemaiovo kuželové
Sa = Sansonovo nepravé

Následně uživatel zadává měřítko.
Zadává celé číslo, větší než 0, jinak je vyzván k opakovanému zadání správného vstupu. 

Uživatel má možnost zvolit i vlastní poloměr Země (zadává celé číslo větší než 0 - jinak je vyzván k opakování) nebo zvolí hodnotu 0 a bude počítáno se skutečným poloměrem Země 6371,11 km.

Naposledy uživatel zadává zeměpisnou délku a šířku libovolného bodu.
Zadává celé nebo desetinné číslo v rozmezí 0 - 180 pro zeměpisnou délku 0 - 90 pro zeměpisnou šířku. 

Výstup

Program vykreslí síť ve zvoleném geografickém zobrazení pomocí modulu turtle a vypíše hodnoty x a y pro zvolený bod. 
Modul turtle je nstaven tak, že po vykreslení sítě stačí kliknout na otevřené okno a zavře se.

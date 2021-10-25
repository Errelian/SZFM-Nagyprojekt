# Discord Bot követelmény specifikáció

## 1 Jelenlegi Helyzet

A JózsefJónás Discord-szerver számtalan felhasználóval rendelkezik, akik gyakran ismerkedés érdekében különböző játékokat szeretnének játszani egymással, de a jelenleg ezt csak harmadik féltől származó oldalakon, és alkalmazások segítségével tudják megvalósítani. Ez jelentősen megnehezíti a pontszámok esetleges nyilvántartását, és az esetleges alkalmazás váltások erősen lelassítják az egész folyamatot.

Felméréseink szerint, ezen okokból sokat esik a felhasználói elégedettség a felhasználóink szavait idézve természetesen.

Jelenleg a leggyakrabban játszott, legnépszerűbb játékok:
  * Sakk
  * Amőba (3x3, 5x5)

## 2 Vágyott Helyzet

A JózsefJónás Discord-szerver számtalan felhasználója a szerverre integrált ún. "Bot"-on keresztül játszanák le a játékaikat. Ezen a boton keresztül a felhasználók letudnák bonyolítani a játékaikat, a bot egyértelműen eldöntené a győztest, és a győztest félt egy profilhoz kötné, ezzel megakadályozva a csalást.

## 3 Jelenlegi üzleti folyamatok

### 3.1 Játék kezdeményezés

Két ismerkedő felhasználónk szeretne közösön játszani egy játékot -> Felkeresnek egy külső alkalmazást vagy oldalt amely biztosítja ezen játékot -> A felhasználók regisztrálnak és/vagy letöltik az alkalmazást. -> Lejátsszák a kívánt játékot. -> A felhasználó kevésbe kötődik a JózsefJónás szerverhez.

## 4 Igényelt üzleti folyamat

### 4.1 Játék kezdeményezés

Két ismerkedő felhasználónk szeretne közösön játszani egy játékot -> Chat-paranccsal meghívják a szerver által hostolt Bot-ot. -> Lejátsszák a játékot, amit a Bot levezet. ->A felhasználó jobban kötődik a szerverhez.

## 5 A Rendszerre vonatkozó szabályok

A Bot fusson a Discord chat-alkalmazás szerverein.

A Bot képes legyen grafikusan megjeleníteni a játék állapotát.

A grafikus felület legyen esztétikus.

A Bot használjon viszonylag kevés erőforrást.

A Bot képes legyen gépi ellenfélként játszani a legegyszerűbb játékokat.

A Bot működjön a JózsefJónás Discord-szerver hálózat bármely szerverén.

## 6 Követelménylista

[K01] Specifikus szerver-függetlenség.

[K02] Erőforrás-hatékonyság.

[K03] Könnyű kezelhetőség.

[K04] Fair levezetés.

[K05] Szabályos levezetés.

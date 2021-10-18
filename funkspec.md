## 1. Jelenlegi helyzet

A JózsefJónás Discord-szerver felhasználói jelenleg csak harmadik féltől származó játékokat tudnak igénybe venni. Ezek gyakran addicionális regisztrációhoz kötöttek, és előfordul, hogy egy kedvelt játékot hostoló szerver ideiglenesen, vagy véglegesen nem elérhető. A felhasználók számára fontos, hogy a játékok eredményei naplózva is legyenek, melyeket könnyen el szeretnének érni. Ezentúl fontos még a lehető legmagasabb rendelkezésre állás biztosítása is.

## 2. Vágyott rendszer

A JózsefJónás Discord-szerver tagjainak célja, hogy az összes tag számára hozzáférhető legyen egy olyan integrált megoldás, melynek segítségével könnyen, átirányításoktól és regisztrációktól mentesen játszhatnak egymás ellen.

A bot legyen felhasználóbarát, egyszerű parancsokkal kezelhető. Alapvető feltétel, a könnyebb játszhatóság, és nagyobb mértékű interakció eléréséhez, hogy a játék ún. "emote"-okkal irányítható lehessen.


## 3. Jelenlegi üzleti folyamatok

### 3.1 Játék kezdeményezés

A JózsefJónás Discord-szerver két tagja megbeszélik közösen, hogy milyen játékot szeretnének játszani. Ha a szerveren még nem elérhető az adott játék, akkor egyéb, külső forrásból beszerzik azt, majd lejátsszák az adott játékot. Ekkor a legtöbb esetben már nem a szerver szolgáltatásain keresztül történik a köztük lévő kommunikáció, aminek következtében csökken a szerveraktivitás, a tagok kevésbé kötődnek a szerverhez, illetve a leendő tagok számára kevésbé lesz vonzó a szerverhez való csatlakozás.

## 4. Igényelt üzleti folyamatok

###4.1 Játék kezdeményezése és folyamata

Két felhasználó eldönti, hogy szeretne közösen játszani egy játékot. -> Chat-paranccsal meghívják a server által hostolt játék-botot -> Lejátsszák a játékot, a játék-bot levezeti, új játékosoknak segít a megértésben -> Az eredményt a játék-bot eltárolja, utólag így visszanézhető és összehasonlítható. -> A felhasználó jobban élvezi a szervert, több időt tölt itt, jobban kötődik.


## 5. Rendszerre vonatkozó szabályok

A Bot fusson a Discord chat-alkalmazás szerverein.

A Bot képes legyen grafikusan megjeleníteni a játék állapotát.

A grafikus felület legyen esztétikus.

A Bot használjon viszonylag kevés erőforrást.

A Bot képes legyen gépi ellenfélként játszani a legegyszerűbb játékokat.

A Bot működjön a JózsefJónás discord-szerver hálózat bármely szerverén.


## 6. Követelménylista

A Bot a Discord-szerver által legyen hostolva.

A Bot ne igényeljen külön letöltést, csak meghívást a szerverre.

A Bot használjon viszonylag kevés erőforrást.

A Bot használata legyen egyértelmű és egyszerű.

A Bot a játékok levezetése során kövesse a megadott szabályrendszert, működése legyen megbízható.

A Bot az eredményeket megbízhatóan és pontosan tárolja.

A Bot gépi ellenfélként is tudjon viselkedni, ha szükséges.


## 7. Használati esetek

A szerver tagjai minden olyan esetben meghívhatják a botot, amikor baráti mérkőzést szeretnének játszani társaikkal. Esetenként, amennyiben több felhasználó is jelentkezik, versenyt indíthatnak melynek végén egyetlen győztes felhasználó kerül feljegyzésre a ranglistában.

## 8. Képernyőtervek

(hogyan fog kinézni? sketch/html mockup)

## 9.Forgatókönyvek

A Discord szerver tagjai igényük szerint hívhatják meg a botot, az erre megfelelő parancs segítségével. Az adott játék kiválasztása a "/" karakter után írt paranccsal történik. pl.:
```
/chess
```
```
/tic-tac-toe
```

 Ekkor a kiválasztott ellenfél játékos értesítést kap, hogy meghívták egy mérkőzésre. Amennyiben elfogadja, megkezdődik a játék. Sakk esetében a kezdőjátékos találomra kerül kisorsolásra.

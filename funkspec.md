## 1. Jelenlegi helyzet

A JózsefJónás Discord-szerver felhasználói jelenleg csak harmadik féltől származó játékokat tudnak igénybe venni. Ezek gyakran addicionális regisztrációhoz kötöttek, és előfordul, hogy egy kedvelt játékot hostoló szerver ideiglenesen, vagy véglegesen nem elérhető. A felhasználók számára fontos, hogy a játékok eredményei naplózva is legyenek, melyeket könnyen el szeretnének érni. Ezentúl fontos még a lehető legmagasabb rendelkezésre állás biztosítása is.

## 2. Vágyott rendszer

<<<<<<< Updated upstream
A JózsefJónás Discord-szerver tagjainak célja, hogy az összes tag számára hozzáférhető legyen egy olyan integrált megoldás, melynek segítségével könnyen, átirányításoktól és regisztrációktól mentesen játszhatnak egymás ellen.
=======
A JózsefJónás Discord-szerver tulajdonosainak és tagjainak célja, hogy az összes tag számára hozzáférhető legyen egy olyan szerver-integrált megoldás (ezentúl ún. "Bot"), melyek egy lényegesen áramvonalasabb folyamattá teszik a mérkőzések szervezését és lebonyolítását. 
Szeretnénk ha a Bot egyszerűen meghívható lenne a szerverre, ott egyszerű, és könnyen megjegyezhető parancsokkal elindítana és játékot, aminek a végén egyértelműen eldöntené a győztest és a két játékos profiljához kötné az eredményt. A bot ezen túl játékra lebontva tárolná minden játékos eredményeit, melyeket összehasonlítás, visszatekintés céljából könnyen el lehessen érni utólag és bármikor. 
A bot legyen felhasználóbarát, egyszerű parancsokkal kezelhető. Alapvető feltétel, a könnyebb játszhatóság, és nagyobb mértékű interakció eléréséhez, hogy a játék ún. "emote"-okkal irányítható lehessen.
Mind a felhasználóknak, mind a szerver tulajdonosainak fontos a lehető legmagasabb rendelkezésre állás biztosítása, ami magába foglalja, hogy a szerver (és ezáltal a Bot) mindig elérhető legyen, fusson; az eredmények mindig lekérdezhetők legyenek; más szerverekre is bármikor meghívható legyen.
>>>>>>> Stashed changes

A bot legyen felhasználóbarát, egyszerű parancsokkal kezelhető. Alapvető feltétel, a könnyebb játszhatóság, és nagyobb mértékű interakció eléréséhez, hogy a játék ún. "emote"-okkal irányítható lehessen.


## 3. Jelenlegi üzleti folyamatok

### 3.1 Játék kezdeményezés

<<<<<<< Updated upstream
A JózsefJónás Discord-szerver két tagja megbeszéli közösen, hogy milyen játékot szeretnének játszani. Ha a szerveren még nem elérhető az adott játék, akkor egyéb, külső forrásból beszerzik azt - ez általában egy külső alkalmazás, vagy egy weboldal. Ezek után lejátsszák az általuk áhított meccse\(ke\)t.
=======
A JózsefJónás Discord-szerver két tagja megbeszélik közösen, hogy szeretnének játszani egy mérkőzést. -> 

Eldöntik, hogy milyen játékot szeretnének játszani. ->

Megkeresik, hogy az adott játék milyen platformon (web-, vagy asztali alkalmazás) elérhető. ->

A két játékos időközben kénytelen a játék idejére elhagyni a szervert, hisz a játékot csak külső "helyszínen" tudják lejátszani.
Ekkor a legtöbb esetben már nem a szerver szolgáltatásain keresztül történik a köztük lévő kommunikáció, hanem magánbeszélgetést folytatnak. ->

A felhasználók regisztrálnak és/vagy letöltik az alkalmazást. ->

Lejátsszák a kiválasztott játékot. ->

A játék befejeztével a játék eredménye nem kerül lokálisan elmentésre, az eredmény lényegében elveszett. ->

A felhasználó összességében kevésbé kötődik a JózsefJónás szerverhez ->

Mindennek következtében csökken a szerveraktivitás, hiszen nem a szerveren belül folyik a játék és a kommunikáció, így a többi tag egyfelől kimarad a közös játékélményből, másrészt az esetek többségében nem alakul ki beszélgetés, amelynek az apropója az adott játék lenne. Mivel nem annyira kötődik, nem fog hívni új tagokat, így nem csak a jelenlegi tagok kötődése csökken, a szerver növekedése sem történik meg, a leendő tagok számára kevésbé lesz vonzó a szerverhez való csatlakozás, hiszen alacsony lesz a szerveraktivitás.
>>>>>>> Stashed changes

Ekkor a legtöbb esetben már nem a szerver szolgáltatásain keresztül történik a köztük lévő kommunikáció, hanem magánbeszélgetést folytatnak.
Ennek következtében csökken a szerveraktivitás, hiszen nem a szerveren belül folyik a játék és a kommunikáció, így a többi tag egyfelől kimarad a közös játékélményből, másrészt az esetek többségében nem alakul ki beszélgetés, amelynek az apropója az adott játék lenne.
Mindemellett a tagok kevésbé kötődnek a szerverhez, hiszen kevesebb időt töltenek ott, illetve a leendő tagok számára kevésbé lesz vonzó a szerverhez való csatlakozás, hiszen alacsony lesz a szerveraktivitás.

## 4. Igényelt üzleti folyamatok

(ugyan az mint a kövspec csak a kivitelező szemszögéből)


## 5. Rendszerre vonatkozó szabályok

<<<<<<< Updated upstream
(ugyan az mint a kövspec csak a kivitelező szemszögéből)
=======
A Bot fusson a Discord chat-alkalmazás szerverein.

A Bot legyen a szerver tulajdonosa által egyszerűen meghívható.

A Bot adjon a felhasználóknak támpontokat az egyszerű parancsos használathoz.

A Bot képes legyen grafikusan megjeleníteni a játék állapotát minden lépést követően.

A grafikus felület legyen esztétikus, és könnyen értelmezhető.

A Bot használjon viszonylag kevés erőforrást.

A Bot képes legyen gépi ellenfélként játszani a legegyszerűbb játékokat.

A Bot működjön a JózsefJónás Discord-szerver hálózat bármely szerverén.
>>>>>>> Stashed changes


## 6. Követelménylista

(ugyan az mint a kövspec csak a kivitelező szemszögéből)


## 7. Használati esetek

A szerver tagjai minden olyan esetben meghívhatják a botot, amikor baráti mérkőzést szeretnének játszani társaikkal. Esetenként, amennyiben több felhasználó is jelentkezik, versenyt indíthatnak melynek végén egyetlen győztes felhasználó kerül feljegyzésre a ranglistában.

## 8. Képernyőtervek

![Képernyőterv](/img/discord_bot_sketch.png)

## 9.Forgatókönyvek

A Discord szerver tagjai igényük szerint hívhatják meg a botot, az erre megfelelő parancs segítségével. Ekkor a kiválasztott ellenfél játékos értesítést kap, hogy meghívták egy mérkőzésre.

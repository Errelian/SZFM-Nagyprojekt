## 1. Jelenlegi helyzet

A JózsefJónás Discord-szerver felhasználói jelenleg csak harmadik féltől származó játékokat tudnak igénybe venni amikor egymás ellen, vagy éppen szerverszintű versenyeken kívánnak megmérkőzni. Ezek gyakran addicionális regisztrációhoz, illetve gyakran az alkalmazás asztali-programként letöltéséhez kötöttek, ez extra hálózati forgalmat generál, lassítja a megnyitást, megnehezíti a mérkőzések összeszervezését már a legelejétől fogva, sőt a reklámok miatt a felhasználói élmény még tovább csorbul. A felmérések szerinti két legnépszerűbb játék a sakk és az amőba, és előfordul hogy a játékosok a két játék között szeretnének váltani, ami viszont az előbb taglalt okokból kifolyólag nem egy felhasználóbarát folyamat.
Előfordul, hogy egy kedvelt játékot hostoló szerver ideiglenesen, vagy véglegesen elérhetetlenné válik, így a megszokott, rendszeresen játszott játékok szervezése nem lehetséges. 
A külső szolgáltatók túlnyomó része a naplózást nem oldotta meg, ezért a lejátszott mérkőzések eredményeinek visszanézése, és a tagok egyéni eredményeinek összegzése nem lehetséges. 

## 2. Vágyott rendszer

A JózsefJónás Discord-szerver tulajdonosainak és tagjainak célja, hogy az összes tag számára hozzáférhető legyen egy olyan szerver-integrált megoldás (ezentúl ún. "Bot"), melyek egy lényegesen áramvonalasabb folyamattá teszik a mérkőzések szervezését és lebonyolítását. 
Szeretnénk ha a Bot egyszerűen meghívható lenne a szerverre, ott egyszerű, és könnyen megjegyezhető parancsokkal elindítana és játékot, aminek a végén egyértelműen eldöntené a győztest és a két játékos profiljához kötné az eredményt. A bot ezen túl játékra lebontva tárolná minden játékos eredményeit, melyeket összehasonlítás, visszatekintés céljából könnyen el lehessen érni utólag és bármikor. 
A bot legyen felhasználóbarát, egyszerű parancsokkal kezelhető. Alapvető feltétel, a könnyebb játszhatóság, és nagyobb mértékű interakció eléréséhez, hogy a játék ún. "emote"-okkal irányítható lehessen.
Mind a felhasználóknak, mind a szerver tulajdonosainak fontos a lehető legmagasabb rendelkezésre állás biztosítása, ami magába foglalja, hogy a szerver (és ezáltal a Bot) mindig elérhető legyen, fusson; az eredmények mindig lekérdezhetők legyenek; más szerverekre is bármikor meghívható legyen.

A bot legyen felhasználóbarát, egyszerű parancsokkal kezelhető. Alapvető feltétel, a könnyebb játszhatóság, és nagyobb mértékű interakció eléréséhez, hogy a játék ún. "emote"-okkal irányítható lehessen.
Mind a felhasználóknak, mind a szerver tulajdonosainak fontos a lehető legmagasabb rendelkezésre állás biztosítása, ami magába foglalja, hogy a szerver (és ezáltal a Bot) mindig elérhető legyen, fusson; az eredmények mindig lekérdezhetőek legyenek; más szerverekre is bármikor meghívható legyen.

A vágyott, automatizált játékok:
  * Sakk
  * Amőba (3x3, 5x5)


## 3. Jelenlegi üzleti folyamatok

### 3.1 Játék kezdeményezés

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


## 4. Igényelt üzleti folyamatok

### 4.1 Játék kezdeményezése és folyamata

A JózsefJónás Discord-szerver két tagja megbeszélik közösen, hogy szeretnének játszani egy mérkőzést. -> 

Eldöntik, hogy milyen játékot szeretnének játszani. ->

Egyszerű chat-paranccsal meghívják a szerver által hostolt Botot ->

A Bot vezetésével, egyszerű parancsokkal irányítva, lejátsszák a játékot. ->

A Bot a győztes kihirdetése után lementi a végeredményt, a két játékos profiljához köti azt. ->

A játékosok élvezik az egyszerű folyamatot, jobban kötődnek a szerverhez. ->

A felhasználó meghívja a barátait is, a szerver növekszik.

## 5. Rendszerre vonatkozó szabályok

A Bot fusson a Discord chat-alkalmazás szerverein.

A Bot legyen a szerver tulajdonosa által egyszerűen meghívható.

A Bot adjon a felhasználóknak támpontokat az egyszerű parancsos használathoz.

A Bot képes legyen grafikusan megjeleníteni a játék állapotát minden lépést követően.

A grafikus felület legyen esztétikus, és könnyen értelmezhető.

A Bot használjon viszonylag kevés erőforrást.

A Bot képes legyen gépi ellenfélként játszani a legegyszerűbb játékokat.

A Bot működjön a JózsefJónás Discord-szerver hálózat bármely szerverén.


## 6. Követelménylista

A Bot a Discord-szerver által legyen hostolva.

A Bot ne igényeljen külön letöltést, csak meghívást a szerverre.

A Bot használjon viszonylag kevés erőforrást.

A Bot használata legyen egyértelmű és egyszerű.

A Bot a játékok levezetése során kövesse a megadott szabályrendszert, működése legyen megbízható.

A Bot az eredményeket megbízhatóan és pontosan tárolja.

A Bot gépi ellenfélként is tudjon viselkedni, ha szükséges.


## 7. Használati esetek

A szerver tagjai minden olyan esetben meghívhatják a botot, amikor baráti mérkőzést szeretnének játszani társaikkal. Esetenként, amennyiben kettőnél több felhasználó is jelentkezik egyidőben a játékra, versenyt indíthatnak. A verseny több kétszemélyes mérkőzésből áll, melynek végén egyetlen győztes felhasználó kerül feljegyzésre a ranglistában, az ő profiljához lesz hozzáadva a győzelem.

## 8. Képernyőtervek

![Képernyőterv](/img/discord_bot_sketch.png)

## 9.Forgatókönyvek

A Discord szerver tagjai igényük szerint hívhatják meg a botot, az erre megfelelő parancs segítségével. Az adott játék kiválasztása a "/" karakter után írt paranccsal történik. pl.:
```
/chess
```
```
/tic-tac-toe
```

 Ekkor a kiválasztott ellenfél játékos értesítést kap, hogy meghívták egy mérkőzésre ezt elfogadhatja vagy elutasíthatja. Amennyiben elfogadja, megkezdődik a játék. Sakk esetében a kezdőjátékos találomra kerül kisorsolásra.

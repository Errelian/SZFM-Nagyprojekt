# Discord Bot rendszerterv

## 1. A rendszer célja

A Discord játékbot a harmadik fél, illetve külső alkalmazásoktól való függést hivatott felváltani az esetleges játékok keretében.
Ezáltal nincs szüksége a felhasználóknak külső oldalakra regisztrálni mivel a naplózások direkt a felhasználókhoz kötődnek,
amiket bármikor meg lehet tekinteni és nem kell tartani a külső játékokat hostoló szerverek ideiglenes vagy végleges megszünésétől. 

## 2. A projekt terve

A fejlesztők csapata öt személyből áll, mindenki saját felelőségekkel rendelkezik:
* Vas Ruben Levente
* Somogyi Viktória
* Görög Balázs
* Pintér Balázs
* Béres Dániel Csaba

A fejlesztők csapata a saját, általuk biztosított gépeken fogják végezni a fejlesztést

### 2.1 Mérföldkövek

[01] Feladatok kiosztása, szerepek meghatározása.

[02] A Discord Bot UI/kezelőfelületének megtervezése.

[03] A Discdord Bot funkciónak implementációja.

[04] A Discord Bot integrációja a szerverhez.

[05] A Discord Bot megfelelő mértékű tesztelése a kívánt környezetekben.

### 2.2 Ütemterv

1: [01] Elérése, ez egy közös megbeszélés útján történik meg.

2: [02] Elérése, ez közös megegyezése útján valósul meg.

3: [03] Elérése, a Backend fejlesztők felelőssége.

4: [04] Elérése, ez a fejlesztők közös munkáján keresztül valósul meg, amit egy közös megbeszélés előz meg.

5  [05] Elérése, ami a Tesztelő felelőssége, megvalósítása meg a különböző Discord szervereken keresztüli teszteléssel valósul meg.

## 3. Modell az üzleti folyamatokhoz

### 3.1.1. Szereplők:
 * Discord Felhasználó

### 3.1.2. Erőforrások:
 * Bármilyen eszköz, amely képes a Discord alkalmazás futtatására.
 * Szervergép
 * Hálózati kapcsolat

### 3.1.3. Bemenetek:
 * Parancsok
 * Emote-ok

### 3.1.4. Entitások:
 * Discord Bot

### 3.1.5. Kimenet:
 * Játékállás
 * Leíró adatok

### 3.1.6. Folyamat:

Egy Discord felhasználó játszani szeretne egy közösségi Discord szerveren -> Paranccsal meghívja a kívánt Bot-ot -> A Bot leellenőrzi, hogy az adott felhasználó már játákban van-e.

Ha igen: akkor nem léphet új játékba.

Ha, nem: Új játékba lép a felhasználó -> Befolyásolhatja a játékot paranccsal, vagy emote-tal -> Nyerhet, vagy fel is adhatja a játékot a megfelelő bevitel segítségével -> Véget ér a játék -> Az eredmény és a felhasználó adatai a játék szempontjából naplzásra kerül késöbbi megtekintésre.

### 3.1.7: Folyamatábra:

![Folyamatábra](/img/rendterv_folyamatabra.png)

### 3.1.8: Példa:

Egy Discord felhasználó szeretne egyett sakkozni, a Magyar Sakkszüvettség Discord szerverén. Meghívja egy paranccsal a Bot-ot, és ha még nincs játákéban egy új játékpartiba fog kerülni. Emote-ok segítségével mozgatja a felhasználó a bábuit majd ügyesen megnyeri a partit. Ezek után a felhasználó adataihoz kapcsolódóan a Bot naplózza a játék kimenetelét.  

## 4. Követelmények

Az előző dokumentumok követelményeinek magyarázata.

# [K01] Specifikus szerver-függetlenség

A bot, Discord-szervertől függetlenül, képes ellátni a feladatait. 

# [K02] Erőforrás-hatékonyság

A bot kis erőforrás-igényű, letisztult és a folyamtok mögötti számítási folyamatok optimalizáltak. 

# [K03] Könnyű kezelhetőség

A bot megjelenése letisztult, használata egyszerű, csak olyan funkciókat tartalmaz, ami szükséges a játékok lebonyolítására és azok naplzásaa.

# [K04] Fair levezetés

A bot mögötti működési és naplózási folyamatok szabályosak és teszteltek, így garantálható a kivételezés nélküliség és a csalás.

# [K05] Szabályos levezetés

A bot mögötti levezetési folyamatok szabályosak és teszteltek, így garantálható a szabályos játék.


## 5. Funkcionális terv

### 5.1. Az elkészítendő rendszer tulajdonságai


### 5.2. Rendszerszereplők
(mik vannak a rendszerben?)

### 5.2. Rendszerhasználati esetek és lefutásaik

#### 5.2.1. Számrendszer-átalakítás

##### 5.2.1.1. A Funkcionalitás leírása

##### 5.2.1.2. Példa lefutás/Használati eset

Életbeli példa arról hogy 5.2.1.1 hogy történik.


## 6. Fizikai környezet

A projekt megvalósítási szempontból egy Discord-bot, ami azt jelenti hogy szükséges hozzá egy állandó host. Ezt a projekt fejlesztési fázisában nagy valószínűséggel egy lokális gép lesz, viszont az üzemeltetési fázisban ez erősen lehetséges hogy a Cloud-on keresztül lesz megvalósítva. Erre több ok is van, mint például a projekt alacsony erőforrás-igénye és 24/7 elérhetőségi szükséglete.

* A kliens által biztosított eszközök:
    - Discord-szerver
* Fejlesztők által használt eszközök, technológiák:
    - Git
    - Visual Studio Code
    - Microsoft Paint
    - PyCharm IDE
* Tesztelt környezetek:
    - Asztali Discord alkalmazás
    - Mobilos Discord alkalmazás
    - Webes Discord oldal
* Futási környezetek:
    - Lokális gép
    - Microsoft Azure/Amazon EC2 (lehetséges, a jövőben)


## 7. Absztrakt domain modell

A rendszer megjelenítését a Discord-alkalmazás beépített formázási, képmegjelenítési eszközein keresztül valósul meg.


![Domain modell gráf](/img/domainmodell.png)


## 8. Architekturális terv

A rendszer architektúrája nagyon egyszerű, ami az ADM-ből is látszik: Mindössze két réteget kezel a projekt.

Első réteg: A discord-oldali réteg, ez kezeli a bementek gyújtését, a kimenetek megjelenítését, és összeségében a felhasználóval való kommunikációt.ű

Második-réteg: A Backend réteg, ez kezeli a játék-logikákat, az adatbázis kezelését, és persze a frontend-el való kommunikációt. 

Ezen rétegek közötti kapcsolatok leolvashatóak az ADM-ből.

## 9. Adatbázisterv

A projekt rendelkezni fog egy alapszintű adatbázissal, ami tárolni fogja a felhasználók hány éles játékot játszottak, ki elllen, és azoknak a kimenetelét.

Az adatbázis egy táblával fog rendelkezni:

* Lesz egy játékos adattábla, amely tárolni fogja az összes játékos adatatait egy-egy sorban: Milyen jáékból, hány mérkőzést játszottek, ebből hány nyert, döntetlen, és vesztett volt.

## 10. Implementációs terv

(az osztályok és köztük lévő kapcsolatok)

## 11. Teszt tervek


## 12. Telepítési tervezet

(hogyan kell telepíteni?)

## 13. Karbantartási tervezet

(hogyan fogjuk működésben tartani?)

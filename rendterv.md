# Számrendszer átalakító rendszerterv

## 1. A rendszer célja

(mit, miért)

## 2. A projekt terve

(kik, mit, és hogyan csinálnak?)

### 2.1 Mérföldkövek

(mik a nagy mérföldkövei a projektnek?)

### 2.2 Ütemterv

(milyen sorrendben akarjuk a mérföldköveket?)

## 3. Modell az üzleti folyamatokhoz

### 3.1.1. Szereplők:
 (kik használják?)

### 3.1.2. Erőforrások:
 (miket használ?)

### 3.1.3. Bemenetek:
 

### 3.1.4. Entitások:
 (a bot)

### 3.1.5. Kimenet:
 
### 3.1.6. Folyamat:

(hogyan használjá?)

### 3.1.7: Folyamatábra:

(folyamatábra)

### 3.1.8: Példa:

(példa)

## 4. Követelmények

(Az előző dokumentumok követelményeinek magyarázata.) 


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

(mi mire alapszik, hova küld dolgokat?)

## 9. Adatbázisterv

(lesz-e adatbázis, és ha igen, milyen?)

## 10. Implementációs terv

(az osztályok és köztük lévő kapcsolatok)


## 11. Teszt tervek


## 12. Telepítési tervezet

(hogyan kell telepíteni?)

## 13. Karbantartási tervezet

(hogyan fogjuk működésben tartani?)
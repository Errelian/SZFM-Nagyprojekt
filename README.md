# SZFM-Nagyprojekt-Discord-bot

## Rövid-leírás

Ez a Szoftverfejlesztési módszertanok órára készült 8 hetes nagyprojekt. Tartalma egy Discord-bot, amit akármelyik szerverre meghívva, egyszerű parancsokkal játszmákat rendezhetünk sakk és amőba játékokban kétszemélyes játékmódokkal.   
Python programozási nyelvben íródott, mert talán az áll legközelebb a Discordhoz.  
Jövőbeli célok között van az amőbához egy AI implementálása, aminek köszönhetően egyszemélyes módban is lehet játszani, de ez időszűkében még nem lett kiötölve és megírva.
  
  
  
  
## A Bot működése


### A Bot meghívása

Bármelyik szerverre meghívható a bot, mindössze annyira van szükség, hogy a szerver tulajdonosa vagy egy adminisztrátora a Discordra bejelentkezzen böngészőből, és a böngésző URL-sávjába másolja a következő linket: LINK  
  
Az itt megnyíló oldalon kiválasztja, hogy (ha több szerveren is vannak adminisztrátori vagy tulajdonosi jogai) melyik szerverhez kívánja meghívni a botot. Ezután az Engedélyezés(/Authorize) gombra nyom, és kész is, a bot már a szerveren fut és használható a megfelelő parancsokkal, de azért javasolt ellenőrizni, hogy a tagok listáján látjuk e a botot (név alapján, de külön BOT szimbolumot is kap a neve mellé). 

### A Bot használata
A Bot parancsokkal irányítható, amiknek a listáját a *!help* paranccsal kapjuk meg, vagyis a következőket:

*!author* - a bot szerzői csapatáról ad egy rövid összefoglalót.

*!info* - A Botról magáról ad vissza információt, röviden összefoglalja hogyan lehet elindítani a lehetséges játékokat.

*!chessInfo* - A sakk játék belső parancsait sorolja fel a felhasználónak.

*!tictacInfo* -  Az amőba játék belső parancsait sorolja fel a felhasználónak.

*!chessChallenge @USER* - A USER helyére a megfelelő felhasználónevet illesztve tudjuk az ellenfelet megpingelni, és kihívni egy mérkőzésre. Ekkor a pálya már meg is jelenik.

*!legal* - Felsorolja az aktuális állapotban adott lehetséges és legális lépéslehetőségeinket.

*!move xX* - Az x-et megfelelő bábu jelölőbetűjével, az X-et egy 1-8 közötti egész számmal helyettesítve léphetünk a megfelelő bábuval - feltéve hogy a lépés legális, lásd: *!legal*

*!resign* - A sakkjátszmát feladhatjuk ezzel a paranccsal.

*!ping* - TODO

*!tictactoe @USER @ÉN* - Az @USER-t a kihívni kívánt felhasználó nevével, az @ÉN-t a saját nevünkkel helyettesítve kezdhetjük el az amőbát, ha az még nem fut.

*!place X* - Az X-et egy 1-9 közötti egész  számmal helyettesítve helyezhetjük el a saját szimbólumunkat (egy nemüres mezőre).


## Közreműködők

A hétfő 12 órai Szoftverfejlesztési módszertanok kurzus kettes csoportja, vagyis:  
  [Görög Balázs](https://github.com/Errelian)  
  [Pintér Balázs](https://github.com/Pbalazs101)  
  [Somogyi Viktória](https://github.com/Sotori32)  
  [Béres Dániel](https://github.com/danielberes5)  
  [Vas Ruben](https://github.com/kuborka)  

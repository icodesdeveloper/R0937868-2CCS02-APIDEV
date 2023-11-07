# Basic API Docs

#### THEMA

Ik koos voor het thema boeken. Boeken lijkt mij een vergeten dingetje als ITer en zag dit als een gelegenheid om nog iets of wat in aanraking te komen met boeken. Deze API zou een voorbeeld kunnen zijn voor als basis voor een bibliotheek of dergelijke gebruik te kunnen worden.

#### EXTRAS (!!BELANGRIJK!!):

Ik heb basic HTTP security aan mijn web app toegevoegd. Het wachtwoord wordt zelfs geëncrypt. Indien er credentials worden gevraagd:

Username: !kun0  
Wachtwoord: adminadmin

Ook heb ik MYSQL gebruikt ipv SQLite, de database wordt ook in okteto gehost.

#### API

De API wordt gehost op Okteto en is bereikbaar via de volgende URL: [OKTETO](https://useritem-api-service-icodesdeveloper.cloud.okteto.net)

Een snel overzicht van de endpoints:

<table border="1" id="bkmrk-method-location-desc" style="border-collapse: collapse; width: 100%;"><colgroup><col style="width: 33.3333%;"></col><col style="width: 33.3333%;"></col><col style="width: 33.3333%;"></col></colgroup><tbody><tr><td>**Method**</td><td>**Location**</td><td>**Description**</td></tr><tr><td>GET</td><td>/books/</td><td>Laat alle boeken zien</td></tr><tr><td>POST</td><td>/books/</td><td>Maak een nieuw boek</td></tr><tr><td>GET</td><td>/books/(id)</td><td>Laat specifiek boek ID zien

</td></tr><tr><td>DELETE</td><td>/books/(id)</td><td>Verwijder een boek

</td></tr></tbody></table>

Deze tabel kan out-of-date zijn voor een meer accurate overzicht van de endpoints gebruik volgende link: [OpenAPI Docs](https://useritem-api-service-icodesdeveloper.cloud.okteto.net/docs#/)

[![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/ZETimage.png)](https://docs.claes.me/uploads/images/gallery/2023-11/ZETimage.png)[![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/mSEimage.png)](https://docs.claes.me/uploads/images/gallery/2023-11/mSEimage.png)

#### API IN ACTIE

- GET | /books/ | Laat alle boeken zien  
    [![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/image.png)](https://docs.claes.me/uploads/images/gallery/2023-11/image.png)
- GET | /books/(id) | Laat een specifiek boek zien  
    [![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/vRSimage.png)](https://docs.claes.me/uploads/images/gallery/2023-11/vRSimage.png)[![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/RsTimage.png)](https://docs.claes.me/uploads/images/gallery/2023-11/RsTimage.png)
- POST | /books/ | Maak een nieuw boek  
    [![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/JR6image.png)](https://docs.claes.me/uploads/images/gallery/2023-11/JR6image.png)[![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/yl7image.png)](https://docs.claes.me/uploads/images/gallery/2023-11/yl7image.png)
- DELETE | /books/(id) | Verwijder een boek  
    [![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/rn0image.png)](https://docs.claes.me/uploads/images/gallery/2023-11/rn0image.png)[![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/SyAimage.png)](https://docs.claes.me/uploads/images/gallery/2023-11/SyAimage.png)
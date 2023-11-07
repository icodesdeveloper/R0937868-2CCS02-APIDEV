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

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f5a4554696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f5a4554696d6167652e706e67.png)[![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f6d5345696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f6d5345696d6167652e706e67.png)

#### API IN ACTIE

- GET | /books/ | Laat alle boeken zien  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f537941696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f537941696d6167652e706e67.png)
- GET | /books/(id) | Laat een specifiek boek zien  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f765253696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f765253696d6167652e706e67.png)[![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f527354696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f527354696d6167652e706e67.png)
- POST | /books/ | Maak een nieuw boek  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f4a5236696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f4a5236696d6167652e706e67.png)[![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f796c37696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f796c37696d6167652e706e67.png)
- DELETE | /books/(id) | Verwijder een boek  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f726e30696d6167652e706e67.png)](https://raw.githubusercontent.com/icodesdeveloper/R0937868-2CCS02-APIDEV/main/.github/assets/68747470733a2f2f646f63732e636c6165732e6d652f75706c6f6164732f696d616765732f67616c6c6572792f323032332d31312f7363616c65642d313638302d2f726e30696d6167652e706e67.png)[![image.png](https://docs.claes.me/uploads/images/gallery/2023-11/scaled-1680-/SyAimage.png)](https://docs.claes.me/uploads/images/gallery/2023-11/SyAimage.png)
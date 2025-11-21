# InfraMusicStore

InfraMusicStore est une API REST permettant de gérer des **artistes**, **albums**, **pistes** et **types de média**. Le projet est développé en **Python** avec **Flask** et **SQLAlchemy**, utilise **MySQL** pour la base de données, et est entièrement conteneurisé avec **Docker** et **Docker Compose**. La documentation de l’API est disponible via **Swagger UI**.

---

## 🏗 Architecture du projet

```
InfraMusicStore/
├─ api/                  # Code source Flask
│  ├─ app.py             # Point d'entrée de l'application (routes, CRUD)
│  └─ models.py          # Modèles SQLAlchemy
├─ db/
│  ├─ init_struct.sql    # Structure de la base de données (tables)
│  └─ init_data.sql      # Données initiales
├─ docs/
│  └─ swagger.yml        # Documentation Swagger (endpoints, schémas, exemples)
├─ Dockerfile            # Image Docker pour l’API Flask
├─ docker-compose.yml    # Déploiement multi-conteneurs (DB, API, Adminer)
├─ .env.example          # Exemple de variables d'environnement
└─ README.md             # Ce fichier
```

---

## ⚙️ Prérequis

Avant de commencer, assurez-vous d’avoir installé :

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* Un navigateur web pour accéder à **Swagger UI** et **Adminer**

---

## 🚀 Installation et lancement

1. Cloner le projet :

```bash
git clone <URL_DU_REPO>
cd InfraMusicStore
```

2. Copier le fichier `.env.example` :

```bash
cp .env.example .env
```

3. Lancer les conteneurs Docker :

```bash
docker-compose up --build
```

4. Vérifier que les conteneurs fonctionnent :

```bash
docker ps
```

5. Accéder aux services :

* API Flask : [http://localhost:5001](http://localhost:5001)
* Swagger UI : [http://localhost:8080](http://localhost:8080)
* Adminer (interface MySQL) : [http://localhost:8080](http://localhost:8080)

---

## 📝 Commandes Docker utiles

* Lister tous les conteneurs en fonctionnement :

```bash
docker ps
```

* Lister tous les conteneurs, même arrêtés :

```bash
docker ps -a
```

* Supprimer tous les conteneurs et volumes :

```bash
docker-compose down -v
```

* Rebuilder l’image API après modification :

```bash
docker-compose up --build
```

* Se connecter à la base MySQL :

```bash
docker exec -it inmusic_db mysql -uroot -proot InfraMusicStore
```

---

## 🗄 Base de données

* SGBD : **MySQL 8**
* Nom de la base : `InfraMusicStore`
* Tables principales :

  * **Artist** (`ArtistId`, `Name`)
  * **Album** (`AlbumId`, `Title`, `ArtistId`)
  * **MediaType** (`MediaTypeId`, `Name`)
  * **Track** (`TrackId`, `Name`, `AlbumId`, `MediaTypeId`, `Milliseconds`, `UnitPrice`)

### Schéma simplifié :

```
Artist (ArtistId, Name)
    └─< Album (AlbumId, Title, ArtistId)
          └─< Track (TrackId, Name, AlbumId, MediaTypeId, Milliseconds, UnitPrice)
MediaType (MediaTypeId, Name)
    └─< Track (TrackId, Name, AlbumId, MediaTypeId, Milliseconds, UnitPrice)
```

---

## 🌐 Routes de l’API

### Artistes

* `GET /artists` : lister tous les artistes
* `GET /artists/<id>` : récupérer un artiste
* `POST /artists` : créer un artiste
* `PUT /artists/<id>` : modifier un artiste
* `DELETE /artists/<id>` : supprimer un artiste

### Albums

* `GET /albums`
* `GET /albums/<id>`
* `POST /albums`
* `PUT /albums/<id>`
* `DELETE /albums/<id>`

### MediaTypes

* `GET /mediatypes`
* `GET /mediatypes/<id>`
* `POST /mediatypes`
* `PUT /mediatypes/<id>`
* `DELETE /mediatypes/<id>`

### Tracks

* `GET /tracks`
* `GET /tracks/<id>`
* `POST /tracks`
* `PUT /tracks/<id>`
* `DELETE /tracks/<id>`

---

## 📖 Documentation Swagger

* Le fichier `docs/swagger.yml` contient :

  * Tous les endpoints
  * Les schémas des données
  * Des exemples de requêtes et de réponses
  * La possibilité de tester directement l’API via Swagger UI

* Swagger UI est accessible à : [http://localhost:8080](http://localhost:8080)

---

## 🔧 Variables d’environnement

Créez un fichier `.env` à partir de `.env.example` :

```env
# Base de données
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=InfraMusicStore
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_HOST=db

# Ports
API_PORT=5000
MYSQL_PORT=3306
ADMINER_PORT=8080
SWAGGER_PORT=8080
```

---

## ✅ Notes supplémentaires

* Tous les scripts SQL d’initialisation sont montés dans le conteneur MySQL via des volumes (`docker-entrypoint-initdb.d`).
* Pour tester vos modifications SQL, modifiez `init_struct.sql` ou `init_data.sql`, puis relancez le conteneur MySQL avec `docker-compose down -v && docker-compose up --build`.
* L’API Flask utilise SQLAlchemy pour les relations `1:N` et la gestion des cascades de suppression.
* Swagger UI peut être personnalisé en modifiant directement `swagger.yml`.

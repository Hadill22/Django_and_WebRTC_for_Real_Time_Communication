
# Django and WebRTC for Real-Time Communication

Ce projet est une application Django complète permettant la communication en temps réel via WebRTC, avec une gestion des utilisateurs, des salons (`Room`), des participants, des journaux de session, et une interface GraphQL + REST + WebSocket sécurisée par JWT.


- JWT authentication via `SimpleJWT`
- GraphQL support via `graphene-django`
- WebSocket signaling using `Django Channels`
 Fonctionnalités principales

 Authentification JWT (`SimpleJWT`)
- Signaling WebSocket via `Django Channels`
-  API REST (`Room`, `Participant`, `SessionLog`)
-  GraphQL (types, mutations, subscriptions)
- Tests avec Postman & GraphQL Playground
-  Interface HTML pour créer/rejoindre un salon

## Setup Instructions

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

3. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

4. **Start development server**:
    ```bash
    python manage.py runserver
    ```
    
    ***commande pour démarrer le serveur ASGI (comme runserver, mais pour Channels).
daphne Django_and_WebRTC_for_Real_Time_Communication.asgi:application
## Endpoints

- `api/token/`: Obtain JWT token
- `rooms/`, `participants/`, `sessionlogs/`: RESTful endpoints
- `graphql/`: GraphQL interface

nstallation locale

```bash
git clone <repo-url>
cd Django_and_WebRTC_for_Real_Time_Communication
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


Authentification JWT (Postman)

### Endpoint pour obtenir un token

```
POST /api/token/
{
   "username": "hp",
    "password": "Admin123"
}

```

### Exemple d'en-tête à utiliser dans Postman :

```
Authorization: Bearer <your_token>
```

---

## 🔁 Endpoints REST testables via Postman

- `GET /rooms/` : Liste des rooms
- `POST /rooms/` : Créer une room
- `GET /participants/` : Liste des participants
- `POST /participants/` : Ajouter un participant
- `GET /sessionlogs/` : Liste des logs
- `POST /sessionlogs/` : Créer un log

---

## 🔄 WebSocket Signaling

### Exemple côté client dans `chat_room.html`

```javascript
const socket = new WebSocket("ws://127.0.0.1:8000/ws/signaling/{{ room.code }}/");
```

### Côté backend : `consumers.py` gère les messages entrants/sortants

---


### 🔹 Query (Participants)

```graphql
query {
  allParticipants {
    id
    username
    role
  }
}
```

### 🔹 Mutation (Créer une Room)

```graphql
mutation {
  createRoom(name: "TestRoom") {
    room {
      id
      name
      code
    }
  }
}
```

### 🔹 Subscription (Nouvelle Room)

```graphql
subscription {
  roomCreated {
    room {
      name
      code
    }
  }
}
```


# Docker
```bash
docker-compose up -d
docker exec -it backend-python bash
```

# Python
## Installation des dépendances
```bash
poetry install --no-root
```

### Swagger et documentation
```bash
http://127.0.0.1:3000/docs
http://127.0.0.1:3000/redoc
```

# Backend simple sans base de données
```bash
# Server
```bash
poetry run uvicorn backend:app --host 0.0.0.0 --port 3000 --reload
```

## Test des routes
```bash
http://127.0.0.1:3000/persons
http://127.0.0.1:3000/person/Martin
http://127.0.0.1:3000/persons/older_than?min_age=29
```

# Backend avec base de données


## Test des routes
```bash
curl -X POST http://127.0.0.1:8000/addcity -H "Content-Type: application/json" -d '{"name": "Paris"}'
curl -X POST http://127.0.0.1:8000/addperson -H "Content-Type: application/json" -d '{"nom": "Doe", "prenom": "John", "age": 30, "city_id": 1}'
curl -X POST http://127.0.0.1:8000/addskill -H "Content-Type: application/json" -d '{"name": "Python"}'
curl -X POST http://127.0.0.1:8000/addpersonskill -H "Content-Type: application/json" -d '{"person_id": 1, "skill_id": 1}'
```


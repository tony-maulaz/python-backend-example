# Database
```sql
CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```

# Python
```bash
pip install fastapi uvicorn sqlalchemy psycopg2
```

# Server
```bash
uvicorn main:app --reload
```

### Swagger et documentation
```bash
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```


## Test des routes
```bash
curl -X POST http://127.0.0.1:8000/addcity -H "Content-Type: application/json" -d '{"name": "Paris"}'
curl -X POST http://127.0.0.1:8000/addperson -H "Content-Type: application/json" -d '{"nom": "Doe", "prenom": "John", "age": 30, "city_id": 1}'
curl -X POST http://127.0.0.1:8000/addskill -H "Content-Type: application/json" -d '{"name": "Python"}'
curl -X POST http://127.0.0.1:8000/addpersonskill -H "Content-Type: application/json" -d '{"person_id": 1, "skill_id": 1}'

```


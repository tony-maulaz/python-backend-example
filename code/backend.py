from fastapi import FastAPI, HTTPException, Query, Response
from pydantic import BaseModel # permet de définir des modèles de données et serialiser/désérialiser des données
from typing import List
import uvicorn


# Création de l'application FastAPI
app = FastAPI()

# Modèle de données pour une personne
class Person(BaseModel):
    nom: str
    prenom: str
    age: int

# Liste de personnes (simulant une base de données)
personnes = [
    Person(nom="Dupont", prenom="Jean", age=30),
    Person(nom="Martin", prenom="Sophie", age=25),
    Person(nom="Durand", prenom="Paul", age=40)
]

# Route pour récupérer la liste des personnes
@app.get("/persons", response_model=List[Person])
def get_persons():
    return personnes

# route : http://127.0.0.1:8000/person/Dupont
# Route pour récupérer une personne par son nom
@app.get("/person/{nom}", response_model=Person)
def get_person_by_name(nom: str):
    for person in personnes:
        if person.nom.lower() == nom.lower():
            return person
    # Si la personne n'est pas trouvée, renvoyer une erreur 404
    raise HTTPException(status_code=404, detail="Personne non trouvée")

# route : http://127.0.0.1:8000/persons/older_than?min_age=29
# Route pour récupérer les personnes avec un âge supérieur à une valeur donnée
@app.get("/persons/older_than", response_model=List[Person])
def get_persons_older_than(min_age: int = Query(0, description="Âge minimum")):
    result = [person for person in personnes if person.age > min_age]
    
    if not result:
        raise HTTPException(status_code=404, detail="Aucune personne trouvée avec cet âge minimum")
    
    return result

# pour éviter l'erreur 404 favicon.ico not found
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)
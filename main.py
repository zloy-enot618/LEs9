from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


animals = [
    {
        "id": 1,
        "name": "Лев",
        "value": 9,
        "risk": "Экстремальный"
    },
    {
        "id": 2,
        "name": "Орёл",
        "value": 17,
        "risk": "Средний"
    },
    {
        "id": 3,
        "name": "Утка",
        "value": 189,
        "risk": "Минимальный"
    },
    {
        "id": 4,
        "name": "Горилла",
        "value": 3,
        "risk": "ОЧЕНЬ ЭКСТРЕМАЛЬНЫЙ"
    },
    {
        "id": 5,
        "name": "Слоник",
        "value": 3,
        "risk": "Минимальный"
    }
]

class Animals(BaseModel):
    id: int
    name: str
    value: int
    risk: str


class AddAnimal(BaseModel):
    name: str
    value: int
    risk: str


@app.get("/", response_class=HTMLResponse)
def say_hello():
    html_hello = """
    <!DOCTYPE html>

    <html>
        <head>
            <title>Hello!</title>
        </head>
        <body>
            <h1>Привет! \nЗайди на /docs.</h1>
        </body>

    </html>
"""
    return HTMLResponse(content=html_hello)



@app.get("/animals", response_model=list[Animals])
def get_animals():
    return animals


@app.post("/animals", response_model=Animals, status_code=201)
def add_animal(animal: AddAnimal):
    am_id = len(animals) + 1

    new_animal = {
        "id": am_id,
        "name": animal.name,
        "value": animal.value,
        "risk": animal.risk
    }
    animals.append(new_animal)
    return new_animal
    

@app.put("/animals/{animal_id}", response_model=Animals)
def uptade_animal(animal_id: int, animal: AddAnimal):
    for saved_animal in animals:
        if saved_animal["id"] == animal_id:
            saved_animal["id"] = animal_id
            saved_animal["name"] = animal.name
            saved_animal["value"] = animal.value
            saved_animal["risk"] = animal.risk
            return saved_animal


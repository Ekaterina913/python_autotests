import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "c5b67135923ab37d0109c35fbb8896d1"
HEADER = {"Content-Type" : "application/json", "trainer_token":TOKEN}
TRAINER_ID = 12611
body_create= {
    "name": "Парампам",
    "photo_id": 157
}
body_name={
    "pokemon_id": "175526",
    "name": "Buby",
    "photo_id": 234
}
body_catch={
    "pokemon_id": "175822"
} 
response_create = requests.post(url=f"{URL}/pokemons", headers=HEADER, json=body_create)
print(response_create.text)

"""response_name = requests.put(url=f"{URL}/pokemons", headers=HEADER, json=body_name)
print(response_name.text)"""

response_catch = requests.post(url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_catch)
print(response_catch.text)

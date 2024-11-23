import requests
from typing import Dict, Any

async def get_pokemon_data(pokemon_name: str) -> Dict[str, Any]:
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        response.raise_for_status()
        data = response.json()

        return {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "sprite": data["sprites"]["other"]["official-artwork"]["front_default"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch Pokémon data: {str(e)}"}
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"],
            "id": data["id"],
            "types": [t["type"]["name"] for t in data["types"]],
            "height": data["height"],
            "weight": data["weight"],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "sprite_url": data["sprites"]["front_default"]
        }
        return pokemon_info
    else:
        print("Pokemon not found.")
        return None

def display_pokemon_info(pokemon_info):
    if pokemon_info:
        print("Name:", pokemon_info["name"].capitalize())
        print("ID:", pokemon_info["id"])
        print("Types:", ", ".join(pokemon_info["types"]))
        print("Height:", pokemon_info["height"])
        print("Weight:", pokemon_info["weight"])
        print("Abilities:", ", ".join(pokemon_info["abilities"]))
        display_pokemon_sprite(pokemon_info["sprite_url"])
    else:
        print("No information to display.")

def display_pokemon_sprite(sprite_url):
    response = requests.get(sprite_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    else:
        print("Failed to load sprite.")

def main():
    pokemon_name = input("Enter the name of the Pokemon: ")
    pokemon_info = get_pokemon_info(pokemon_name)
    display_pokemon_info(pokemon_info)

if __name__ == "__main__":
    main()

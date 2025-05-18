import json
import utils
import requests
import random
from time import sleep

url = "https://pokeapi.co/api/v2/"

class Pokemon:
    def __init__(self, name, type, id, height, weight):
        self.name = name
        self.type = type
        self.id = id
        self.height = height
        self.weight = weight
        
class Pokedex:
    def __init__(self):
        try:
            with open("pokedex.json") as pokedex_file:
                self.pokedex = json.load(pokedex_file)
        except FileNotFoundError:
            self.pokedex = {}
            self.choose_starter()

        self.types = [
                    'Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice',
                    'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic',
                    'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'
                ]

    def add_pokemon(self, pokemon):

        self.pokedex[pokemon.name] = { "Name": pokemon.name,
                                    "Type": pokemon.type,
                                    "Id": pokemon.id,
                                    "Height": pokemon.height,
                                    "Weight": pokemon.weight
                                }
        
        self.save_pokedex()
        print(f"Pokemon {pokemon.name} added to your Pokedex!")
        sleep(2)

    def choose_starter(self):
        starter_pokemons = ["Squirtle", "Bulbasaur", "Charmander"]
        
        while True:
        
            starter = input("\nChoose a starter Pokemon. Squirtle, Bulbasaur or Charmander: ")
            starter = starter.lower()
            starter = starter.capitalize()
        
            if starter not in starter_pokemons:
                print("\nInvalid starter Pokemon.")
                sleep(2)
            else:
                break
        
        self.get_pokemon(starter)
        self.save_pokedex()
        if starter == "Squirtle":
            print(utils.ascii_squirtle)
            sleep(2)
        elif starter == "Charmander":
            print(utils.ascii_charmander)
            sleep(2)
        else:
            print(utils.ascii_bulbasaur)
            sleep(2)

    def remove_pokemon(self, pokemon):
        pokemon = pokemon.capitalize()

        if pokemon in self.pokedex:
            del self.pokedex[pokemon]
            self.save_pokedex()
            print(f"Pokemon {pokemon} removed from your Pokedex.")
            sleep(2)
        else:
            print("Pokemon not found at your Pokedex.")
            sleep(2)


    def print_pokemon(self, pokemon):
        pokemon = pokemon.capitalize()

        if pokemon in self.pokedex:
            for attribute, value in self.pokedex[pokemon].items():
                print(f"{attribute}: {value}")
            sleep(2)
        else:
            print("Pokemon not found at your Pokedex.")
            sleep(2)

    def print_type_pokemon(self, type):
        type = type.capitalize()

        if type in self.types:
            
            print(utils.pokemon_ascii_banner(f"{type}"))
            pokemons_by_type = [pokemon for pokemon, data in self.pokedex.items() if data["Type"] == type]
            print()
            for pokemon in pokemons_by_type:
                print(pokemon)
            sleep(2)
        else:
            print(f"None Pokemon of the type {type} was found on your Pokedex.")
            sleep(2)

    def print_pokedex(self):
        print(utils.pokemon_ascii_banner("Pokedex"))
        for pokemon in self.pokedex:
            print(pokemon)
        print("")
        sleep(2)

    def print_stats(self):
        print()
        print(utils.pokemon_ascii_banner("Stats"))
        self.many = len(self.pokedex)

        self.tallest = max(self.pokedex.items(), key=lambda x: x[1]["Height"])[0]
        self.shortest = min(self.pokedex.items(), key=lambda x: x[1]["Height"])[0]
        self.heaviest = max(self.pokedex.items(), key=lambda x: x[1]["Weight"])[0]
        self.lightest = min(self.pokedex.items(), key=lambda x: x[1]["Weight"])[0]

        print(f"You currently have {self.many} Pokemons.\nYour tallest Pokemon is {self.tallest}.\nYour shortest Pokemon is {self.shortest}.\nYour heaviest Pokemon is {self.heaviest}.\nYour lightest Pokemon is {self.lightest}.\n")
        sleep(2)
    
    def save_pokedex(self):
        with open("pokedex.json", "w") as pokedex_file:
            json.dump(self.pokedex, pokedex_file, indent=4)

    def get_pokemon(self, pokemon_name):
        response = requests.get(f"{url}/pokemon/{pokemon_name}")

        if response.status_code == 200:
            pokemon_data = response.json()
            new_pokemon = Pokemon(name=pokemon_data["name"].capitalize(), 
                                type=pokemon_data["types"][0]["type"]["name"].capitalize(),
                                id=pokemon_data["id"],
                                height=pokemon_data["height"],
                                weight=pokemon_data["weight"])
            self.add_pokemon(new_pokemon)
        else:
            print("It wasn't possible to retrieve the Pokemon's data. Maybe a typo?")
            
    def random_pokemon(self):
        pokemons = [pokemon for pokemon in self.pokedex]
        random_pokemon = random.choice(pokemons)
        print(f"Your random Pokemon is {random_pokemon}.")
        self.print_pokemon(random_pokemon)
    
    def count_by_type(self):
        counter = {}

        types = [value['Type'] for _, value in self.pokedex.items()]

        for type in types:
            if type in counter:
                counter[type] += 1
            else:
                counter[type] = 1

        for item, value in counter.items():
            print(f"{item}: {value}")
        sleep(2)
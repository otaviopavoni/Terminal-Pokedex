import models
from time import sleep

user_pokedex = models.Pokedex()

class PokedexUI:
    def __init__(self):
        self.pokedex = models.Pokedex()
        self.menu_options = {
            1: ("Add Pokemon", self.add_pokemon),
            2: ("Remove Pokemon", self.remove_pokemon),
            3: ("Check Pokedex", self.show_pokedex),
            4: ("Check Pokemon", self.show_pokemon),
            5: ("Check Pokemons by type", self.show_by_type),
            6: ("See Pokedex's Stats", self.show_stats),
            7: ("Type count", self.type_count),
            8: ("Random Pokemon", self.random_pokemon),
            9: ("Quit", exit)
        }

    def display_menu(self):
        print("\n=== POKEDEX MENU ===")
        for key, (description, _) in self.menu_options.items():
            print(f"[{key}] {description}")

    def run(self):
        while True:
            self.display_menu()

            try:
                choice = int(input("Select an option: "))
                if choice in self.menu_options:
                    self.menu_options[choice][1]()
            except ValueError:
                print("Please enter a number!")

    def add_pokemon(self):
        name = input("Type the name of the Pokemon you want to add: ")
        pokemon = self.pokedex.get_pokemon(name)

    def remove_pokemon(self):
        name = input("Type the name of the Pokemon you want to remove: ")
        pokemon = self.pokedex.remove_pokemon(name)

    def show_pokemon(self):
        name = input("Type the name of the Pokemon you want to check: ")
        self.pokedex.print_pokemon(name)
    
    def show_pokedex(self):
        self.pokedex.print_pokedex()

    def show_by_type(self):
        type = input("Select the type of the Pokemon you want to add: ")
        self.pokedex.print_type_pokemon(type)

    def show_stats(self):
        self.pokedex.print_stats()

    def type_count(self):
        self.pokedex.count_by_type()

    def random_pokemon(self):
        self.pokedex.random_pokemon()
    
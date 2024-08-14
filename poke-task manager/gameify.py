from pokemon import pokemon_list
import random
from tabulate import tabulate
import pickle
import time
import os

class Trainer:
    def __init__(self, name):
        self.name = name
        self.box = set()
        self.party = set()
        self.box_names = []
        self.pokedex = []
        self.tasks = {}
        self.add_starter()
    
    def __str__(self):
        return self.name

    def add_starter(self):
        """
        Adds the first pokemon to your box, you can input
        any base pokemon here. Always occurs when initialising trainer.
        """
        starter = input("\nChoose your starter pokemon!\n> ")
        while not starter in pokemon_list.keys():
            print("\nThat pokemon is not in the box, check your spelling and capitalization. The pokemon must also be pre-evolved.")
            starter = input("\nChoose your starter pokemon!\n> ")
        self.discover_pokemon(starter)

    def gain_xp(self, xp):
        """
        Gives the allocated xp to each pokemon within your party.  
        input - xp, Int, the amopunt of xp to be added
        """
        for pokemon in self.party:
            pokemon.xp += xp
            while pokemon.xp >= pokemon.lvl * 100:
                pokemon.lvl_up(self)
    
    def discover_pokemon(self, name):
        """
        Adds a pokemon to the box, telling the user that a
        pokemon has been found.  
        input - name, Str, the name of the pokemon found.
        """
        if not name in self.pokedex:
            self.pokedex.append(name)
        if not name in self.box_names:
            self.box.add(Pokemon(name))
            self.box_names.append(name)
            print(f"\n{name} has been discovered!")

    def add_to_party(self, name):
        """
        Adds a discovered pokemon within a users box to their party.  
        Input - name, Str, name of the pokemon to be added
        """
        pokemon = self.find_pokemon(name)
        if pokemon in self.box:
            if len(self.party) == 6:
                print("\nParty is at max size, remove a pokemon first.")
            else:
                self.party.add(pokemon)
                print(f"\n{pokemon} has been added to your party!")
        else:
            print(f"\n{pokemon} is not in your box")

    def remove_from_party(self, name):
        """
        Removes a pokemon from the users party.  
        input - name, Str, name of the pokemon to be removed
        """
        pokemon = self.find_pokemon(name)
        if len(self.party) == 0:
            print("\nParty is empty.")
        elif pokemon in self.party:
            self.party.remove(pokemon)
            print(f"\n{name} has been removed from your party.")
        else:
            print(f"\n{name} is not in your party.")

    def unlock_random_pokemon(self):
        """
        Unlocks a random pokemon from the list of all base pokemon.  
        The unlock is cancelled if the pokemon has already been discovered.
        """
        pokemon = random.choice(list(pokemon_list.keys()))
        if not pokemon in self.box_names:
            print("\nWhat's this? A random pokemon has been found!")
            self.discover_pokemon(pokemon)

    def complete_task(self, task):
        """
        Allows the user to complete a task, giving them the assigned amount
        of experience to all pokemon in their party.  
        input - task, Str, the matching string of a task available to complete.
        """
        if len(self.tasks) == 0:
            print("\nNo tasks have been added.")
        elif task in self.tasks:
            xp_gain = self.tasks[task]
            print(f"\nAll pokemon in party have gained {xp_gain} xp.")
            self.gain_xp(xp_gain)
            if random.random() <= 0.3:
                self.unlock_random_pokemon()

    def print_party(self):
        """
        Returns a table containing every pokemon in the users party, with
        its given level.  
        Output - Str, the table of pokemon
        """
        def func(i):
            return i[1]
        
        head = ["Pokemon", "Level", "Experience"]
        data = []
        for pokemon in self.party:
            data.append([pokemon.name, pokemon.lvl, str(pokemon.xp) + " / " + str(pokemon.lvl * 100)])
            data.sort(key=func, reverse=True)
        return (tabulate(data, headers=head, tablefmt="grid"))

    def find_pokemon(self, name):
        """
        Given a pokemon's name, this finds and returns the Pokemon object
        within the trainers box and party  
        Input - name, Str, the name of the pokemon to be found  
        Output - pokemon, Pokemon, the pokemon object that has been found
        """
        for pokemon in self.box:
            if pokemon.name == name:
                return pokemon
        return None
            
    def add_task(self):
        """
        Adds a task to the list of tasks for that user.
        """
        task = input("\nEnter the name of the new task\n> ")
        xp = int(input("\nEnter the experience to be gained by completing this task\n> "))
        if task in self.tasks:
            print("\nTask already exists.")
        elif xp <= 0:
            print("\nxp must be greater than 0")
        else:
            self.tasks[task] = xp
            print("\nTask has been added\n")

    def print_box(self):
        """
        Returns the entire box, listing every pokemon found by the user.
        Output - Str, the list of pokemon
        """
        return "Box:\n" + ", ".join(self.box_names)
    
    def party_names(self):
        """
        Returns a list of every pokemons name within the users party, 
        for easier searching.
        Output - Array of Str, the list of pokemon
        """
        party = []
        for pokemon in self.party:
            party.append(pokemon.name)
        return party
    
    def print_tasks(self):
        """
        Returns a table containing every task and allocated xp gain
        for completing that task.
        Output - Str, the formatted table of each task
        """
        def func(i):
            return i[1]
        data = [[i, int(self.tasks[i])] for i in self.tasks.keys()]
        data.sort(key=func)
        return tabulate(data, tablefmt="grid")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.pop(task)
            print("\nTask has been deleted.")
        else:
            print("\nTask does not exist.")

    def print_pokedex(self):
        return "Pokedex:\n" + ", ".join(self.pokedex)


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.lvl = 14
        self.evolutions = pokemon_list[name]
        self.stage = 1
        # self.shape = pokemon_shapes[name]

    def __str__(self):
        return self.name
    
    def lvl_up(self, trainer):
        """
        Levels up the pokemon by removing the next level of xp and increasing its level. 
        Also by updating their name and stage number if the pokemon can evolve.  
        Input - trainer, Trainer, the trainer that owns the given pokemon
        """
        self.xp -= self.lvl * 100
        self.lvl += 1
        print(f"\n{self.name} has leveled up, {self.name} is now level {self.lvl}!")
        if self.lvl >= self.stage * 15 and len(self.evolutions) > self.stage:
            new_stage = self.evolutions[self.stage]
            if isinstance(new_stage, tuple):
                new_stage = random.choice(new_stage)
            trainer.box_names[:] = [new_stage if x == self.name else x for x in trainer.box_names]
            self.stage += 1
            print(f"\n{self.name} has evolved into {new_stage}!")
            self.name = new_stage
            trainer.pokedex.append(self.name)

    def print_pokemon(self):
        """
        Returns a descriptive table of the stats of one pokemon.  
        Output - Str, the formatted table containing a pokemons name,
        level, and xp to level up.
        """
        data = [["Name", self.name],
                ["Level", self.lvl],
                ["Experience to next lvl", self.lvl * 100 - self.xp]]
        return tabulate(data, tablefmt="grid")


def save_game(trainer, name_set):
    """
    Saves the game to two files, one for the set of all users,
    and another for the current trainer.  
    Input - name_set, Set, the collection of all users.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, f"users.pickle"), "wb") as file2:
        pickle.dump(name_set, file2)
    with open(os.path.join(here, f"state_{trainer.name}.pickle"), "wb") as file:
        pickle.dump(trainer, file)
        print("Game has been saved")

def load_users():
    """
    Loads the file containing name_set, the list of all users.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "users.pickle"), "rb") as file:
            if os.path.getsize(os.path.join(here, "users.pickle")) == 0:
                return set()
            name_set = pickle.load(file)
            return name_set
    except FileNotFoundError:
        print("No users file found")
    except pickle.UnpicklingError:
        print("Invalid data in users file")

def load_game(name):
    """
    Loads the trainer profile and data for the given trainer.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, f"state_{name}.pickle"), "rb") as file:
            found_trainer = pickle.load(file)
            return found_trainer
    except FileNotFoundError:
        print("No trainer file found")
    except pickle.UnpicklingError:
        print("Invalid data in trainer file")


def startUp(name_set):
    """
    Function to start the game and load the users profile.
    """
    trainer = None
    print("\nWelcome to the poke-task manager! \nEnter your trainer name to continue.")
    name = input("> ")
    if name in name_set:
        print("\nUser found, use this save? y/n")
        reply = input("> ")
        if reply == "y":
            print("\nLoading saved profile.")
            trainer = load_game(name)
        else: 
            print("Startup cancelled")
    else:
        print("\nUser not found, would you like to create a new profile? y/n")
        reply = input("> ")
        if reply == "y":
            print("\nCreating new profile.")
            name_set.add(name)
            trainer = Trainer(name)
        else: 
            print("Startup cancelled")
    return trainer

def main():
    """
    Main function of the program.
    """
    name_set = load_users()
    trainer = None
    while trainer == None:
        trainer = startUp(name_set)
    running = True
    while running:
        print("")
        print("*" * 50)
        print("")
        print("\nWhat would you like to do?")

        num = int(input("\n 1 - Complete a task \n 2 - View your party \n 3 - View a specific pokemon \n 4 - Add to your party \n 5 - Remove from your party \n 6 - Add a task \n 7 - Remove a task \n 8 - View Box \n 9 - View Pokedex \n 10 - Save game \n 11 - Quit \n> "))
        
        print("")
        print("*" * 50)
        print("")

        if num == 1:
            print("\nEnter exactly the task you would like to complete:")
            print(trainer.print_tasks())
            task = input("> ")
            trainer.complete_task(task)

        elif num == 2:
            print("Party:")
            print(trainer.print_party())

        elif num == 3:
            print("\n Which pokemon would you like to view?\n")
            print(trainer.print_party())
            pokemon = input("> ")
            if pokemon in trainer.party_names():
                print("\n" + trainer.find_pokemon(pokemon).print_pokemon())
            else:
                print(f"\n{pokemon} is not in party.")

        elif num == 4:
            print("\nWhich pokemon from your box would you like to add to your party? \n")
            print(trainer.print_box())
            pokemon = input("> ")
            trainer.add_to_party(pokemon)

        elif num == 5:
            print("\nWhich pokemon would you like to remove from your party? \n")
            print("\n" + trainer.print_party())
            pokemon = input("> ")
            trainer.remove_from_party(pokemon)

        elif num == 6:
            trainer.add_task()

        elif num == 7:
            print(trainer.print_tasks())
            print("Which task would you like to remove?")
            task = input("> ")
            trainer.remove_task(task)

        elif num == 8:
            print(trainer.print_box())

        elif num == 9:
            print(trainer.print_pokedex())

        elif num == 11:
            save_game(trainer, name_set)
            running = False
            time.sleep(5)

        else:
            save_game(trainer, name_set)

main()
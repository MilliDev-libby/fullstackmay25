import random

class BigCat:
    def __init__(self, name):
        self.name = name
        self.speed = 5
        self.strength = 5
        self.intelligence = 5
        self.health = 5
        self.durability = 5

    def is_alive(self):
        return self.health > 0

    def stats(self):
        return f"{self.name} - Health: {self.health}, Strength: {self.strength}, Speed: {self.speed}, Intelligence: {self.intelligence}, Durability: {self.durability}"

class Lion(BigCat):
    def __init__(self, name="Lion"):
        super().__init__(name)
        self.strength = 50
        self.health = 50

    def king(self, target):
        if isinstance(target, Cheetah):
            if random.random() <= 0.6:
                print(f"{target.name} escaped Lion's wrath!")
                return
        print(f"{self.name} used KING on {target.name}!")
        target.speed = 0
        target.strength = 0
        target.intelligence = 0
        target.health = 0
        target.durability = 0

class Leopard(BigCat):
    def __init__(self, name="Leopard"):
        super().__init__(name)
        self.strength = 30
        self.intelligence = 30
        self.health = 30

    def attack(self, target):
        if isinstance(target, Lion):
            print(f"{self.name} attacked {target.name} and triggered king()!")
            target.king(self)
        elif isinstance(target, Cheetah):
            if random.random() <= 0.6:
                print(f"{target.name} dodged Leopard's attack!")
                return
            else:
                print(f"{self.name} hit {target.name}!")
                target.health -= 15
        else:
            print(f"{self.name} hit {target.name}!")
            target.health -= 15

class Cheetah(BigCat):
    def __init__(self, name="Cheetah"):
        super().__init__(name)
        self.speed = 75
        self.strength = 25
        self.intelligence = 25
        self.health = 25
        self.durability = 25

    def run(self, target):
        if isinstance(target, Leopard):
            print(f"{self.name} ran into {target.name}!")
            target.attack(self)
        elif isinstance(target, Lion):
            print(f"{self.name} ran into {target.name}!")
            target.king(self)

        if self.is_alive():
            print(f"{self.name} ran away and lost 20 health!")
            self.health -= 20


# Game Simulation
def battle():
    lion = Lion()
    leopard = Leopard()
    cheetah = Cheetah()

    cats = [lion, leopard, cheetah]
    print("Initial Stats:")
    for cat in cats:
        print(cat.stats())
    print("\n--- Game Begins ---\n")

    # Turn 1: Leopard attacks Lion
    leopard.attack(lion)

    # Turn 2: Cheetah runs into Leopard
    cheetah.run(leopard)

    # Turn 3: Lion uses king on Leopard
    lion.king(leopard)

    # Turn 4: Cheetah runs into Lion
    cheetah.run(lion)

    print("\n--- Final Stats ---")
    for cat in cats:
        print(cat.stats())

    # Decide winner
    alive = [cat for cat in cats if cat.is_alive()]
    if len(alive) == 1:
        print(f"\n🏆 {alive[0].name} is the winner!")
    elif len(alive) == 0:
        print("\n💀 No one survived...")
    else:
        alive.sort(key=lambda x: x.health, reverse=True)
        print(f"\n🏆 {alive[0].name} wins with highest health!")

# Run the game
battle()


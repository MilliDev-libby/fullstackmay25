import random

class Human:
    def __init__(self, name, strength=3, intelligence=3, dexterity=3, health=100):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.health = health

    def attack(self, target):
        if isinstance(target, Human):
            damage = 5 * self.strength
            target.health -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        else:
            print(f"{self.name} can only attack other humans.")

    def show_stats(self):
        print(f"{self.name} => Health: {self.health}, STR: {self.strength}, INT: {self.intelligence}, DEX: {self.dexterity}")

class Wizard(Human):
    def __init__(self, name):
        super().__init__(name, intelligence=25, health=50)

    def heal(self):
        heal_amount = 10 * self.intelligence
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} points. Health is now {self.health}.")

    def fireball(self, target):
        if isinstance(target, Human):
            damage = random.randint(20, 50)
            target.health -= damage
            print(f"{self.name} casts Fireball on {target.name} for {damage} damage.")
        else:
            print("Invalid target.")

class Ninja(Human):
    def __init__(self, name):
        super().__init__(name, dexterity=175)

    def steal(self, target):
        if isinstance(target, Human):
            damage = 5 * self.strength
            target.health -= damage
            self.health += 10
            print(f"{self.name} steals from {target.name}, dealing {damage} damage and healing 10 health. Health is now {self.health}.")
        else:
            print("Invalid target.")

    def get_away(self):
        self.health -= 15
        print(f"{self.name} gets away! Lost 15 health. Health is now {self.health}.")

class Samurai(Human):
    def __init__(self, name):
        super().__init__(name, health=200)

    def death_blow(self, target):
        if isinstance(target, Human):
            if target.health < 50:
                target.health = 0
                print(f"{self.name} performs Death Blow on {target.name}. {target.name} is defeated!")
            else:
                print(f"{target.name} is too strong for Death Blow (health ≥ 50).")
        else:
            print("Invalid target.")

    def meditate(self):
        self.health = 200
        print(f"{self.name} meditates and restores full health. Health is now {self.health}.")

# --- Game Example ---

# Create characters
wiz = Wizard("Gandalf")
ninja = Ninja("Shadow")
sam = Samurai("Musashi")
enemy = Human("Bandit", strength=4)

# Show initial stats
wiz.show_stats()
ninja.show_stats()
sam.show_stats()
enemy.show_stats()
print("\n--- Actions Begin ---\n")

# Wizard attacks with fireball and heals
wiz.fireball(enemy)
wiz.heal()

# Ninja steals from enemy and escapes
ninja.steal(enemy)
ninja.get_away()

# Samurai attacks and then uses death blow if possible
sam.attack(enemy)
sam.death_blow(enemy)
sam.meditate()

# Show final stats
print("\n--- Final Stats ---")
wiz.show_stats()
ninja.show_stats()
sam.show_stats()
enemy.show_stats()

import random

# Base class
class BigCat:
    def __init__(self):
        self.speed = 5
        self.strength = 5
        self.intelligence = 5
        self.health = 5
        self.durability = 5

    def is_alive(self):
        return self.health > 0
    
    def display_stats(self, name="Big Cat"):
        print(f"\n{name}'s Stats:")
        print(f"Speed: {self.speed}, Strength: {self.strength}, Intelligence {self.intelligence}, Health: {self.health}, Durability: {self.durability}")

class Lion(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 50
        self.health = 50
    
    def king(self,target):
        if isinstance(target, Cheetah):
            if random.random() < 0.6:
                print("Cheetah dodged the Lion's wrath!")
                return
        print(f"Lion used king() on {target.__class__.__name__}")
        target.speed = 0
        target.strength = 0
        target.intelligence = 0
        target.health = 0
        target.durability = 0

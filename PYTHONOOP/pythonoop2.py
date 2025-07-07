class Boxer: 
    def __init__(self, name, size, strength, wins, losses):
        self.name = name
        self.size = size
        self.strength = strength
        self.wins = wins 
        self.losses = losses
    
    def display_stats(self):
        print(f"\n stats for {self.name}:")
        print(f"Size: {self.size}")
        print(f"Strength: {self.strength}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
    
# Create 2 boxer objects
boxer1 = Boxer("Iron Mike", size=9, strength=10, wins=25, losses=2)
boxer2 = Boxer("Crusher Carl", size=8, strength=9, wins=20, losses=5)

# User chooses which boxer to bet on
print("/nwho would you like to bet on?")
print("1 = Iron Mike")
print("2 = Crusher Carl")
choice = input("Enter the number of your choice (1 or 2): ")

# Determine the better boxer based on total stats
score1 = boxer1.size + boxer1.strength + boxer1.wins - boxer1.losses
score2 = boxer2.size + boxer2.strength + boxer2.wins - boxer2.losses

# Determine and display result
if (choice == "1" and score1 >= score2) or (choice == "2" and score2 >= score1):
    print("/n You won your bet!")
else:
    print("/n You lost your bet!")


# Reveal comparsion
print(f"\n{boxer1.name} total score: {score1}")
print(f"{boxer2.name} total score: {score2}")


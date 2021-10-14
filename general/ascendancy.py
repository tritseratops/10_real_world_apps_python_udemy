import random

race = random.randint(1,21)

races = {1:"Minions", 2: "Snowendomas", 3: "Orfa", 4: "Kambuchka", 5: "Hanshaks", 6: "Fluendri", 7: "Balifids", 8: "Swaparamans", 9: "Frutmaka",
         10: "Shevar", 11: "Govorom", 12: "Ungooma", 13: "Dubtaks", 14: "Capelons", 15: "Mebes", 16: "Oculons", 17: "Arbryls", 18: "Marmozians",
         19: "Chronomyst", 20: "Chamachies", 21:"Nimbuloids"}

color = random.randint(1,7)
colors = {1:"Blue", 2: "Orange", 3: "Green", 4: "Violet", 5: "Yellow", 6: "Pink", 7: "Brown"}

print(f"Your race is {races[race]}")
print(f"Your color is {colors[color]}")


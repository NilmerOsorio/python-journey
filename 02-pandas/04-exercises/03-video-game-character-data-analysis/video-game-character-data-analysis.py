import pandas as pd

# 1. Load the CSV into a DataFrame called characters

print("----Exercise 1----")

characters = pd.read_csv("video_game_characters.csv")
print(characters.to_string())
print()

# 2. Print the frist 5 rows

print("----Exercise 2----")
print(characters.iloc[[0,1,2]])
print()

# 3. Print only Name, Game, and Level

print("----Exercise 3----")
print(characters[["Name", "Game", "Level"]].to_string(index=False))
print()

# 4. Fin all characters with a Level greather than 70.

print("----Exercise 4----")
print(characters[characters["Level"] > 70].to_string(index=False))
print()

# 5. Find all characters whose Role is "Hacker"

print("----Exercise 5----")
print(characters[characters["Role"] == "Hacker"])
print()

# 6. Create a Boolean Series called high_level that is True when Level >= 70

print("----Exercise 6----")
high_level = pd.Series(characters["Level"] >= 70)
print(high_level)
print()

# 7. Find all characters from "Nigth City"

print("----Exercise 7----")
print(characters[characters["City"] == "Night City"].to_string(index=False))
print()

# 8. Find the character with the most hours played

print("----Exercise 8----")

def highest_hours(characters):

    highest = 0
    highest_index = 0

    for index, character in enumerate(characters["Hours_Played"]):
        if(character > highest):
            highest = character
            highest_index = index
    
    return characters.iloc[highest_index]

print(highest_hours(characters))
print()

# 9. Find the average Hours_Played

print("----Exercise 9----")

def avg_hours(characters):
    
    sum_hours = 0
    average = 0

    for hours in characters["Hours_Played"]:
        sum_hours += hours

    average = sum_hours/(characters.shape[0])
    return average

print(avg_hours(characters))
print()

# 10. Find all characters who have played more than 400 hours AND have a Level greater than 70

print("----Exercise 10----")

print(characters[(characters["Hours_Played"] > 400) & (characters["Level"] > 70)].to_string(index = False))
print()

# 11. Find all characters whose favorite weapon is "Sword"

print("----Exercise 11----")

sword_characters = characters[characters["Favorite_Weapon"] == "Sword"]
print(sword_characters)


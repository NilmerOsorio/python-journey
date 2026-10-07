import pandas as pd

df = pd.DataFrame({
    "Name": [
        "Aragorn", "Legolas", "Gandalf", "Gimli", "Boromir", "Arwen",
        "Frodo", "Samwise", "Merry", "Pippin", "Galadriel", "Elrond",
        "Thorin", "Bilbo", "Saruman", "Sauron", "Éowyn", "Faramir"
    ],
    "Race": [
        "Human", "Elf", "Maia", "Dwarf", "Human", "Elf",
        "Hobbit", "Hobbit", "Hobbit", "Hobbit", "Elf", "Elf",
        "Dwarf", "Hobbit", "Maia", "Maia", "Human", "Human"
    ],
    "Class": [
        "Warrior", "Ranger", "Mage", "Warrior", "Warrior", "Mage",
        "Rogue", "Support", "Rogue", "Rogue", "Mage", "Mage",
        "Warrior", "Rogue", "Mage", "Mage", "Warrior", "Ranger"
    ],
    "Faction": [
        "Gondor", "Mirkwood", "Istari", "Erebor", "Gondor", "Rivendell",
        "Hobbiton", "Hobbiton", "Hobbiton", "Hobbiton", "Lothlórien",
        "Rivendell", "Erebor", "Hobbiton", "Isengard", "Mordor",
        "Rohan", "Gondor"
    ],
    "Level": [
        20, 18, 25, 17, 15, 19,
        8, 7, 6, 5, 28, 24,
        21, 10, 23, 35, 16, 14
    ],
    "Weapon": [
        "Andúril", "Bow", "Glamdring", "Axe", "Sword", "Sword",
        "Sting", "Sword", "Sword", "Sword", "Dagger", "Sword",
        "Orcrist", "Sting", "Staff", "Mace", "Sword", "Bow"
    ],
    "HP": [
        150, 120, 200, 160, 140, 130,
        80, 75, 70, 65, 180, 170,
        175, 90, 190, 300, 125, 135
    ],
    "Attack": [
        92, 88, 85, 90, 84, 72,
        55, 50, 48, 45, 70, 68,
        94, 58, 80, 100, 82, 78
    ],
    "Defense": [
        88, 75, 92, 95, 80, 70,
        55, 60, 52, 50, 85, 82,
        90, 58, 75, 95, 72, 76
    ],
    "Magic": [
        30, 25, 100, 20, 10, 95,
        15, 10, 12, 8, 100, 98,
        15, 10, 90, 100, 20, 15
    ],
    "Location": [
        "Minas Tirith", "Mirkwood", "Middle-earth", "Erebor",
        "Gondor", "Rivendell", "Hobbiton", "Hobbiton",
        "Hobbiton", "Hobbiton", "Lothlórien", "Rivendell",
        "Erebor", "Hobbiton", "Isengard", "Mordor",
        "Rohan", "Gondor"
    ]
})

print(df)
print()

# 1. Select a single column
# Select the Name column and print it.

print("----Exercise 1----")

print(df["Name"])
print()

# 2. Select multiple columns
# Select only Name, Level, and Weapon.

print("----Exercise 2----")

print(df[["Name", "Level", "Weapon"]])
print()

# 3. Select one row
# Select the row belonging to Gandalf using its index.

print("----Exercise 3----")

print(df.iloc[2])
print()

# 4. Select multiple rows
# Select the rows for Legolas, Gandalf, and Gimli using their indexes.

print("----Exercise 4----")

print(df.iloc[1:4])
print()

# 5. Select specific rows AND columns
# Select Aragorn and Boromir, but only display their Name, Weapon, and HP.

print("----Exercise 5----")

print(df.loc[[0,4], ["Name", "Weapon", "HP"]])
print()

# 6. Boolean selection
# Create a boolean Series that tells you which characters have a Level greater than 18.

print("----Exercise 6----")

print(df["Level"] > 18)
print()

# 7. Filter the DataFrame
# Use that boolean condition to display only characters whose level is greater than 18.

print("----Exercise 7----")

print(df[df["Level"] > 18])
print()

# 8. Challenge
# Display the Name and Weapon of every character whose HP is at least 150.

print("---Exercise 8----")

print(df.loc[df["HP"] >= 150, ["Name", "Weapon"]])
print()

# 9. Mini challenge
# Find all Warriors and display only their Name and Level.

print("----Exercise 9----")

print(df.loc[df["Class"] == "Warrior", ["Name", "Level"]])
print()

# 10. Final challenge
# Find all characters who:
# use a Sword
# and have at least Level 18
# Display only their Name, Level, and Weapon.

print("----Exercise 10----")

print(df.loc[(df["Weapon"] == "Sword") & (df["Level"] >= 18), ["Name", "Level", "Weapon"]])
print()

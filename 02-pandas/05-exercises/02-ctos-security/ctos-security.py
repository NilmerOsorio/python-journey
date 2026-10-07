import pandas as pd

hackers = {
    "Name": ["Aiden Pearce", "Marcus Holloway", "Wrench", "T-Bone Grady", "Sitara Dhawan", "Jordi Chin"],
    "City": ["Chicago", "San Francisco", "San Francisco", "Chicago", "San Francisco", "Chicago"],
    "Age": [39, 24, 28, 52, 26, 37],
    "Skill": [9.5, 9.0, 8.8, 9.8, 8.5, 8.0],
    "Reputation": [95, 92, 89, 97, 90, 85]
}

df_hackers = pd.DataFrame(hackers)

print(df_hackers)
print()

# 1. Using your DataFrame:
# Display the first 3 rows.
# Display the last 2 rows.
# Display the column names.
# Display the shape of the DataFrame.

print("----Exercise 1----")

print("----Display the frist 3 rows----")
print(df_hackers.iloc[[0, 1, 2]])
print()

print("----Display the last two rows----")
print(df_hackers.iloc[[4, 5]])

print("----Display the column names----")
print(df_hackers.columns.tolist())

print("----Display the shape of the DataFrame----")
print(df_hackers.shape)
print()

# 2. Access information
# Print only the Name column.
# Then print only the Skill column.
# Then print both Name and Reputation.

print("----Exercise 2----")

print("----Print only the name column----")
print(df_hackers["Name"].to_string(index = False))
print()

print("----Then print only the Skill column----")
print(df_hackers[["Skill"]].to_string(index = False))
print()

print("----Then print both Name and Reputation----")
print(df_hackers[["Name", "Reputation"]].to_string(index = False))
print()

# 3. Find Aiden: 
# Display the row containing Aiden Pearce.
# Then display the row containing Marcus Holloway.

print("----Exercise 3----")

print("----Display the row containing Aiden Pearce----")
print(df_hackers[df_hackers["Name"] == "Aiden Pearce"])
print()

print("----Then display the row containing Marcus Holloway----")
print(df_hackers[df_hackers["Name"] == "Marcus Holloway"])
print()

# 4. Elite hackers:
# Create a Boolean condition that checks whether each hacker has a: Skill >= 9.0 and print the Boolean result.
# Then use it to create a new DataFrame containing only the elite hackers.

print("----Exercise 4----")

print("----Create a Boolean condition that checks whether each hacker has a: Skill >= 9.0 and print the Boolean result----")
print(df_hackers["Skill"] >= 9.0)
print()

print("----Elite Hackers----")
elite_hackers = df_hackers[df_hackers["Skill"] >= 9.0]
print(elite_hackers)
print()

# 5. Chicago operation:
# Create a DataFrame containing only hackers who are from: Chicago
# Then create another one containing only hackers from: San Francisco

print("----Exercise 5----")

print("----Create a DataFrame containing only hackers who are from: Chicago----")
chicago_hackers = df_hackers[df_hackers["City"] == "Chicago"]
print(chicago_hackers)
print()

print("----Then create another one containing only hackers from: San Francisco----")
san_francisco_hackers = df_hackers[df_hackers["City"] == "San Francisco"]
print(san_francisco_hackers)
print()

# 6. High reputation
# Find every hacker whose reputation is greater than 90.
# Don't manually select the names.
# Make Pandas do the work. 

print("----Exercise 6----")

print("----Find every hacker whose reputation is greater than 90----")
print(df_hackers[df_hackers["Reputation"] > 90])
print()

# 7. Combining conditions 
# Now CTOS gets more interesting.
# Find hackers who:
# are from San Francisco
# AND have a Skill of at least 8.5
# You'll need to combine two conditions.

print("----Exercise 7----")

print("----Find hackers who: are from San Francisco AND have a Skill of at least 8.5")
print(df_hackers[(df_hackers["City"] == "San Francisco") & (df_hackers["Skill"] >= 8.5)])
print()

# 8. Adding a new hacker

# DedSec recruits someone new:
# Name: Raymond Kenney
# City: Chicago
# Age: 55
# Skill: 9.9
# Reputation: 99
# Add him to your DataFrame.
# Add two more characters.
# Then print the DataFrame again.

print("----Exercise 8----")

new_hackers = pd.DataFrame([{
    "Name": "Raymond Kenney",
    "City": "Chicago",
    "Age": 55,
    "Skill": 9.9,
    "Reputation": 99
},
{
    "Name": "Josh Sauchak",
    "City": "San Francisco",
    "Age": 25,
    "Skill": 8.7,
    "Reputation": 91
},
{
    "Name": "Horatio Carlin",
    "City": "San Francisco",
    "Age": 27,
    "Skill": 8.3,
    "Reputation": 86
}], index = [6, 7, 8])

df_hackers = pd.concat([df_hackers, new_hackers])

print(df_hackers)
print()

# 9. Add a new column:
# Create a new column called:
# Wanted
# A hacker is considered wanted if their reputation is greater than 90.
# So your DataFrame should eventually have something like:
# Name              Reputation    Wanted
# Aiden Pearce          95          True
# Marcus Holloway       92          True
# Wrench                89          False
# ...

print("----Exercise 9----")

df_hackers["Wanted"] = df_hackers["Reputation"] > 90
print(df_hackers)
print()

# 10. Final Mission — Take down CTOS
# Starting with your complete DataFrame, answer these using Pandas:
# 1. Who's the oldest hacker?
# 2. Who has the highest Skill?
# 3. Which hackers have a Reputation below 90?
# 4. Which hackers are from Chicago and have a Skill above 9.0?
# 5. How many hackers are in the database?
# 6. How many hackers are wanted?
# 7. Create a DataFrame containing only the name, city, and skill of hackers with Skill ≥ 9.0.

print("----Exercise 10----")

print("----Who's the oldest hacker?----")
print(df_hackers.nlargest(1, "Age"))
print()

print("----Who has the highest skill?----")
print(df_hackers.nlargest(1, "Skill"))
print()

print("----Which hackers have a Reputation below 90?----")
print(df_hackers[df_hackers["Reputation"] < 90])
print()

print("----Which hackers are from Chicago and have a Skill above 9.0?----")
print(df_hackers[(df_hackers["City"] == "Chicago") & (df_hackers["Skill"] > 9.0)])
print()

print("----How many hackers are in the database?----")
print(df_hackers.shape[0])
print()

print("----How many hackers are wanted?----")
print(df_hackers[df_hackers["Wanted"] == True].shape[0])
print()

print("----Create a DataFrame containing only the name, city, and skill of hackers with Skill ≥ 9.0----")
best_hackers = df_hackers[df_hackers["Skill"] >= 9.0][["Name", "City", "Skill"]]
print(best_hackers)


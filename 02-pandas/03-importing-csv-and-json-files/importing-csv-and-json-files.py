import pandas as pd

#Importing a CSV file
df = pd.read_csv("anime.csv")

# In case the CSV file is too huge, it only shows the first five rows and the last five rows
print(df)
print()
print("----" * 50)

# If we want to see all of the rows we can use the method to_string()
print(df.to_string())
print()

#Importing JSON

df_watch_dogs = pd.read_json("watch_dogs_dataset.json")
print(df_watch_dogs)


import pandas as pd

# Pass a second argument as a keyword argument.
# It makes it easier to look for data.
anime = pd.read_csv("anime.csv", index_col="author")

# Selection by column
# When there is a lot of data to display, Pandas prints the first 5 rows
# and the last 5 rows by default.
print(anime["title"])
print()

# Use .to_string() to display the entire column.
print(anime["title"].to_string())
print()

# Set index=False to hide the index in the output.
print(anime["title"].to_string(index=False))
print()

# Print multiple columns
print(anime[["title", "genre", "episodes"]])

# Selection by rows
print(anime.loc["Tite Kubo"])
print()

print(anime.loc["Eiichiro Oda"])
print()

# Pass a list of columns to display only the selected data.
print(anime.loc["Tite Kubo", ["title", "episodes", "rating"]])
print()

print(anime.loc["Eiichiro Oda", ["title", "episodes", "rating"]])
print()

print(anime.loc["Sui Ishida", ["title", "episodes", "rating"]])
print()

# A range of rows can also be selected.
print(anime.loc["Tite Kubo": "Gege Akutami", ["title", "episodes", "rating"]])
print()

# Select a row by its integer position.
print(anime.iloc[0])
print()

# Select a range of rows as well
# The second number is exclusive
print(anime.iloc[0:11])
print()

# The third value sets the step, so the selection moves two rows at a time.
print(anime.iloc[0:11:2])
print()

print(anime.iloc[0:11:3])
print()

# Select every other row from index 0 to 10 and columns from index 0 to 2.
print(anime.iloc[0:11:2, 0:3])
print()

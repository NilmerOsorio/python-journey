import pandas as pd

data = {
    "Name": ["SpongeBob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

print(df)

print()

# Accesing data

print("----Accesing data----")
print(df.loc["Employee 1"])
print("--" * 10)
print(df.loc["Employee 2"])
print("--" * 10)
print(df.loc["Employee 3"])

print()

print("----It's also possible to access the data using integer position----")
print(df.iloc[0])
print("--" * 10)
print(df.iloc[1])
print("--" * 10)
print(df.iloc[2])

# Add a new column

print("----Add a new column----")
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)

print()

# Add new rows

print("----Add new rows----")
new_rows = pd.DataFrame([{
    "Name": "Sandy",
    "Age": 28,
    "Job": "Engineer"
},
{
    "Name": "Eugene",
    "Age": 60,
    "Job": "Manager"
}], index = ["Employee 4", "Employee 5"])

df = pd.concat([df, new_rows])

print(df)
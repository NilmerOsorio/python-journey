# 🐼 Pandas DataFrame Exercises

A set of exercises to practice **Pandas DataFrames** and data selection using a *Lord of the Rings*-themed dataset.

## 📚 What I Learned

* Creating DataFrames with `pd.DataFrame()`
* Selecting single and multiple columns
* Selecting rows with `.iloc`
* Selecting rows and columns with `.loc`
* Creating Boolean conditions
* Filtering DataFrames
* Filtering text and numerical values
* Combining multiple conditions with `&`

## 🧠 Key Concepts

```python
df["Name"]                         # Select a column
df[["Name", "Level"]]              # Select multiple columns
df.iloc[2]                         # Select a row by index
df.loc[[0, 4], ["Name", "HP"]]     # Select rows and columns
df[df["Level"] > 18]               # Filter data
```

## 🛠️ Technologies

* 🐍 Python
* 🐼 Pandas

## 🎯 Goal

Practice the fundamentals of **selecting and filtering data with Pandas** before moving on to more advanced data analysis concepts.

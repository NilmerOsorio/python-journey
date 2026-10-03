# 🐼 Pandas — Importing CSV & JSON Files

This project is a small practice exercise where I learned how to **import CSV and JSON files into Python using Pandas**.

## 📚 What I Learned

* Importing Pandas with `import pandas as pd`
* Reading CSV files with `pd.read_csv()`
* Reading JSON files with `pd.read_json()`
* Working with imported data as Pandas **DataFrames**
* Displaying DataFrames with `print()`
* Using `.to_string()` to display all rows

## 📄 Importing a CSV File

I used an anime dataset to practice importing CSV data:

```python
import pandas as pd

df = pd.read_csv("anime.csv")

print(df)
print(df.to_string())
```

By default, Pandas displays a shortened version of large DataFrames. The `.to_string()` method can be used when I want to display the complete DataFrame.

## 🔶 Importing a JSON File

I also practiced importing JSON data using a Watch Dogs dataset:

```python
df_watch_dogs = pd.read_json("watch_dogs_dataset.json")

print(df_watch_dogs)
```

## ⚖️ CSV vs JSON

| File    | Pandas Method    |
| ------- | ---------------- |
| `.csv`  | `pd.read_csv()`  |
| `.json` | `pd.read_json()` |

Both methods allow the data to be loaded into a **DataFrame**, which can then be analysed and manipulated using Pandas.

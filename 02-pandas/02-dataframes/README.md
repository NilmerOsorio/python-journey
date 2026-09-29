# 🐼 Pandas DataFrames

In this lesson, I learned the basics of **DataFrames** using Pandas.

## 📊 Creating a DataFrame

A DataFrame is a table-like structure made of rows and columns.

```python
import pandas as pd

data = {
    "Name": ["SpongeBob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
```

## 🔍 Accessing Data

### `.loc[]`

Access data using the **index label**:

```python
df.loc["Employee 1"]
```

### `.iloc[]`

Access data using the **integer position**:

```python
df.iloc[0]
```

> `loc` → label
> `iloc` → position

## ➕ Adding a Column

```python
df["Job"] = ["Cook", "N/A", "Cashier"]
```

## ➕ Adding Rows

Create another DataFrame and combine it with the original:

```python
df = pd.concat([df, new_rows])
```

## 🧠 Key Takeaways

* `pd.DataFrame()` → creates a DataFrame.
* `index` → defines row labels.
* `.loc[]` → accesses rows by label.
* `.iloc[]` → accesses rows by position.
* `df["Column"]` → adds a column.
* `pd.concat()` → combines DataFrames.

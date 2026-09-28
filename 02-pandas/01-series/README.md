# 🐼 Pandas Series

This practice covers the basic concepts of **Pandas Series**, a one-dimensional data structure used to store values together with their indexes.

## 📚 Summary

A Series can be created from a **list** and optionally assigned custom indexes:

```python
data = [100, 102, 104]
series = pd.Series(data, index=["a", "b", "c"])
```

Each value is associated with an index:

```text
a → 100
b → 102
c → 104
```

### 🔎 Accessing Data

There are two main ways to access values:

* **`.loc[]`** → access using the index label.
* **`.iloc[]`** → access using the integer position.

```python
series.loc["a"]   # 100
series.iloc[0]    # 100
```

### ✏️ Updating Data

Values can be modified through their index:

```python
series.loc["c"] = 200
```

### 🔍 Filtering Data

Series can be filtered using Boolean conditions:

```python
series[series >= 200]
```

This returns only the values that satisfy the condition.

Other examples:

```python
series[series < 200]
series[series == 100]
```

### 📖 Series from Dictionaries

A dictionary can also be converted into a Series. The **keys become the indexes** and the **values remain the data**:

```python
calories = {
    "Day 1": 1700,
    "Day 2": 2100,
    "Day 3": 1700
}

series = pd.Series(calories)
```

This is useful when the data already has meaningful labels.

## 🧠 Key Takeaways

* A **Series** is a one-dimensional labeled data structure.
* It contains **indexes and values**.
* `.loc[]` uses labels, while `.iloc[]` uses positions.
* Values can be updated directly.
* Boolean conditions can be used to filter data.
* Lists and dictionaries can both be used to create Series.

> **Main idea:** Pandas Series make it easier to organize, access, modify, and filter one-dimensional data.

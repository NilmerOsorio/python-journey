# Pandas Series Practice 🐼

Practice exercises for learning **Pandas Series** with Python.

## Topics

* Creating Series
* Accessing values
* Filtering data
* Boolean conditions
* Boolean indexing
* Comparing values

## Example

```python
passed = my_series > 3.0
print(passed)
```

This creates a Boolean Series with `True` or `False` depending on whether each value is greater than `3.0`.

```python
print(my_series[my_series > 3.0])
```

This filters the Series and returns only the values greater than `3.0`.

## Goal

Practice the basics of **Pandas Series** and get more comfortable working with conditions and filtering.

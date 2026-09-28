import pandas as pd

data = [100, 102, 104]

series = pd.Series(data, index = ["a", "b", "c"])

print(series)

print()
# Accesing data
print("----Accesing data----")
print(series.loc["a"])
print(series.loc["b"])
print(series.loc["c"])

print() 

print("----It's also possible to access the data using integer position----")
print(series.iloc[0])
print(series.iloc[1])
print(series.iloc[2])

print()
# Updating data
print("----Updating data----")

series.loc["c"] = 200

print(series)

print()
# Filtering series data
print("----Filtering series data----")
my_second_data = [100, 102, 104, 200, 202]

print()

my_second_series = pd.Series(my_second_data, index = ["a", "b", "c", "d", "e"])
print(my_second_series)

print()

print("----Return any values from the series that are greather than or equal to 200----")
print(my_second_series[my_second_series >= 200])

print()

print("----Return any values from the series that are smaller than 200----")
print(my_second_series[my_second_series < 200])

print()
# We can also use a dictionary to make series
print("----We can also use a dictionary to make series----")
calories = {"Day 1": 1700, "Day 2": 2100, "Day 3": 1700}

my_third_series = pd.Series(calories)

print(my_third_series)

print()

print("----Let's see how many calories I've eaten each day----")
print("----using the loc property----")

print(my_third_series.loc["Day 1"])
print(my_third_series.loc["Day 2"])
print(my_third_series.loc["Day 3"])

print()

# Updating data
print("----Updating data----")
print("----I cheated in my third day since I ate a biscuit----")

my_third_series["Day 3"] += 500

print(my_third_series)

print()

# Filtering data
print("----Filtering data----")
print("----I want to see which days I didn't follow my diet----")
print(my_third_series[my_third_series >= 2000])

print()

print("----I want to see which days I followed my diet----")
print(my_third_series[my_third_series <  2000])
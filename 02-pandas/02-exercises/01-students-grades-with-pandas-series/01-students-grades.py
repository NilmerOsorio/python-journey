import pandas as pd

students = {
    "Charles": 4.2,
    "Laura": 3.8,
    "Andrew": 4.5,
    "Sophie": 2.9,
    "Matthew": 3.6,
    "Valentina": 4.8
}

my_series = pd.Series(students)

print(my_series)

print()

# 1. Accessing data: Get Laura's mark, and then Sophie's grade
print("----Exercise 1----")
print(my_series.loc["Laura"])
print(my_series.loc["Sophie"])

print()

# 2. Basic information: 
# Find:
# The highest mark.
# The lowest mark.
# The average mark.

print("----Exercise 2----")

def highest_mark(my_series):

    highest = 0 

    for marks in my_series:

        if (marks > highest):
            highest = marks

    return highest

def lowest_mark(my_series):

    lowest = my_series.iloc[0]

    for marks in my_series:

        if (marks < lowest):
            lowest = marks
    
    return lowest

def average(my_series):

    total_sum = 0
    average = 0

    for marks in my_series:
        total_sum += marks

    average = total_sum/len(my_series)

    return average
    
print(f"The highest mark is: ", highest_mark(my_series))
print(f"The lowest mark is: ", lowest_mark(my_series))
print(f"The average mark is: ", average(my_series))

print()


# 3. Filtering:
# Create a new Series containing only students who passed.
# Assume that the passing grade is: 3.0
print("----Exercise 3----")

passing_students = pd.Series(my_series[my_series > 3.0])

print(passing_students)

print()

# 4. Add a new student without recreating the entire Series.
print("----Exercise 4----")
my_series.at["Daniel"] = 3.4

print(my_series)

print()

# 5. Challenge: create a boolean Series that tells you whether each student passed.
print("----Exercise 5----")
passed = my_series > 3.0

print(passed)

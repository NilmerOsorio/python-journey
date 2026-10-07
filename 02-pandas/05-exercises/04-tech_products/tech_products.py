import pandas as pd

# 1. Load the JSON:Import Pandas and load the JSON file into a DataFrame.
# Print the DataFrame.

print("----Exercise 1----")

tech_products = pd.read_json("tech_products.json")
print(tech_products.to_string())

print()

# 2. Inspect the DataFrame
# Print:
# the first 5 rows
# the last 5 rows
# the shape
# the column names

print("----Exercise 2----")

print("----Print the first 5 rows----")
print(tech_products.iloc[[0, 1, 2, 3, 4]])
print()

print("----Print the last 5 rows----")
print(tech_products.tail(5).to_string())
print()

print("----Print the shape----")
print(tech_products.shape)
print()

print("----Print the column names----")
print(tech_products.columns.tolist())
print()

# 3. Select columns
# Print only:
# Product
# Company
# Price

print("----Exercise 3----")

print(tech_products[["Product", "Company", "Price"]])
print()

# 4. Find expensive products
# Find all products whose price is greater than $500.
# Store the result in a variable called: expensive_products

print("----Exercise 4----")

expensive_products = tech_products[tech_products["Price"] > 500]
print(expensive_products)
print()

# 5. Find highly-rated products
# Find all products with a rating greater than or equal to 4.7.

print("----Exercise 5----")

best_rating = tech_products[tech_products["Rating"] >= 4.7]
print(best_rating.to_string(index = False))
print()

# 6. Boolean Series practice
# Create a Boolean Series that tells you whether each product has more than 100 million users.
# Something like:
# 0     True
# 1     False
# 2     True
# ...
# Don't filter the DataFrame yet. I specifically want you to practice recognizing that a condition by itself produces a Boolean Series.

print("----Exercise 6----")

print(tech_products["Users_Millions"] > 100)
print()

# 7. Combine conditions
# Find products that satisfy both:
# Rating ≥ 4.5
# Users > 50 million

print("----Exercise 7----")

print(tech_products[(tech_products["Rating"] >= 4.5) & (tech_products["Users_Millions"] > 50)])
print()

# 8. AI products
# Find all products where:
# AI_Powered == True

print("----Exercise 8----")

print(tech_products[tech_products["AI_Powered"] == True].to_string(index = False))
print()

# 9. Gaming products
# Find all products whose category is:
# Gaming

print("----Exercise 9----")

print(tech_products[tech_products["Category"] == "Gaming"].to_string(index = False))
print()

# 10. Expensive AI products
# Find products that are:
# AI-powered
# AND cost more than $1,000

print("----Exercise 10----")

print(tech_products[(tech_products["AI_Powered"] == True) & (tech_products["Price"] > 1000)].to_string(index = False))
print()

# 11. Pick one column and calculate
# Find the average price of all the products.

print("----Exercise 11----")

def average_price(tech_products):

    sum = 0
    avg = 0

    for price in tech_products["Price"]:
        sum += price

    avg = sum/(tech_products.shape[0])
    rounded_avg = round(avg, 4)

    return rounded_avg

print(average_price(tech_products))
print()

# 12. Challenge
# Find all products released after 2020 that have a rating above 4.5.

print("----Exercise 12----")

print(tech_products[(tech_products["Release_Year"] > 2020) & (tech_products["Rating"] > 4.5)].to_string(index = False))
print()

# 13. Find the product with the highest number of users.

print("----Exercise 13----")

def most_used(tech_products):

    highest = 0
    biggest_index = 0

    for index, users in enumerate(tech_products["Users_Millions"]):
        if(users > highest):
            highest = users
            biggest_index = index

    return tech_products.iloc[biggest_index]

print(most_used(tech_products))

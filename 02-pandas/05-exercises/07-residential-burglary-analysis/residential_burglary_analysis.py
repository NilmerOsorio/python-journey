import pandas as pd

# Importing the CSV file
df = pd.read_csv("HURTO_A_RESIDENCIAS_20261012.csv")

# In case the CSV file is too huge, it only shows the first five rows and the last five rows
print(df)
print()
print("----" * 50)

# If we want to see all of the rows we can use the method to_string()
# print(df.to_string())
# print()
# print("----" * 50)

# The shape attribute returns a Python tuple containing two numbers: (number_of_rows, number_of_columns)
print("----Shape of the DataFrame----")
print(df.shape)
print()
print("----" * 50)

# Identify the columns available in the dataset
print("----Column Names----")
print(df.columns)
print()
print("----" * 50)

# Check the data types of the required columns
print("----Data Types----")
print(df[["DEPARTAMENTO", "CANTIDAD", "FECHA HECHO"]].dtypes)
print()
print("----" * 50)

# Challenge: Inspect the DataFrame structure and data types
print("----DataFrame Information----")
df.info()
print()
print("----" * 50)

# Display the first five records
print("----First Five Records----")
print(df.head())
print()
print("----" * 50)

# Generate descriptive statistics for numerical columns
print("----Descriptive Statistics----")
print(df.describe())
print()
print("----" * 50)

# Rename the columns
print("----Renaming Columns----")
df = df.rename(columns = {
    "FECHA HECHO": "fecha",
    "COD_DEPTO": "cod_depto",
    "DEPARTAMENTO": "departamento",
    "COD_MUNI": "cod_muni",
    "MUNICIPIO": "municipio",
    "TIPO DELITO": "tipo_delito",
    "CANTIDAD": "cantidad"
})
print(df.columns)
print()
print(df.head())
print()
print("----" * 50)

# Convert fecha into a date type
print("----Converting data type----")
df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y")
print()
print("----" * 50)

# Verify the converted date data type
print("----Updated DataFrame Information----")
df.info()
print()
print("----" * 50)

#----------------------------------------------------------------#
#----------------------ACTIVITIES TO SOLVE-----------------------#
#----------------------------------------------------------------#

print("----------------------------------------------------------------")
print("----------------------ACTIVITIES TO SOLVE-----------------------")
print("----------------------------------------------------------------")

# 1. Display the records for a category, showing three columns of your choice, sorted by value from highest to lowest. 
# Change the category to one that doesn't exist and explain the result.

print("\n" + "=" * 80)
print("EXERCISE 1".center(80))
print("=" * 80)

print("Description:")
print("Display the records for a category, showing three columns of your choice,")
print("sorted by value from highest to lowest.")
print("Change the category to one that doesn't exist and explain the result.")
print("=" * 80)

# Part 1: Define a category that exists in the dataset
category = "SANTANDER"

# Filter records by department, select three columns, and sort
def first_exercise(df, category):
    category_records = df[df["departamento"] == category][["fecha", "municipio", "cantidad"]].sort_values(by="cantidad", ascending = False)

    return category_records.head(10)

# Display results for the existing category
print(f"\n---- Results for Category: {category} ----")

category_records = first_exercise(df, category)
print(category_records)

# Part 2: Test a category that does not exist in the dataset
category = "ATLANTIS"

print(f"\n---- Results for Category: {category} ----")

category_records = first_exercise(df, category)
print(category_records)

# Explanation:
# When the category is changed to `"ATLANTIS"`, the function returns an empty DataFrame 
# because there are no records in the dataset whose `departamento` value matches that 
# category. The selected columns remain visible, but the index is empty because no rows satisfy the 
# filtering condition. This is expected behavior and doesn't represent an error.

print()
print("----" * 50)



# 2. Count how many records exceed a value you define and display the ten highest values. 
# What happens if that value is greater than the maximum in your table?

print("\n" + "=" * 80)
print("EXERCISE 2".center(80))
print("=" * 80)

print("Description:")
print("Count how many records exceed a value you define and display the ten")
print("highest values.")
print("What happens if that value is greater than the maximum in your table?")
print("=" * 80)

# Part 1: Define a threshold within the dataset's range
value_threshold = 1

# Filter records above the specified threshold and sort them
def second_exercise(df, value_threshold):
    filtered_records = df[df["cantidad"] > value_threshold].sort_values(by="cantidad", ascending=False)

    print(f"Threshold: {value_threshold}")
    print(f"Number of matching records: {filtered_records.shape[0]}")

    print("\n---- Ten Highest Values ----")
    print(filtered_records.head(10))

    return filtered_records

# Display results using the initial threshold
print("\n---- Results Within the Dataset's Range ----")
filtered_records = second_exercise(df, value_threshold)

# Part 2: Test a threshold above the dataset's maximum
value_threshold = 10

print("\n---- Results Above the Dataset's Maximum ----")
filtered_records = second_exercise(df, value_threshold)

# Explanation:
# When the threshold is set to `10`, the filtering operation returns an empty DataFrame 
# because the maximum value in the `cantidad` column is `7`. 
# Consequently, no records satisfy the condition `cantidad > 10`, 
# and the number of matching records is zero.

print()
print("----" * 50)



# 3. Display the records between two dates, ordered by date. 
# Explain what happens if you write the most recent date first.

print("\n" + "=" * 80)
print("EXERCISE 3".center(80))
print("=" * 80)

print("Description:")
print("Display the records between two dates, ordered by date.")
print("Explain what happens if you write the most recent date first.")
print("=" * 80)

# Define the date range
start_date = pd.to_datetime("01/08/2026", format="%d/%m/%Y")
end_date = pd.to_datetime("31/08/2026", format="%d/%m/%Y")

# Filter records within the specified date range
def third_exercise(df, start_date, end_date):

    filtered_records = df[(df["fecha"] >= start_date) & (df["fecha"] <= end_date)].sort_values(by="fecha")

    return filtered_records

# Part 1: Use the dates in chronological order
print("\n---- Results Using the Correct Date Range ----")
date_records = third_exercise(df, start_date, end_date)

print(f"Number of matching records: {date_records.shape[0]}")
print(date_records.head(10))

# Part 2: Reverse the dates to test the filtering condition
print("\n---- Results With Reversed Dates ----")
reversed_records = third_exercise(df, end_date, start_date)

print(f"Number of matching records: {reversed_records.shape[0]}")
print(reversed_records.head(10))

# Explanation:
# When the most recent date is provided first, the function returns an empty 
# DataFrame because the start date is later than the end date. No record can 
# satisfy both date conditions simultaneously. The selected columns remain visible,
# but the index is empty because no rows match the filtering criteria. 
# To obtain the expected results, the start date must be earlier than or equal 
# to the end date.

print()
print("----" * 50)



# 4. Display the records in a category whose value is above the average for the entire table.
# Explain why the result would be different if compared against the average for that category.

print("\n" + "=" * 80)
print("EXERCISE 4".center(80))
print("=" * 80)

print("Description:")
print("Display the records in a category whose value is above the average")
print("for the entire table.")
print("Explain why the result would be different if compared against the")
print("average for that category.")
print("=" * 80)

# Define the category to analyze
category = "SANTANDER"

# Calculate the mean of cantidad across the entire dataset
overall_mean = df["cantidad"].mean()
print(f"Overall mean: {overall_mean}")

# Filter records by department and a given mean threshold
def fourth_exercise(df, mean_threshold, category):

    filtered_records = df[(df["departamento"] == category) & (df["cantidad"] > mean_threshold)]
    print(f"Number of matching records: {filtered_records.shape[0]}")

    return filtered_records

# Part 1: Use the overall dataset mean (required by the challenge)
print("\n---- Results Using the Overall Mean ----")
print(fourth_exercise(df, overall_mean, category))
print()

# Part 2: Calculate the selected department's mean
category_mean = df[df["departamento"] == category]["cantidad"].mean()
print(f"\nCategory mean for {category}: {category_mean}")

# Compare the results using the department's own mean
print("\n---- Results Using the Category Mean ----")
print(fourth_exercise(df, category_mean, category))

# Explanation: 
# The overall mean of the `cantidad` column is approximately 1.001682, while the 
# mean for Santander is approximately 1.001487. Although these values are different,
#  both means lie between 1 and 2. Since `cantidad` contains integer values, both 
# conditions select records with a value of at least 2. Therefore, both approaches
# return the same 38 records.
# In general, the results can differ because a category's mean may be higher or 
# lower than the mean of the entire dataset. This changes the threshold used to 
# filter the records and can therefore change the number of records returned.

print()
print("----" * 50)



# 5. Display the n records with the highest values ​​for a category. 
# What happens if n is greater than the number of existing records?

print("\n" + "=" * 80)
print("EXERCISE 5".center(80))
print("=" * 80)

print("Description:")
print("Display the n records with the highest values for a category.")
print("What happens if n is greater than the number of existing records?")
print("=" * 80)

# Define the category to analyze
category = "SANTANDER"

# Filter records by category and sort by cantidad in descending order
def fifth_exercise(df, n, category):
    filtered_records = df[df["departamento"] == category].sort_values(by="cantidad", ascending=False)
    return filtered_records.head(n)

# Part 1: Display the 5 records with the highest values
n = 5

print(f"\n---- Top {n} Records for {category} ----")
print(fifth_exercise(df, n, category))
print()

# Part 2: Check what happens when n exceeds the number of available records
n = 1000000

result = fifth_exercise(df, n, category)

print(f"\n---- Results When n Exceeds Available Records ----")
print(f"Number of records returned: {result.shape[0]}")

# Explanation:
# When `n` is greater than the number of records available for the selected 
# category, the `head(n)` method returns all available records instead of raising
# an error. This happens because `head(n)` returns up to `n` records, not 
# necessarily exactly `n` records. For example, if we set `n = 1_000_000` and the
# selected category has fewer than one million records, the method returns every 
# record belonging to that category. We can verify this by using `.shape[0]`, 
# which tells us the actual number of records returned.
# 🏠 Residential Burglary Data Analysis with Pandas

## 📌 About the Project

This project was developed as part of the **Data Structures class at my university**, where we are learning to work with Python and Pandas.

The assignment involved working with a real-world dataset about residential burglary in Colombia. The goal was to practise data manipulation and analysis by completing five challenges involving filtering, sorting, numerical comparisons, and date ranges.

Through this activity, I strengthened my understanding of Pandas DataFrames, reusable functions, and how to test different inputs and edge cases.

## 📊 Dataset Information

The dataset, **HURTO A RESIDENCIAS**, was downloaded from Colombia's Open Data Portal.

- 🗂️ **Dataset:** HURTO A RESIDENCIAS
- 🔗 **Source:** [Colombia's Open Data Portal](https://www.datos.gov.co/Seguridad-y-Defensa/HURTO-A-RESIDENCIAS/7mn7-vzqp)
- 📁 **File format:** CSV
- 📄 **Number of records:** 615,764
- 📋 **Number of columns:** 7

The dataset contains information about incident dates, departments, municipalities, geographic identifiers, and reported quantities. The crime type column was empty in the downloaded file.

## 🛠️ Technologies Used

- 🐍 **Python** — Main programming language.
- 🐼 **Pandas** — Loading, exploring, filtering, sorting, and analysing tabular data.
- 💻 **Visual Studio Code (VS Code)** — Code editor used to develop and run the project.
- 🐙 **Git and GitHub** — Version control and project documentation.

## 💻 Challenges Completed

### 1. 🔎 Filtering and Sorting by Category

Filtered records by department, selected specific columns, and sorted them by quantity in descending order.

I also tested what happens when the selected category does not exist in the dataset.

### 2. 🔢 Filtering by a Numerical Threshold

Counted records whose quantity exceeded a specified value and displayed the ten records with the highest quantities.

I tested a threshold greater than the maximum value in the dataset to understand what happens when no records satisfy the condition.

### 3. 📅 Filtering by Date Range

Selected records between two dates and sorted them chronologically.

I also examined what happens when the start date is later than the end date.

### 4. 📊 Comparing Values Against an Average

Filtered records belonging to a selected department whose quantities exceeded the mean of the entire dataset.

I compared this result with using the mean calculated for the selected department to understand the difference between overall and category-specific averages.

### 5. 🏆 Selecting the Top N Records

Retrieved the top *n* records for a selected department, sorted by quantity in descending order.

I tested what happens when *n* exceeds the number of available records and learned that Pandas returns all available records instead of raising an error.

## 📚 What I Learned

Through these exercises, I practised:

1. 🗂️ **Working with DataFrames** — Loading CSV files and inspecting their dimensions, columns, data types, and descriptive statistics.
2. 🧹 **Data preparation** — Renaming columns and converting date strings into datetime objects.
3. 🔎 **Data filtering** — Applying Boolean conditions to select records that meet specific criteria.
4. ↕️ **Sorting data** — Ordering records by numerical values and dates.
5. 🧮 **Statistical analysis** — Calculating means and comparing values against different thresholds.
6. 🧩 **Reusable functions** — Using parameters and variables to make functions adaptable to different inputs.
7. 🧪 **Testing edge cases** — Understanding empty results, reversed date ranges, thresholds that exceed available values, and requests for more records than exist.
8. 🔍 **Interpreting results** — Examining outputs to understand why the code behaves differently under different conditions.

## 💡 Key Takeaways

This assignment helped me understand how to manipulate Pandas DataFrames and apply programming concepts to a real-world dataset.

I also learned the importance of writing reusable functions, testing different inputs, and considering edge cases rather than focusing only on expected results.

Working through the challenges step by step helped me strengthen both my Python skills and my ability to reason about data.

## 🎯 Conclusion

This project is part of my ongoing **Python development journey** and represents a practical application of concepts studied in my university's Data Structures class.

Each challenge gave me an opportunity to practise, experiment, and better understand how Python and Pandas can be used to explore and analyse structured data.

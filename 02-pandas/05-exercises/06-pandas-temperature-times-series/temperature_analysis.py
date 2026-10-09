import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

today = pd.Timestamp(datetime.today().date())

dates = pd.date_range(
    end=today,
    periods=1000,
    freq="D"
)

temperatures = (
    20
    + 5 * np.sin(np.linspace(0, 20 * np.pi, 1000))
    + np.random.normal(0, 1.5, 1000)
)

temperatures = np.round(temperatures, 1)

temp_serie = pd.Series(
    temperatures,
    index=dates,
    name="Temperature"
)

df_temp = temp_serie.reset_index()

df_temp.columns = ["Date", "Temperature"]

df_temp.to_excel(
    "1000_days_temperature.xlsx",
    index=False
)
print()

print("----Questions----")

# 1. What was the average temperature during those 1000 days?
print("----Exercise 1----")

def average_temperature(df_temp):

    sum = 0
    avg = 0

    for temp in df_temp["Temperature"]:
        sum += temp

    avg = sum/(df_temp.shape[0])
    rounded_avg = round(avg, 4)
    return rounded_avg

print(average_temperature(df_temp))
print()

# 2. How many days recorded a temperature higher than 25°C?
print("----Exercise 2----")

over25 = 0

for temp in df_temp["Temperature"]:
    if (temp > 25):
        over25 += 1

print(over25)
print()

# 3. What was the maximum temperature and on what date did it occur?
print("----Exercise 3----")

def maximum_temperature(df_temp):

    highest = 0
    highest_index = 0

    for index, temp in enumerate(df_temp["Temperature"]):
        if (temp > highest):
            highest = temp
            highest_index = index
    return df_temp.iloc[highest_index]

print(maximum_temperature(df_temp))
print()

# 4. Create a graph of the entire temperature series. Describe what you observe.

print("----Exercise 4----")

plt.title("Temperature over Time")
plt.plot(df_temp["Date"], df_temp["Temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

messagebox.showinfo(
    "Graph's description",
    "The temperature goes up and down following a repeating wave-like pattern. "
    "The temperatures fluctuate around an average of approximately 20°C, "
    "with random fluctuations throughout the series. "
    "The highest temperatures are around 30°C, while the lowest are around 10°C."
)
print()

# 5. Calculate a 30-day moving average and plot it over the original series. What are the advantages of this technique? (TIP: Use .rolling().mean().)

print("----Exercise 5----")

plt.plot(df_temp["Date"], df_temp["Temperature"])
thirty_day_avg = df_temp["Temperature"].rolling(30).mean()
plt.plot(df_temp["Date"],thirty_day_avg)
plt.show()

messagebox.showinfo(
    "Moving Average Explanation",
    "The 30-day moving average smooths the random fluctuations (noise) "
    "from the original temperature series. This makes it easier to identify "
    "general patterns and trends. The smoothed line stays roughly between "
    "15°C and 25°C, but this represents the average, not the actual daily temperatures."
)
print()

# 6. Filter the data between July 1, 2023, and December 31, 2026, and generate a new Series containing only the days with a temperature < 18°C.

print("----Exercise 6----")

low_temperatures = df_temp[((df_temp["Date"] >= '2023-07-1') & (df_temp["Date"] <= '2026-12-31')) & (df_temp["Temperature"] < 18)]["Temperature"]
print(low_temperatures.to_string())
print()

# 7. Research a library or technology (other than Pandas) used for processing time series at scale.

print("----Exercise 7----")

print("There's a README which has got the answer for this question")

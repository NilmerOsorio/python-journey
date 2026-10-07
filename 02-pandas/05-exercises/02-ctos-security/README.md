# 🐼💻 Watch Dogs — Pandas DataFrames Practice

A small **Python + Pandas** practice project where I worked with **DataFrames** using a fictional database of hackers from the **Watch Dogs universe**.

Instead of using a generic dataset, I created a **DedSec/CTOS-style database** containing information such as hackers, cities, skill levels, and reputation.

## 🎯 What I Practiced

Through several exercises, I practiced:

* Creating DataFrames with `pd.DataFrame()`
* Accessing rows and columns
* Using `iloc`, `columns`, and `shape`
* Filtering data with Boolean conditions
* Combining conditions with `&`
* Adding new rows with `pd.concat()`
* Creating new columns based on conditions

Example:

```python
elite_hackers = df_hackers[df_hackers["Skill"] >= 9.0]
```

This simulates CTOS identifying the most skilled hackers in the database.

## 🎮 Watch Dogs Theme

The exercises were built around characters such as **Aiden Pearce, Marcus Holloway, Wrench, T-Bone, Sitara, and Jordi**.

The dataset was also expanded with characters like **Raymond Kenney**, making the practice feel more like managing a real DedSec intelligence database.

## 🤖 Using AI Consciously

I used AI as a **practice generator**, not as a solution generator.

Instead of asking AI to write the code for me, I asked it to create exercises based on the **Pandas concepts I had already learned**. I then solved the challenges myself and used AI mainly to support my learning when necessary.

> **The goal was to use AI to practice programming, not to avoid programming.**

## 🛠️ Technologies

* 🐍 Python
* 🐼 Pandas
* 💻 VS Code

## 🚀 Goal

Continue improving my data manipulation skills while learning how Pandas can be applied to more realistic datasets.

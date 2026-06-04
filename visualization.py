import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Count per mood
mood_counts = df["Mood"].value_counts()

plt.figure()
mood_counts.plot(kind="bar")
plt.title("Items per Mood")
plt.xlabel("Mood")
plt.ylabel("Count")
plt.show()

# Category distribution
cat_counts = df["Category"].value_counts()

plt.figure()
cat_counts.plot(kind="pie", autopct='%1.1f%%')
plt.title("Category Distribution")
plt.show()
import pandas as pd

# Load the Amazon review dataset
df = pd.read_csv("fake-reviews.csv")

# Display the first five rows
print(df.head())

# Count missing values in each column
print(df.isnull().sum())

# Character length of each review
df["char_length"] = df["text_"].apply(len)

# Word count of each review
df["word_count"] = df["text_"].str.split().apply(len)

# Display the first five rows with the new columns
print(df.head())

# Import libraries for visualizing data
import seaborn as sns
import matplotlib.pyplot as plt

# Create a boxplot comparing review lengths
sns.boxplot(x="char_length", y="label", data=df)

# Add a title and axis labels
plt.title("Character Length of Reviews by Label")
plt.xlabel("Character length")
plt.ylabel("Review label")

# Display the graph
plt.show()
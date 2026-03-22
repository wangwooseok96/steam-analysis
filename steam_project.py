import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# PRICE DISTRIBUTION
# Read data
df = pd.read_csv("games.csv")

# View column names
print("Columns:", df.columns.tolist())

# Select key columns
df = df[['Price', 'Estimated owners', 'Positive', 'Negative', 'Genres']].copy()

# Convert to numerical values
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Owners_clean'] = pd.to_numeric(df['Estimated owners'], errors='coerce')
df['Positive'] = pd.to_numeric(df['Positive'], errors='coerce')
df['Negative'] = pd.to_numeric(df['Negative'], errors='coerce')

# Remove missing values
df = df.dropna(subset=['Price', 'Owners_clean', 'Positive', 'Negative', 'Genres'])

# Calculate the total number of reviews and the positive review rate
df['Total_reviews'] = df['Positive'] + df['Negative']
df['Review_score'] = df['Positive'] / df['Total_reviews']

# Remove outliers
df = df[(df['Price'] >= 0) & (df['Owners_clean'] > 0) & (df['Total_reviews'] > 0)]

print(df.head())
print(df.shape)

plt.figure(figsize=(8,5))
df_paid = df[df['Price'] > 0]
sns.histplot(df_paid['Price'], bins=20, kde=True)
mean_price = df_paid[df_paid['Price'] <= 60]['Price'].mean()
median_price = df_paid['Price'].median()
plt.axvline(mean_price, linestyle='--', label='Mean')
plt.axvline(median_price, linestyle='-', label='Median')
plt.title("Distribution of Paid Game Prices on Steam")
plt.xlabel("Price ($)")
plt.ylabel("Number of Games")
plt.xlim(0, 60)
plt.legend()
plt.tight_layout()
plt.show()



# CORRELATION HEATMAP
# Log transformation
df['Log_Owners'] = np.log1p(df['Owners_clean'])

# Column selection and removal of null values
corr_df = df[['Price', 'Log_Owners', 'Review_score']].dropna()

# Calculate correlations
corr = corr_df.corr()

# Create a heatmap
plt.figure(figsize=(6,4))

sns.heatmap(
    corr,
    annot=True,
    fmt=".3f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Matrix (Steam Games)")
plt.tight_layout()
plt.show()




# GENRE BOXPLOT
# Main Genre
df['Main_Genre'] = df['Genres'].apply(lambda x: x.split(',')[0].strip())

# Select Top 6
top_genres = df['Main_Genre'].value_counts().head(6).index
df_genre = df[df['Main_Genre'].isin(top_genres)].copy()

# Log Transformation
df_genre['Log_Owners'] = np.log1p(df_genre['Owners_clean'])

# Sort by “Median”
order = df_genre.groupby('Main_Genre')['Log_Owners'].median().sort_values().index

# Plot
plt.figure(figsize=(10,6))

sns.boxplot(
    data=df_genre,
    x='Main_Genre',
    y='Log_Owners',
    order=order
)

plt.title("Game Sales by Genre (Log Scale, Sorted by Median)")
plt.xlabel("Genre")
plt.ylabel("Log(Number of Owners)")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

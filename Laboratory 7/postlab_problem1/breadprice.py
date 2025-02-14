import pandas as pd
import matplotlib.pyplot as plt


file_path = "breadprice.csv"
df = pd.read_csv(file_path)


print("Initial Data:")
print(df.head())


df['Year'] = df['Year'].astype(int)
df['Average Price'] = df.iloc[:, 1:].mean(axis=1)


avg_price_per_year = df[['Year', 'Average Price']].set_index('Year')


plt.figure(figsize=(10, 5))
plt.plot(avg_price_per_year.index, avg_price_per_year['Average Price'], marker='o', linestyle='-', color='b')
plt.xlabel("Year")
plt.ylabel("Average Bread Price")
plt.title("Average Bread Price per Year")
plt.grid(True)
plt.show()

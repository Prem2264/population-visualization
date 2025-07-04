import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['India', 'China', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico'],
    'Population (2022)': [1407563842, 1425887337, 332403650, 279134505, 235824862, 214326223, 216746934, 169828911, 144713314, 126705138]
}

df = pd.DataFrame(data)
df = df.sort_values('Population (2022)', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(df['Country'], df['Population (2022)'], color='skyblue')
plt.title('Top 10 Countries by Population (2022)', fontsize=16)
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

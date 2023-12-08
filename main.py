import matplotlib.pyplot as plt
import pandas as pd

# Table 1
data1 = {
    "Year": ["2018", "2019", "2020", "2021", "2022"],
    "Total pe tara - Barbati": [37263, 36411, 40717, 45464, 36157],
    "Total pe tara - Femei": [19774, 19300, 21450, 23438, 19286],
    "Urban - Total": [12809, 12387, 15093, 17640, 13268],
    "Rural - Total": [24454, 24024, 25624, 27824, 22889],
}

df1 = pd.DataFrame(data1)
df1.set_index("Year", inplace=True)

# Table 2
data2 = {
    "Year": ["2020", "2021", "2022"],
    "Sub 20 ani": [120, 1410, 1292],
    "20-24 ani": [3430, 6873, 6053],
    "25-29 ani": [7108, 5215, 4346],
    "30-34 ani": [4298, 2599, 2415],
    "35-39 ani": [2067, 1663, 1660],
    "40-49 ani": [1938, 1656, 1575],
    "50-59 ani": [879, 596, 572],
    "60 ani si peste": [428, 256, 244],
}

df2 = pd.DataFrame(data2)
df2.set_index("Year", inplace=True)

# Table 3
data3 = {
    "Year": ["2019", "2020", "2021", "2022"],
    "Sub 20 ani": [2, 1, 3, 2],
    "20-24 ani": [288, 240, 241, 264],
    "25-29 ani": [1392, 1063, 1191, 1006],
    "30-34 ani": [2354, 1821, 1926, 1653],
    "35-39 ani": [1928, 1617, 1946, 1913],
    "40-49 ani": [2947, 2430, 2721, 2797],
    "50-59 ani": [1371, 1147, 1370, 1387],
    "60 ani si peste": [453, 472, 496, 539],
}

df3 = pd.DataFrame(data3)
df3.set_index("Year", inplace=True)

# Table 4
data4 = {
    "Year": ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
    "Total pe tara - Baieti": [20414, 18722, 17790, 16637, 16167, 15113, 13910],
    "Total pe tara - Fete": [19226, 17641, 16747, 15786, 14667, 14207, 13042],
    "Urban - Baieti": [7758, 7190, 6914, 6632, 6405, 6164, 5744],
    "Urban - Fete": [7205, 6684, 6387, 6135, 5797, 5726, 5408],
    "Rural - Baieti": [12656, 11532, 10876, 10005, 9762, 8949, 8166],
    "Rural - Fete": [12021, 10957, 10360, 9651, 8870, 8481, 7634],
}

df4 = pd.DataFrame(data4)
df4.set_index("Year", inplace=True)

# Plotting
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

# Table 1 (Changed to Pie Chart)
df1.sum().plot.pie(ax=axes[0, 0], autopct='%1.1f%%', colormap='viridis')
axes[0, 0].set_title('Total Population Distribution by Gender and Location')
axes[0, 0].set_ylabel('')

# Table 2
df2.plot(ax=axes[0, 1], kind='line', stacked=True, colormap='plasma')
axes[0, 1].set_title('Marital Status by Age Group')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('Population')

# Table 3
df3.plot(ax=axes[1, 0], kind='area', stacked=True, colormap='inferno')
axes[1, 0].set_title('Marital Status by Age Group and Gender')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Population')

# Table 4
df4.plot(ax=axes[1, 1], kind='bar', stacked=True, colormap='magma')
axes[1, 1].set_title('Population by Gender and Location (2016-2022)')
axes[1, 1].set_xlabel('Year')
axes[1, 1].set_ylabel('Population')

# Display the tables
plt.tight_layout()
plt.show()
print("Table 1:")
print(df1)
print("\nTable 2:")
print(df2)
print("\nTable 3:")
print(df3)
print("\nTable 4:")
print(df4)

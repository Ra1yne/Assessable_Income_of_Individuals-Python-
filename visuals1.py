import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
from tabulate import tabulate


def print_table(dataframe):
    print(tabulate(dataframe, headers='keys', tablefmt='fancy_grid'))

tax_group_data = pd.read_csv(r'data/Assessable Income of Individuals by Tax Group.csv')
#print_table(tax_group_data)

pivot_tax_group_data = tax_group_data.pivot(index='year_of_assessment', columns='tax_group', values='assessable_income')
year = pivot_tax_group_data.index
width = 0.35
x = np.arange(len(year))


plt.bar(x-width/2, pivot_tax_group_data['Non-Taxable Group'], width, label='Non-Taxable Group', color='skyblue')
plt.bar(x+width/2, pivot_tax_group_data['Taxable Group'], width, label='Taxable Group', color='orange')

plt.figure(figsize=(10, 6))

plt.xlabel('Year')
plt.ylabel('Assessable Income')
plt.title('Assessable Income For Different Tax Groups')

plt.xticks(x, year)
plt.legend()
plt.show()

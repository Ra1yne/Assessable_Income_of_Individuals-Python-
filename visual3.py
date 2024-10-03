import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
from tabulate import tabulate


def print_table(dataframe):
    print(tabulate(dataframe, headers='keys', tablefmt='fancy_grid'))
    
tax_group_data = pd.read_csv(r'data/Income of Individuals by Income Type and Tax Group.csv')
#print_table(tax_group_data.head())

aggregated_data = tax_group_data.groupby(['year_of_assessment', 'income_type'], as_index=False).agg({'amount': 'sum'})
pivoted_data = aggregated_data.pivot(index='year_of_assessment', columns='income_type', values='amount')
#print_table(pivoted_data.head())

y = pivoted_data.loc[2023]
my_labels = ['Dividends', 'Employment Income', 'Income from Trade and Profession', 'Interest', 'Other Types', 'Rent', 'Royalties']
#print(y)


plt.pie(y)
plt.legend()

plt.show()
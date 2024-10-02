import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
from tabulate import tabulate


def print_table(dataframe):
    print(tabulate(dataframe, headers='keys', tablefmt='fancy_grid'))
    
tax_group_data = pd.read_csv(r'data/Assessable Income of Individuals.csv')

#print_table(tax_group_data)

plt.figure(figsize=(12, 6))
plt.bar(tax_group_data['year_of_assessment'], tax_group_data['assessable_income'], color='skyblue', width=0.35)
plt.xticks(tax_group_data['year_of_assessment'])

plt.xlabel('Year')
plt.ylabel('Assesable Income')
plt.title('Assesably Income by Year')

plt.show()
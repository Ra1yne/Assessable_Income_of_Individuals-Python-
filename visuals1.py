import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from tabulate import tabulate

def print_table(dataframe):
    print(tabulate(dataframe, headers='keys', tablefmt='fancy_grid'))

tax_group_data = pd.read_csv(r'data/Assessable Income of Individuals by Tax Group.csv')
print_table(tax_group_data)


import pandas as pd
import os

# Prompt user for csv filename
#filename = input('Please enter the CSV\'s full path including filename: ').strip()
filename = 'ex_data.csv' # TODO: use above for final build ^
# Handle missing .csv
l = len(filename)
if filename[l-4:l] != '.csv':
    filename = filename + '.csv'
# Handle non-existant file, load into dataframe if possible
if not os.path.exists(filename):
    print('A File with that name was not found.')
    exit()
else:
    df = pd.read_csv(filename)

# Our objective is to create a map for each row from index 0 to n


# Create col_num dictionaries, indexed chronologically within the list
map_list = []
for col in df.columns:
    # Populate an dictionary in the form - 'label':num(label) 
    t_dict = {}
    for e in df[col].unique():
        t_dict[e] = (df[col] == e).sum()
    map_list.append(t_dict)

# Populate the dictionary with each mapping
print(map_list)


import pandas as pd  # import pandas to work with data/dataframes

# Asking for file name so that this may be used with other files
file1 = input("Please enter the file name you would like to use: ")

# Converting the csv file to a pandas dataframe for readability and
# so the script can work with the data more easily
df = pd.read_csv(file1)
has_column_labels = input("Does this data already have column labels (y/n)? ")
column_to_extract = ""
if has_column_labels == 'n':
    num_columns = int(input("How many columns in the data set? "))
    column_labels = []
    for i in range(1, num_columns + 1):
        column_labels.append(f"data{str(i)}")
    df.columns = column_labels
    column_number = input("Which number column are we extracting? ")
    column_to_extract = f"data{column_number}"
else:
    column_to_extract = input("What is the column label we should be extracting? ")
# Assigning arbitrary column labels, so I can specify which column I need


# Just labeling columns "data1", "data2", etc.


# Converting column 'data9' (names) to a list called list_of_names
list_of_names = df[column_to_extract].to_list()
# Asking for text file to use to compare for and remove common names from the list_of_names
file2 = input("Please enter the file name of the comparison file: ")
common_names = open(file2, 'r')
list_of_commons = []

# Scroll through each line/row of the text file
# Strip leading and ending spaces
# Append each common name to the list list_of_commons for comparison
for line in common_names:
    stripped_line = line.strip()
    list_of_commons.append(stripped_line)
na_tuple = ('na', 'NA', 'Na', 'nA', 'n/a', 'N/A', 'n.a', 'N.A')
number_tuple = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
# Make sure the names are all first letter capitalized
list_of_names2 = [str(name) for name in list_of_names]
list_of_names = list_of_names2
counter = 0
i = 0
length_list = len(list_of_names)
print(length_list)
while i < length_list:
    if len(list_of_names[i]) < 2:
        print(list_of_names[i])
        list_of_names.remove(list_of_names[i])
        length_list = len(list_of_names)
        i += 1
        continue
    #elif type(list_of_names[i]) == float:
    #    list_of_names.remove(list_of_names[i])
    #    length_list = len(list_of_names)
    #    i += 1
    #    continue
    elif list_of_names[i].startswith(number_tuple):
        list_of_names.remove(list_of_names[i])
        length_list = len(list_of_names)
        i += 1
        continue
    elif list_of_names[i] in na_tuple:
        print(list_of_names[i])
        list_of_names.remove(list_of_names[i])
        length_list = len(list_of_names)
        i += 1
        continue

    list_of_names[i] = list_of_names[i].capitalize()
    i += 1
print(len(list_of_names))
# Compare original names to common names and if there is a match,
# remove from the list_of_names
for name in list_of_names:
    if name in list_of_commons:
        list_of_names.remove(name)
output1 = input("Please enter tha name of the text file you would like to use for export: ")

# Export remaining names in list_of_names to text file
with open(output1, 'a') as f:
    for name in list_of_names:
        f.write(name.capitalize())
        f.write('\n')
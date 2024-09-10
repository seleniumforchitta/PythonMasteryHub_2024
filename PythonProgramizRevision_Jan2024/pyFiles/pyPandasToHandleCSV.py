# Pandas is a popular data science library in Python for data manipulation and analysis.
# If we are working with huge chunks of data, it's better to use pandas to handle CSV files for ease and efficiency.

import pandas as pd
reader = pd.read_csv('person.csv')
print(reader)

# else

# for index, row in reader.iterrows():
#     print(row)

#
# Read CSV Files
# To read the CSV file using pandas, we can use the read_csv() function.

# Write to a CSV Files
# To write to a CSV file, we need to use the to_csv() function of a DataFrame.

# creating a data frame
df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])

# writing data frame to a CSV file
df.to_csv('person.csv')
import csv

with open('C:\\Users\\chitt\\PycharmProjects\\PythonMasteryHub_2024\\PythonProgramizRevision_Jan2024\\pyFiles'
          '\\Testing.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#  Read CSV file Having Tab Delimiter
with open('person.csv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)

# Read CSV files with initial spaces
with open('person.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)

# Read CSV files with quotes
with open('person.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)
file.close()

with open('C:\\Users\\chitt\\PycharmProjects\\PythonMasteryHub_2024\\PythonProgramizRevision_Jan2024\\pyFiles'
          '\\Testing.csv', 'a', newline='') as file:
    # Here 'w' will remove everything from the file and start writing fresh
    # But 'a' will keep appending to the file
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])

file.close()
with open('C:\\Users\\chitt\\PycharmProjects\\PythonMasteryHub_2024\\PythonProgramizRevision_Jan2024\\pyFiles'
          '\\Testing.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

file.close()

# Writing Multiple Rows with writerows()
row_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
file.close()

# Write CSV File Having Pipe Delimiter
data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)

# Write CSV files with quotes
row_list = [
    ["SN", "Name", "Quotes"],
    [1, "Buddha", "What we think we become"],
    [2, "Mark Twain", "Never regret anything that made you smile"],
    [3, "Oscar Wilde", "Be yourself everyone else is already taken"]
]
with open('quotes.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer.writerows(row_list)
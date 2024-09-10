import csv

with open('C:\\Users\\chitt\\PycharmProjects\\PythonMasteryHub_2024\\PythonProgramizRevision_Jan2024\\pyFiles'
          '\\Testing.csv', 'r') as file:
    reader = csv.reader(file)

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
myList = ["Abhishek ", "Bangalore", 32, 10, '23LPA']
myList.insert(0, "Mr.")  # Inserts at the 0th place
print(myList)  # ['Mr.', 'Abhishek ', 'Bangalore', 32, 10, '23LPA']
myList.append("Maersk")  # Appends at the end
print(myList)  # ['Mr.', 'Abhishek ', 'Bangalore', 32, 10, '23LPA', 'Maersk']
myList.pop()  # Removes the last element
print(myList)  # ['Mr.', 'Abhishek ', 'Bangalore', 32, 10, '23LPA']
print(myList.count("Bangalore"))  # 1
myList.remove(10)  # It removes the mentioned element form the list
print(myList)  # ['Mr.', 'Abhishek ', 'Bangalore', 32, '23LPA']
myList.reverse()  # It reverses all the element
print(myList)  # ['23LPA', 32, 'Bangalore', 'Abhishek ', 'Mr.']
print(myList.index(32))  # It gives the index of the element
myList.clear()  # It empties the list
print(myList)  # []

print("---------------------------New Section------------------------------")
# a = [2,3,4,5,6,7,6]
# b = [5,6,7,8,9,0]
a = 2
b = 3
print(a == b)

# My Favourite interview question
myList = [3, 2, 3, 4, 5, 2, 2, 3, 2, 6, 7]
for i in myList:
    if i == 2:
        myList.remove(i)
        myList.append(i)
print(myList)
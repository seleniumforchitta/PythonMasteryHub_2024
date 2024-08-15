import copy

# Python List index()
animals = ['cat', 'dog', 'rabbit', 'horse']
print(animals.index('dog'))  # o/p - 1

# Python List append()
animals.append('elephant')
print(animals)  # o/p - ['cat', 'dog', 'rabbit', 'horse', 'elephant']

# Python List extend()
a = [10, 20, 30]
b = [15, 25, 35]
a.extend(b)  # If you so c = a.extend(b) it will give None as it only extends an existing list
print(a)  # o/p - [10, 20, 30, 15, 25, 35]

# Python List insert()
a = [10, 20, 30, 40, 50]
a.insert(4, 100)
print(a)  # o/p - [10, 20, 30, 40, 100, 50]

# Python List remove() - The remove() method removes the first matching element (which is passed as an argument)
a.remove(50)
print(a)  # o/p - [10, 20, 30, 40, 100]

# Python List count() - This returns the number of times the specified element appears in the list.
# len() will give of length of the list but count() will give the count of an element.
numbers = [2, 3, 5, 2, 11, 2, 7]
count = numbers.count(2)
print('Count of 2:', count)  # o/p - Count of 2: 3

# Python List pop() - method removes the item at the specified index. The method also returns the removed item.
# If the index is not passed, the default index -1 is passed as an argument (index of the last item).
animals.pop()  # Before pop - ['cat', 'dog', 'rabbit', 'horse', 'elephant']
print(animals)  # o/p - ['cat', 'dog', 'rabbit', 'horse']
returned_animal = animals.pop(1)
print(animals)  # o/p - ['cat', 'rabbit', 'horse']
print(returned_animal)  # o/p - dog
# If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.

# Python List reverse()
prime = [2, 3, 5, 7]
prime.reverse()
print("Reversed list : ", prime)  # o/p - Reversed list :  [7, 5, 3, 2]

# Python List sort()
animals = ['cat', 'dog', 'rabbit', 'horse', 'elephant']
numbers = [2, 3, 5, 2, 11, 2, 7]
# print(animals.sort()) This will throw None - because it doesn't return anything rather -
animals.sort()
numbers.sort()
print(animals)  # o/p - ['cat', 'dog', 'elephant', 'horse', 'rabbit']
print(numbers)  # o/p - [2, 2, 2, 3, 5, 7, 11]
# The sort() method can take two optional keyword arguments:
# reverse - By default False. If True is passed, the list is sorted in descending order.
# key - Comparison is based on this function.
numbers.sort(reverse=True)
print(numbers)  # o/p - [11, 7, 5, 3, 2, 2, 2]
animals.sort(reverse=True)
print(animals)  # o/p - ['rabbit', 'horse', 'elephant', 'dog', 'cat']
# Reverse Strings Based on Length
text = ["abc", "wxyz", "gh", "a"]
# sort strings based on their length
text.sort(key=len)
print(text)  # o/p - ['a', 'gh', 'abc', 'wxyz']

# Python List copy() - Returns a shallow copy of the list. Returns a new list, doesn't modify the original list.
prime = [2, 3, 5, 7]
prime_num = prime.copy()
print(prime_num)  # [2, 3, 5, 7]
# List copy using =
old_list = [1, 2, 3]
new_list = old_list
old_list.pop()
print(new_list)  # [1, 2]
# However, there is one problem with copying lists in this way. If you modify new_list, old_list is also modified.
# It is because the new list is referencing or pointing to the same old_list object.
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[1][0] = 'BB'
print("Old list:", old_list)  # Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
print("New list:", new_list)  # New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# Copy List Using Slicing Syntax - shallow copy using the slicing syntax
mylist = ['cat', 0, 6.7]
# copying a list using slicing
new_list = mylist[:]
# Adding an element to the new list
new_list.append('dog')
# Printing new and old list
print('Old List:', mylist)  # Old List: ['cat', 0, 6.7]
print('New List:', new_list)  # New List: ['cat', 0, 6.7, 'dog']
veryNewList = new_list[-1::-1]
print(veryNewList)  # ['dog', 6.7, 0, 'cat']
veryNewList = new_list[:]
print(veryNewList)  # ['cat', 0, 6.7, 'dog']


# Python List clear()
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.clear()
print('List after clear():', prime_numbers) # Output: List after clear(): []
#  If you are using Python 2 or Python 3.2 and below, you cannot use the clear() method.
#  You can use the del operator instead. - del prime_numbers[:]



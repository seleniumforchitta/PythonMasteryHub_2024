# Union
# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)  # Union using |: {0, 1, 2, 3, 4, 5}
# perform union operation using union()
print('Union using union():', A.union(B))  # Union using union(): {0, 1, 2, 3, 4, 5}

# Intersection
# first set
A = {1, 3, 5}
# second set
B = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A & B)  # Intersection using &: {1, 3}
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))  # Intersection using intersection(): {1, 3}

# Difference
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('Difference using &:', A - B)  # Difference using &: {3, 5}
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))  # Difference using difference(): {3, 5}

# Symmetric Difference
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('using ^:', A ^ B)  # using ^: {1, 3, 5, 6}
# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))  # using symmetric_difference(): {1, 3, 5, 6}


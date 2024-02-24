number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement is easy')

# ---------------------------------------------------------------

number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')

# ---------------------------------------------------------------

number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')


# For Loop
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
sum = 0;
for i in list1:
    sum = sum+i;

print(sum)

# While Loop
# Find the sum of all the elements from 1 to 100
tot = 10;
sum = 0;
i = 0;
while i<10:
    sum = sum+i;
    i = i+1;
print(sum)

# While loop with else
counter = 0;
while counter<3:
    print("Inside loop");
    counter = counter+1;
else:
    print("Inside else")

# Break and continue
# For Loop
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
for i in list1:
    if i==5:
        break
    print(i)

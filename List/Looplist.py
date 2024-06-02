# Python - Loop List
#You can loop through  the list items by using a for loop:
#Example:- Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
# Example:- print all items by referring to their index number:
Thislist = ["apple", "banana", "cherry"]
for i in range(len(Thislist)):
    print(Thislist[i])

# Using a While loop 
# Example:- print all items, using a while loop to go through all the index numbers
thisList = ["apple", "banana", "cherry"]
i = 0 
while i < len(thisList):
    print(thisList[i])
    i +=1

#Looping Using List Comprehension
# Example:- A short hand for loop that will print all items all items in a list:
ThisList = ["apple", "banana", "cherry"]
[print(x) for x in ThisList]

# Python - Add List Items
# Append Items
# append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert items
# insert()
thisList = ["apple", "banana", "cherry"]
thisList.insert(1, "orange")
print(thisList)

# Extend list 
# extend()
# Example:- Add the elements of tropical to thislist:
list = ["apple", "banana", "cherry"]
fruits = ["mango", "pineapple", "papaya"]
list.extend(fruits)
print(list)

# Add Any Iterable
# example:- Add elements of tuple to a list:
Thislist = ["apple", "banana", "cherry"]
Thistuple = ("kiwi", "orange")
Thislist.extend(Thistuple)
print(Thislist)
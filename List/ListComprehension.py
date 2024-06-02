# Python - list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#Example:- 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "e" in x]
print(newlist)

#Condition
# The conditon is like a filter is a filter that only accepts the items that valuate to True.
#Example:- Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
#Example:- You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

#Same example but with a condition:
#Example:- Accept only number lower thar 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Example:- Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# Example:- Set values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

# Example:- Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
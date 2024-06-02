# Python Sets
# Example:- Create a Set:
mySet = {"apple", "banana", "cherry"}
print(mySet)

# Duplicates Not allowed
# Example:- Duplicate values will be ignored:
mySet = {"apple", "banana", "mango", "cherry", "apple"}
print(mySet)

# Example:- whwt is the data type of a set?
mySet = {"apple", "banana", "cherry", True, 1, 2}
print(type(mySet))

# Note:- the value True and 1 are considered the same value in sets, and are treated as duplicates:
# Example:- True and 1 is considered the same value:
mySet = {"apple", "banana", "cherry", True, 1, 2}
print(mySet)

# Example:- False and 0 is considered the same value:
mySet = {"apple", "banana", "cherry", False, True, 0 , 2}
print(mySet)
 

 # Example:- What is the data type of a set?
mySet = {"apple", "banana", "cherry"}
print(type(mySet))

# Example:- Using the set() constructor to make a set:
mySet = set(("apple", "banana", "cherry")) # note the double round-brackets
print(mySet)
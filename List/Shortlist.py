# Python - Sort Lists
# Sort List Alphanumerically
# sort()
# Example:- sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "apple"]
thislist.sort()
print(thislist)

# Example:- Sort the list numerically:
thisList = [100, 50, 65, 82, 20, 5]
thisList.sort()
print(thisList)

# Customezi Sort Function
# Example:- sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort
# example:- case sensitive sorting can give an unexpected result:
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)

# Example:- perform a case-insenitive sort of the list:
thislist = ["Banana", "orange", "Kiwi", "Cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse Order
# reverse()
# Example:- Reverse the order of the list items:
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.reverse()
print(thislist)
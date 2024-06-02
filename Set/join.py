# the union() method returns a new set with all items from both sets.
# Example:- Join set1 and set2 into a new set:
set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

# Example:- use | to join two sets:
set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1 | set2
print(set3)

#Join Multiple Sets
# Example:- join multiple sets wih the union() method:
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"sohit", "sahil"}
set4 = {"apple", "banana","cherry"}
mySet = set1.union(set2,set3,set4)
print(mySet)

# Example:- Use | to join multiple sets:

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"sohit", "sahil"}
set4 = {"apple", "banana","cherry"}
mySet = set1 | set2 | set3 |set4
print(mySet)

# Intersection
# Example:- Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# Example:- Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# Example:- keep the items that exist in both set1 and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

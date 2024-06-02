# Change item value
# Example :- Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "mango"
print(thislist)

# Change a Range of item values
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:3] = ["blackcurrant", "watermelon"]
print(list)

List = ["apple", "banana", "cherry"]
List[1:2] = ["blackcurrant", "watermelon"]
print(List)

list2 = ["apple", "banana", "cherry"]
list2[1:3] = ["watermelon"]
print(list2)

# Insert items 
list3 = ["apple", "banana", "cherry"]
list3.insert(2, "watermelon")
print(list3)
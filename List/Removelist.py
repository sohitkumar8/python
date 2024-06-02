# Python - Remove List items
#remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thisList = ["apple", "banana", "cherry", "banana", "kiwi"]
thisList.remove("banana")
print(thisList)

# Remove Specified Index
# pop()
#Example:- Remove the second item:
list = ["apple", "banana", "cherry"]
list.pop(1)
print(list)

#Example :- Remove the last item:
List = ["apple", "banana", "cherry"]
List.pop()
print(List)

# The del keyword also removes the specified index:
#Example:- Remove the first item:
Thislist = ["apple", "banana", "cherry"]
del Thislist[0]
print(Thislist)

# Clear the List 
#Example:- Clear the list content:
ThisList = ["apple", "banana", "cherry"]
ThisList.clear()
print(ThisList)
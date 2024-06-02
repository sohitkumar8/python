# Global variables
x = "awesome"
def myfunc():
    print("Python is ",x)
myfunc()

# second example :-
a = "awesome"
def myfunc():
    a = "fantastic"
    print("Python is "+a)

myfunc()
print("Python is "+a)

# The global keyword
def myfunc():
    global b
    b = "fantastic"
myfunc()
print("Python is "+b)

#fourth example:-
y = "awesome"
def myfunc():
    global y
    y = "fantastic"
    
print("Python is "+y)
myfunc()
print("Python is "+y)



from operator import truediv

x=2

print(x==2)
print(x!=2)
print(x==3)
print(x<5)
print(x>5)

######################################

name="John"
age=23
if name == "John" and age == 23:
    print("you are john, 23")
if name == "john" and age == 23:
    print("you are john, 23")
if name=="John" or name=="Rick":
    print("hi James/Rick")
if name in ["John", "Rick"]:
    print("hi James/Rick")

######################################

a=True
b=True
if a==True:
    print("a true")
elif b==True:
    print("b true")
else:
    print("a and b false")

if a!=True:
    print("a false")
elif b!=True:
    print("b false")
else:
    print("a and b True")

if a==False:
    print("a false")
elif b==False:
    print("b false")
else:
    print("a and b True")

######################################

x=[1,2,3]
y=[1,2,3]

if x==y:
    print("x is the same as y")
else:
    print("x is not the same as y")

if x is y:
    print("x is y")
else:
    print("x is not y")

######################################

print(True)
print(False)
print(False==False)
print(not False)
print(not False == False)

######################################


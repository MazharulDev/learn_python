import numpy as np

# variable 
a=1
b=2
# print(a)
# print(b)
# print(a+b)

name= "mahfuz"
age= 25
# print(name,age)

# spacific data type 

name=str("mahfuz")
age=int(25)
height=float(5.5)
isMale=bool(True)
# print(name,age,height,isMale)

# multiple variable in one line 

a,b,c=1,2,3
# print(a,b,c)

# one value to multiple variable 

a=b=c=1
# print(a,b,c)

# unpacking a collection 

fruits=["apple","banana","cherry"]
x,y,z=fruits
# print(x,y,z)

x="paython"
y=" is"
z=" awesome"
# print(x+y+z)

m=5
n=1
# print(m+n)

# global variable

x="awesome"

def myfunc():
    print("paython is " + x)

# myfunc()

def createGlobal():
    global mahfuz
    mahfuz="my name is mahfuz"

createGlobal()
print(mahfuz)

age = [12,34,34,34,45]
converted_array=np.array(age)
print(converted_array)

print(type(converted_array))

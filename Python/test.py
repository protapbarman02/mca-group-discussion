print("Hi")

"""  
data types
function
OOP
try catch
multithreading
"""

# data types
a = 5  # integer
a = "hello"  # string
b = 5.5  # float
c = 5j + 2  # complex
d = "Hi"  # single / double quote
e = [1, 2, 3, 4, 5]  # list
f = [1, "hi", True, False, 5.5, 5j + 2]  # list
g = True  # boolean : True/ False
h = None
print(type(h))
print(4j + 4.2 + 2 + 2j)

# tuple, set, dictionary


# operators +
a = "Hi"
b = "H"
# print(a - b)
print(a * 5)
# print(a / 5)

a = 5
a = a + 1
a += 1
print(a)
a = +1
print(a)
# python does not support pre/post-incremental values


a = "Pawan"
print(a[0])
print(a[-1])

# string functions
print(len(a))
print(a[0:2])  # starting from 0, ending before 2
print(a[::-1])
# start:end:step

print(a.upper())  # lower
print(a)


# mutable

# immutable
a = "Hello, World!"
print(a.replace("H", "J"))
print(a)

name = "Protap"
age = 25
print(
    f"My Name is {name} and age is {age}"
)  # inside f string, number is auto converted to string    # automatic typecasting

arr = [1, 2]
print(f"{arr}")

a = 5
a = str(a)  # manual typecasting
print(a)

name = "I\"m protap barman"
print(name.center(100))
a = "Hi"
b= "Hello"

print(b.join("-"))


a = 5
if a==5:
  print("yes")
  
if a is 5:
  print("yes")
  
if a!=10:
  print("yes")
  
if a is not 10:
  print("yes")

if a:
  print("yes")
  
if(a==5):
  print("yes")
  
if((a is 5) and (a is not 10)):
    print("yes")
    
if((a is 5) or (a is not 10)):
  print("yes")
  
if(not a is 5):
  print("yes")
else:
  print("no")
  
  
# loops
# list
# tuple, set
# dictionary
# list and dictionary comprehension
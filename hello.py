#First Code
print("Hello World!")
print("Welcome to Python Programming!")


#Variables
#A variable is a name given to a memory location in a program.
Name="Sarikaa Lamsal"
print ("My name is", Name)
Age=21
print("My age is", Age)
Height=5.3
print("My height is", Height)


#Assignment Operators
x=5
X2=x
print("X2 is:", X2)


#Rules for Identifiers
#1. Identifiers can be combination of uppercase and lowercase letters, digits and underscores(_).
#   So myvariable, variable_1, Variable_for_print all are valid python identifiers.
#2. An identifier cannot start with a digit. So variable1 is a valid while 1variable is not valid.
#3. We can't use special symbols like !, @, #, $, %, etc. in identifiers. So variable@1 is not valid.
#4. Identifiers can be of any length.



#Data Types
print(type(Name))     #string
print (type(Age))     #integer
print (type(Height))  #float

#Boolean : True or False
is_student=True
print (type(is_student))  #boolean

#None : represents the absence of a value
is_teacher=None
print (type(is_teacher))  #NoneType


age=21
old=False
a=None
print(type(old))  #boolean
print(type(a))    #NoneType



#Keywords:
#Keywords are reserved words in Python that have special meaning and cannot be used as identifiers (variable names, function names, etc.).
#some examples of keywords in python are:
# and             else           in             return
# as              except         is             True
# assert          finally        lambda         try
# break           False          nonlocal       while
# class           for            not            with
# continue        from           or             yield
# def             global         pass
# del             if             raise
# elif            import         None




#Print Sum
a=10
b=20
sum=a+b
print ("The sum of", a, "and", b, "is:", sum)



#Comments In Pyhton
# This is a single-line comment
"""
This is a multi-line comment
It can span multiple lines
"""


#Types of Operators
#1. Arithmetic Operators: +, -, *, /, %, **
#2. Relational/Comparison Operators: ==, !=, >, <, >=, <=
#3. Logical Operators: and, or, not
#4. Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=

#Arithmetic Operators
a=10
b=20
sum=a+b
print ("The sum of", a, "and", b, "is:", sum)


#Relational/Comparison Operators 
a = 50
b = 20
print(a>b)   # True
print(a<b)   # False
print(a>=b)  # True
print(a<=b)  # False
print(a==b)  # False
print(a!=b)  # True


#Assignment Operators
num = 5
num = num + 5
print("num =", num)
num = 10
num /= 2
print("num =", num)
num = 20
num %= 4
print("num =", num)


#Logical Operators
x = True
y = False
print(x and y)  
x = True
y = False
print(x or y)
x = True
y = False
print(not x)



#Type Conversion
#Type conversion and Type Casting
#Conversion is the process of converting one data type to another data type automatically. In Python, we can convert data types using built-in functions like int(), float(), str(), etc.
#Casting is the process of converting one data type to another data type manually. In Python, we can cast data types using built-in functions like int(), float(), str(), etc.




#Type Conversion
a = 2
b = 4.25

sum = a + b
print("The sum of", a, "and", b, "is:", sum)



#Type Casting
a = 2
b = 4.25

sum = a + int(b)
print("The sum of", a, "and", int(b), "is:", sum)



#Input in Python
#input() statement is used to accept values (using keyboard) from user.
# input() #result for input is always a string.
# int (input()) #int
# float (input()) #float


name = input("enter your name:")
print("Welcome", name)



#Practice Question
#Write a program to input 2 numbers and print their sum.
first= int(input("enter first number:"))
second= int(input("enter second number:"))  
print("sum= ", first+second)

#Write a program to input side of a square and print its area.
side=float(input("enter the side of the square:"))
print("area of the square is:", side *side)

#write a program to input 2 floating point and print their sum.
first=float(input("enter first number :"))
second= float(input("enter second number:"))
print("Their average is:" , ((first+second)/2))

#WAP to input 2 numbrs, a and b. Print True if a is greater than b. If not print false.
a=int(input("enter first number:"))
b=int (input("enter the second number:"))
print(a>=b)


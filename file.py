# Output function 

# print(5000)
# print(600 + 300)
# print(600 * 3)
# print(50.4545 + 80.4545)

# print('Hello welcome to python')
# print("Hey all, welcome to expertzlab")
# print("Hello")

# print("Pranav")     ctrl + /

# Variables : container to store values

# a = 5000
# print( a + 600)
# print(100 + a - 800)

# b = "Python"
# print(b)
# c = 'Hello all, python is a easy syntaxing language'
# print(c)

# x = y = z = 500
# print(x)
# print(y)
# print(z)

# m,n,p = 800,700,600
# print(m)
# print(n)
# print(p)


# x = 70
# x = 60
# x = 100
# x = 65 
# print(x)


# Naming rules for variables
# 1. variable name shoulb be start with alphabet or underscore 
# 2. Numbers and special characters are not allowed as first letter 
# 3. after first letter name will followed by eighter number / alphabet / underscore
# 4. special characters are not allowed 
# 5. Keywords (reserved words in python) are not allowed

# abc = 50
# _abc = 60
# # 5xyz = 70
# x5yz = 70
# x5_yz = 70
# # x5-yz = 70

# # help('keywords')
# # break = 80
# Break = 80 

# # True = 100
# true = 100

# x = "05"

# Data types in python 
# 1. Numeric d.t  : int, float, complex 
# 2. Boolean d.t 
# 3. Sequence d.t : list, tuple, string 
# 4. Dictionary 
# 5. set 

# numberic,bool, str : primary d.t 
# list, tuple, dict, set : collection d.t 

# Numeric 
# int 
# a = 10
# print(a)
# print(type(a))
# b = -50
# print(type(b))

# # Float
# x = 50.4545
# print(type(x))
# y = -0.05454
# print(type(y))

# m = 50 + 100
# m = 50.5 + 100
# print(type(m))

# b = 3 + 4j
# print(type(b))


# Boolean : False , True 
# a = True 
# b = False 
# print(type(a))
# print(type(b))

# String : '' / "" / ''' ''' 
# x = "hello"
# y = 'python'
# z = '''welcome'''
# print(type(x))
# print(type(y))
# print(type(z))

# # a = 'i don't like speed'
# a = "i don't like speed"
# print(a)
# # b = "i like "Kashmiri" Apples"
# b = 'i like "Kashmiri" Apples'
# print(b)
# n = "Arun Anu Aneesh Amal"
# n = "Arun " \
# "Anu " \
# "Aneesh " \
# "Amal"


# n = "Arun \nAnu \nAneesh \nAmal"
# n= '''Arun
#   Amal Anu
# Aneesh'''
# print(n)

# x = 'True'
# print(type(x))
# y = "0.0544545"
# print(type(y))

# Type casting : data type conversion 

# x = "10.45454545"
# print(type(x))
# newx = float(x)
# print(newx)
# print(type(newx))

# y = 4545455
# newy = str(y)
# print(newy)
# print(type(newy))

# z = "hello"
# # newz = int(z)

# m = bool(z)
# print(m)

# z  = ""
# n = bool(z)
# print(n)

# input fn 

# a = 70 
# print(a + 100)

# n = input("Enter your name:")    # str 
# print(n)

# x = input("Enter a no:")
# print(x)
# print(type(x))

# x = int(input("Enter a no:"))
# print(x)
# print(type(x))

# x = float(input("Enter a no:"))
# print(x)
# print(type(x))
# print(x + 100)

# Operators in python 
# 1. Arithemtic op. 
# 2. Assignment op. 
# 3. Relational op. 
# 4. Membership op. 
# 5. Logical op. 

# 1.Arithmetic : + , - , * , / ,** , % , //
# a = 50 
# b = 20 
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# c = a+b
# print(c)
# print(c*3)
# print(c*4)

# d = 10 
# print(d ** 3)
# print(d ** 4)

# x = "hello"
# y = "python"
# print(x+y)
# print(x+" "+y)

# # print(x-y) # error
# # print(x*y) # error
# # print(x/y) # error

# print(y * 4)

# # m = "python"
# # n = 500
# # print(m+n)  # error

# # % modulus print reminder of division 
# print(5 % 2)
# a = 18 
# b = 3
# print(a % b )

# print(21/4)
# # // Floor division : print integer part of output 
# print(21//4)

# Assignment  : = , += , -= , *= , /= 
# x = 10
# x = 50 
# x = 80 
# x = 20 
# print(x)

# # x = x + 30 
# # x += 30
# # x -= 30
# # print(x)

# y = 100
# y += 100
# y += 200
# print(y)

# m = 10
# m += 50 
# m -= 30
# m *= 2
# m /= 6
# print(m)

# Relational operators (==, != , > , < , >= , <=)
# a = 50 
# b = 30 
# c = 50 
# p = "Kochi"

# print(a == b)
# print(b == c)
# print(a == c)
# print(a == 80)
# print(p == 'Kottayam')
# print(p == 'Kochi')
# print(p == 'KOCHI')

# print(b != c)
# print(a != c)

# print(a > b)
# print(b < c)
# print(a < c)
# print(a <= c)
# print(b >= 80)

# 4. Membership : in , not in : 
# not applicable in numeric, bool

# x = "Hi all welcome to python programming"
# print('python' in x)
# print('Java' in x)
# print('g' in x)

# print('hello' not in x)
# print('welcome' not in x)
# print('Python' not in x)

# 5. Logical operators : and, or , not  
# and :
#     if all conditions are True , o/p = True 
#     if any one condition is False , o/p = False 

# a = 10 
# b = 15 
# c = 25 
# print(a != b and b <= 20 and c >= 25)
# print(a != b and b <= 20 and c >= 30)
# print(a != b and b <= 10 and c >= 30)

# # or : 
# #     if any one condition is True , o/p = True 
# #     if all conditions are False , o/p = False 
# print(a != b or b <= 20 or c >= 25)
# print(a != b or b <= 20 or c >= 30)
# print(a != b or b <= 10 or c >= 30)
# print(a == b or b <= 10 or c >= 30)


# not : reverse your result 
# print(not(a != b and b <= 20 and c >= 25))
# print(not(a == b or b <= 10 or c >= 30))

# control structures  
# 1. sequence c.s 
# a = 10 
# b = 10
# print(a)
# print(b)

# 2. selection c.s : if, if-else, elif, nested if-else 
# if 
# syntax :
# if condition:  True 
#     statements

# a = 7
# a = int(input("Enter a no:"))
# if a > 10:
    # print("Values is Above 10")









# if-else 
# syntax :
# if condition:  True 
#     statements
# else:          False 
#     statements

# a = int(input("Enter a no:"))
# if a > 10:
#     print("Values is Above 10")
# else:
#     print("Value is Below 10")

# Q: write a pgm to find a student 
# pass or failed in exam 
# (passmark is above 40)


# mark = int(input("Enter your mark:"))
# if mark > 40:
#     print("Pass")
# else:
#     print("Fail")

# Q: Take user state as an input and if user if not from kerala 
# give a greeting as "WELCOME TO GOD'S OWN COUNTRY" . if user is from kerala 
# give a greeting as "HEY MALLU"

# s = input("Enter your state:").lower()
# if s == 'kerala':
#     print("HEY MALLU")
# else:
#     print("WELCOME TO GOD'S OWN COUNTRY")

# Q: write a pgm to check a number even or odd 

# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Q) Write a pgm to calculate the total bonus point of students 
# if student participated in Sports ,bonus point is 10
# if student participated in Arts ,bonus point is 5
# if student participated in Events ,bonus point is 3


# b = 0 
# b += 10
# b += 5
# print(b)

# q1 = input("Are you paricitipated in SPORTS (y/n):").lower()
# q2 = input("Are you paricitipated in ARTS   (y/n):").lower()
# q3 = input("Are you paricitipated in EVENTS (y/n):").lower()

# totalBonus = 0
# if q1 == 'y':
#     totalBonus += 10
# if q2 == 'y':
#     totalBonus += 5
# if q3 == 'y':
#     totalBonus += 3

# print("Total bonus =", totalBonus)


# Q: create a unit convertor
# km to mile 
# dollar to rupees 
# kelvin to celsius


# choice = input('''Choose your Converter type from below option 
# 1 : for Km to Mile
# 2 : for Dollar to Indian Rupees 
# 3 : for Kelvin to Celsius ::''')

# if choice == '1':
#     v = int(input("Enter your value in KiloMeter :"))
#     m = v * 0.621371
#     print('In mile :' , m)
# elif choice == '2':
#     v = int(input("Enter your value in DOLLAR :"))
#     exchangeRate = 92 
#     r = v * exchangeRate
#     print('In India rupee :',r)
# elif choice == '3':
#     v = int(input("Enter your value in Kelvin:"))
#     c = v - 273.15
#     print('In  celsius:',c)
# else:
#     print("Invalid Choice")


# q : Create an ATM withdrawl : 
# every one have a balance = 2000
# >>>  if minimum amount is less than 0 print "Invalid amount"
# >>>  if withdrawl amount is greater than balance print "insufficient balance"
# >>>  if amount is not a mutiple of 100 print "enter amount in multiples of 100"
# >>>  if all are okay print "Transaction completed"


# AccountBalance = 2000
# withdraw = int(input("Enter your amount to Withdraw:"))  
# if withdraw > 0:
#     if withdraw <= AccountBalance:
#         if withdraw % 100 == 0:
#             print("Transaction Completed Please collect your cash")
#         else:
#             print("Enter amount in multiples of 100")
#     else:
#         print("Insufficient Balance")
# else:
#     print("Invalid Amount, Minimum withdraw should be above 0")


# Q: write a pgm to create a login system to login as a admin 
# admin credentials are   username = "admin" , password = 'expertzlab123'
# take input from user as both username and password

# if user username is not matching with admin username print "invalid username"
# if user password is not matching with admin password print "incorrect password"
# if both are mathching print "Login successfull as Admin"

# username = 'admin'
# password = 'expertzlab123'

# u = input("Enter your Username:")
# p = input("Enter your Password:")

# if u == username:
#     if p == password:
#         print("Credentias are matching, login completed as ADMIN")
#     else:
#         print("Incorrect password")
# else:
#     print("Invalid username")


# Assignment : question answer app code 


# Loops 
# Q: using while loop print 30 to 60
# Q: using while loop print 30 to 60 in reverse order 
# Q: using while loop find no.s which are divisible by 3 in btw 50 and 100

# n = 30
# while n <= 60:
#     print(n)
#     n+=1

# n = 60
# while n >= 30:
#     print(n)
#     n-=1

# n=50
# while n <= 100:     
#     if n%3 == 0:
#         print(n)
#     n+=1

# using while loop :
# Q: find the no.s which are divisible by 3 and 7 in the range 1000 and 2000
# Q: find the no.s which are not divisible by 3 and 7 in the range 1000 and 2000


# x = 1000
# while x <= 2000:
#     if x%3 == 0 and x%7 == 0:
#         print(x)
#     x+=1

# x = 1000
# while x <= 2000:
#     if not(x%3 == 0 and x%7 == 0):
#         print(x)
#     x+=1


# For loop : 
# based on range ,
# not applicable in numeric and boolean variables
# x = "python"
# x = range(1,11,1)    # range(start, end, step)   

# x = "python"
# for k in x:    #  1. k = 'p' , 2. k='y' 3.'t'....6.k='n'
#     print("Welcome to python")

# x = "hey"
# for k in x:   
#     print("Welcome to python",k)

# x = range(1,21,1)
# for i in x:
#     print("Welcome",i)

# x = 445555              Error
# for i in x:
#     print("welcome")



# Q: Using for loop find 
# square of values from 10 to 25


# x = range(10,26,1)
# for i in x:
#     print(i**2)

# for i in range(10,26,1):
#     print(i,i**2)


# Q: find the cube of all odd numbers 
# btw 5 to 20 

# for i in range(5,21,2):
#     print(i, i**3)

# for i in range(5,21,1):
#     if i%2 != 0:
#         print(i, i**3)

# Q: write a pgm to find numbers which are 
# divisible by 3 and 5 in the range 1250 and 1503

# for i in range(1250,1504,1):
#     if i%5 == 0 and i%3 ==0:
#         print(i)

# range(start, stop , step)  :   
# range(10,23,1)  = 10,11,12,13,.....22
# range(10,23,2)  = 10,12,14,16......22
# range(10,23,5)  = 10,15,20

# range(start, stop)  => default step =1
# range(10,23)  = 10,11,12.......22

# range(stop) =>  default start = 0 , step 1
# range(15)  = 0,1,2,3,4,5.....14

# range(20,9,-1) : 20,19,18,17......10

# Q: write a pgm to find numbers btw 2000 and 2050 
# in which each digit of number is even 

# 2000 ==>   2(even) , 0(even), 0(even) , 0(even)   # condition True
# 2010 ==>   2(even) , 0(even), 1(odd)              # condition false
# 2024 ==>   2(even), 0(even), 2(even), 4(even)     # condition True

#    012345....
# a = "hello welcome"
# print(a)
# # index : a numbers assigned to each element
# print(a[1])
# print(a[6])
# print(a[12])
# # print(a[13])

# # negative index : from right to 
# # left start with -1 
# # b = "h    e   l   l   o"
# #     -5   -4  -3  -2  -1
# b = 'Hello'
# print(b[-1])
# print(b[-3])

# x = "Welcome to python programming"
# print(x[0])
# print(x[-1])
# print(len(x))
# print(len(b))
# print(x[ len(x)-1 ])




# for i in range(2000,2051):
#     s = str(i)  # s = "2000", s="2001"
#     if int(s[0])%2 ==0 and int(s[1])%2 ==0 and int(s[2])%2 ==0 and int(s[3])%2 ==0:
#         print(i)


# a = "hello welcome to python programming"
# start = 0 
# end = len(a)-1

# for i in range(start,len(a)):
#     print(i, a[i])


# a = input("Enter a String:")
# for i in range(len(a)):
#     print(i, a[i])



# x = "hhhhhhhhhhhhhhh"
# for i in x:
#     print("Welcome to python")

# for i in range(1,11):
#     print("Welcome to python")

# * 
# * *
# * * *
# * * * * 
# * * * * *

# a = "hello"
# print(a * 5)

# print("python " * 5)
# print("* " * 1)
# print("* " * 2)
# print("* " * 3)
# print("* " * 4)
# print("* " * 5)

# for i in range(1,6):
#     # print(i)
#     print("* " * i)

# Write a pgm to generate below pattern 

# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(5,0,-1):
#     # print(i)
#     print("* " * i)



# for i in range(1,6):
#     print(i,"Hello")
#     print(i,"Python")
#     print(i+100)
#     print()
 
# for i in range(1,6):        # i = 1 ,      i= 2    i=3
#     print("Hello")
#     for k in range(10,13):  # k = 10 , k= 11, k= 12
#         print(i,k)
#     print()

# for i in range(1,11):
    # print(i)
    # print(i,end="")
    # print(i,end="--")
    # print(i,end=" ")





# Write a pgm to create below pattern

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# for i in range(1,6):      # i = 1                              i=2                                  i=3
    # print(i) 
    # for k in "hello":   # k='h',k='e',k='l',k='l',k='o'        # k='h',k='e',k='l',k='l',k='o'     # k='h',k='e',k='l',k='l',k='o'
    #     print('HI')


# for k in range(1,3):
#     print(k,end=" ")

# for i in range(1,6):        #i=1             i=2            i=3
    # for k in range(1,i+1): # range(1,2)      range(1,3)     range(1,4)
    #     print(k,end=" ")
    # print()

# for i in range(5,0,-1):
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# for i in range(5,0,-1):
#     for k in range(i,0,-1):
#         print(k,end=" ")
#     print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1 
# 2 1
# 1





# Q: write a pgm to find a number prime or not 

# prime : 

# n/1       n/n
# 10/1 2,3,4.....9     10/10
# 7/1  2,3,4,6      7/7
# 5/1  2,3,4           5/5
# 6/1  2,3,4,5       6/6








# Loop controlls in loop: 
# continue to skip , 
# break to stop  , 
# pass to no execution

# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)
    
# for i in range(1,6):
#     if i==4:
#         break
#     print(i)

# for i in range(1,6):
#     pass
# print("For loop will execute after some time")
    

# loop controls in while loop

# a = 0
# while a <= 10:
#     print(a)
#     a+=1


# a = 0
# while a <= 10:
#     if a == 4:
#         break;    
#     print(a)
#     a+=1


# a = 0
# while a <= 10:     # a=4
#     if a == 4:
#         a+=1
#         continue;    
#     print(a)
#     a+=1









# while True:
#     a = int(input("Enter a number:"))
#     b = int(input("Enter a number:"))
#     print("Total = ",a+b)
#     c = input("Do you want to stop(y/n):").lower()
#     if c == 'y':
#         print("Thank you")
#         break


# Q: write a pgm to find a number prime or not 

# prime : 

# n/1       n/n
# 10/1 2,3,4.....9     10/10
# 7/1  2,3,4,6      7/7
# 5/1  2,3,4           5/5
# 6/1  2,3,4,5       6/6

# n = int(input("Enter your number:"))    # n= 5                 n=8
# for i in range(2,n):                    # range(2,5) = 2,3,4   range(2,8)= 2,3,4..7
#     # print(i)
#     if n%i == 0:
#         print("Not a prime")
#         break
# else:
#     print("Prime")

# collection datatypes in python (list,tuple,dict,set)
# list :
# >> used to represent as []
# >> list elements are separated by , 
# >> list can store multiple data types
# >> variable length is not limited 
# >> list are mutable (items of list can change)
# >> items / elements of list is accessable with index 

# a = []            # empty list
# print(type(a))
# f = ['Apple','Orange','Grape',"Pine apple","Water melon"]
# print(f)
# print(type(f))
# s = ['Arun',25,"Kochi",True,172.5]
# print(s)

# # s = "Python"
# # print(s[0])

# #     0         1       2           3           4
# f = ['Apple','Orange','Grape',"Pine apple","Water melon"]
# #     -5        -4      -3          -2          -1
# print(f)
# print(f[3])
# print(f[2])
# # print(f[6])  Error
# print(f[-3])



# # Nested list : List inside a list 
# #                0  1 2
# s = ['Arun',25,[50,60,55],'Kochi']
# #      0    1       2        3
# print(s)
# print(s[0])
# print(s[2])
# print(s[2][1])

# #    0              1       2
# m =[[10,20,30],[50,70,60],[45,25]]
# #     0 1 2      0  1  2    0 1
# print(m[2])
# print(m[2][1])
# print(m[2][-1])

# Operations on list
# 1. replace 
# f = ['Apple','Orange','Grape',"Pine apple","Water melon"]
# print(f)
# f[1] = "Lemon"
# f[-2] = 'Dragon Fruit'
# print(f)

# s = ['Arun',25,[50,60,55],['Palarivattom','Kochi','Kerala']]
# print(s)
# s[2][1] = 68
# s[3][0] = "Kaloor"
# s[3] = "Kochi"
# print(s)

# 2. Insert(index,value)
# f = ['Apple','Orange','Grape',"Pine apple","Water melon"]
# # f.insert(2,"Mango")        # into index
# # f.insert(4,"Lemon")
# f.insert(-2,"Dragon Fruit")  # next to index
# print(f)

# s = ['Arun',25,[50,60,55],['Palarivattom','Kochi','Kerala']]
# s[2].insert(1,554545)
# print(s)

# 3. Sort : only applicable if list using same data types as elements 

# f = ['Apple','Orange','Grape',"Pineapple","Watermelon","Mango"]
# f.sort()
# f.sort(reverse=True)
# print(f)

# l = [54,6,2,89,4,78,55,91,45,54,54,8,0,45,50.45]
# l.sort()
# l.sort(reverse=True)
# print(l)

# m = [[50,40,70],[12,35,15],[78,12],[78,13,15]]
# m.sort()
# # m.sort(reverse=True)
# print(m)

# m[3].sort()
# print(m)


# 4.Delete in list 
# del 
# pop 
# remove

# c = ['Red','Green','Blue','Black','Grey','Yellow',"Green"]
# print(c)
# del c[3]
# print(c)

# c.pop(4)
# print(c)

# c.remove('Green')
# print(c)

# print(del c[-4])   # error 
# print(c)

# print(c.pop(-4))
# print(c)

# 5. Append : Used to add an items to last index

# x = [10,20,30,40]
# print(x)
# x.append(500)
# x.append(80)
# x.append(90)
# print(x)

# m = []
# m.append("Car")
# m.append("Truck")
# m.append("Motor Bike")
# m.append("Aero plane")
# print(m)

# # 6. Extend: add a list to another existing list 

# a = [10,20,30,40,50]
# b = [100,200,300]
# a.extend(b)
# print(a)



# # 7. Concatination
# a = [10,20,30,40,50]
# b = [100,200,300]
# c = a+b 
# print(c)


# # ?Requirements 
# 1. Create a list 5 student names 
# 2. Add a new student to 3rd position 
# 3. Add one more student to end of list 
# 4. arrange student names in reverse alphabetical
#     order 
# 5. remove first student from current list 
# 6. create one more list with 3 student name 
# 7. Add above 2 list and create a new student list 

# s = ['John','Tom','Mike','Sera','Susan']
# s.insert(2,"Catherine")
# s.append("Ani")
# s.sort(reverse=True)
# del s[0]
# print(s)
# new = ['Rohan','Rahul','Jacob']
# students = new + s
# print(students)











# Q: create a list of values btw 10 and 20 

# a = []
# a.append(10)
# a.append(11)
# a.append(12)
# a.append(13)
# print(a)

# new = []
# for i in range(10,21):
#     # print(i)
#     new.append(i)
# print(new)

# Q: create a list of even numbers btw 
# 50 to 100 
# Q: create a list of values which are 
# not divibile by 3 and 5 in the range 1250 to 2000

# new = []
# for i in range(50,101):
#     # print(i)
#     if i%2 == 0:
#         new.append(i)
# print(new)

# new = []
# for i in range(1250,2000):
#     if not(i%3 == 0 and i%5==0):
#         new.append(i)
# print(new)


# a = "Hello"
# b = ["Black",'Blue','Maroon','Yellow']

# for i in a:
#     print(i)

# for i in b:
#     print(i)

x = [10,54,6,89,45,69,32,44,6,36]
# Q: add 100 with each element of above list 

# new = []
# for i in x:
#     # print(i)
#     new.append(i+100)
# print(new)






# n= [10,60,15,36,13,17,89,45,25,33,40]

# Q: create a new list of odd numbes from above list

# Q: Find the square of each element from above list 
# and create a new list 

# new = []
# for i in n:
#     # print(i)
#     if i%2 != 0:
#         new.append(i)
# print(new)

# new = []
# for i in n:
#     new.append(i**2)    
#     # new.append(i*i)  
# print(new)


# a = ['Python','Java','C++','C#','R','Javascript']
# membership : in , not in 

# print("Hello" in a)
# print("Python" in a)
# print("java" in a)

# print("Javascript" not in a)
# print("J" not in a)

# Q: Remove duplicate items from below list and create a new list 
x = [50,60,70,10,50,60,70,10,20,30,30,10,50,80]

# new = []
# for i in x:            
#     # print(i)
#     if i not in new:
#         new.append(i)
# print(new)

# Students = ['Amal','Arun','Akshay','Deepak','Libin','John','Ziyad','Aslam']
# sports = ['Tom','Akshay','Rahul','Manu','Anas','Libin']
# # Q: find the students who are not in sports team 

# new = []
# for i in Students:
#     if i not in sports:
#         new.append(i)
# print(new)


# TUPLE 
# >>> ()
# >>> Same as list , but tuple are immutable 

# t = ()    # empty tuple
# print(t)
# print(type(t))

# t = ('Car','Bus','Truck','Bike')
# print(t)

# t = ("Akshay",25,"Kochi",False,[50,60,70,80],168.5)
# print(t)
# print(type(t))

# print(t[1])
# print(t[4])
# # t.insert(2,500)

# t[4].insert(2,500)
# print(t)


# DICTIONARY  
# >>> {}
# >>> each item should be in a format k:v 
# >>> key and value sepated by : 
# >>> each k:v sepated by ,
# >>> dict donot accept duplicate keys, 
# >>> values can become duplicate

# d = {}            # empty dict 
# print(d)
# print(type(d))

# student = {"Name":'John',"Age":23,"Place":"Kochi","Height":172.5,10:100,20:"Ten"}
# print(student)
# print(type(student))

# student = {"Name":'John',"Age":23,"Place":"Kochi","Name":"Teena"}
# print(student)

# student = {"F_Name":'John',"Age":23,"Place":"Kochi","L_Name":"John"}
# print(student)




# student = {"F_Name":'John',"Age":23,"Place":"Kochi",
#            "L_Name":"David","Height":172.5}
# print(student)
# print(student['F_Name'])
# print(student['Place'])
# # print(student['marks'])  Error

# student['Age'] = 25
# student['Place'] = "Bangalore"
# student['TotalMark'] = 562
# print(student)

# temp = {}
# temp['Sunday'] = 30.56
# temp['Monday'] = 31.25
# temp['Tuesday'] = 29.89
# print(temp)


# Q: Create a dict with key are btw
# 1 to 10 and values are square of keys

# d = {1:1,2:4,3:9,4:16,5:25.....10:100}

# d = {}
# d[1] = 1**2
# d[2] = 2**2
# d[3] = 3**2
# d[4] = 4**2
# print(d)

# d= {}
# for i in range(1,11):
#     # print(i)
#     d[i] = i**2
# print(d)


# from above list create a dict in which 
# keys will be each element of x and values are 
# whether it is "Odd" or "Even"

# out = {70:"Even",15:"Odd",68:"Even",.....}


# x = [70,15,68,61,32,89,46,13,56,11,78,36]
# d = {}
# for i in x:
#     # print(i)
#     if i%2 == 0:
#         d[i] = "Even"
#     else:
#         d[i] = "Odd"
# print(d)


# for loop in dict 

x = "Hello"
y = [50,60,70,"Python","Java",100]

# for i in x:
#     print(i)

# for j in y:
#     print(j)

z = {"Name":"Arun","Age":20,"Place":"Kochi",
     "Height":172}
# for k in z:   
#     print(k)   # keys

# print(z['Age'])
# print(z['Height'])
# print(z['Place'])

# for i in z:
    # print(i)
    # print(z[i])    # keys
    # print(i,z[i])    # keys and values

# for i in z.keys():
#     print(i)

# for i in z.values():
#     print(i)

# for i in z.items():  # i =(k,v)
#     print(i)

# for i,j in z.items():
#     print(i)   # keys
#     print(j)   # values


# e = {"Anu":56000,"Meera":48500,
#      "Saneesh":53500,'Akshay':51369,'Rahul':38965,
#      "Sana":53978,"Sneha":48787}   

#Q) increment each employee salary with 10% of their current salary and create a new dict 

# new = {}
# for i,j in e.items():
#     new[i] = round(j*1.10)
# print(new)

products = {"Laptop":62600,"Mouse":800,"Keyboard":2500,"Monitor":12000,"Ups":23000,"Speaker":31300}
# Create a new dict in which apply 20% discount if the product price is above 5000 and
# if price is below 5000 no change in price 

new = {}
for i,j in products.items():
    if j >= 5000:
        new[i] = round(j*.80)
    else:
        new[i] = j
print(new)
print(f"New dict = {new}")


Fname = "John"
Lname = "David"
Age = 22 
Place = "London"

# print('Hi my name is',Fname,Lname,". I am ",Age," Years old. I am from ",Place)
# formating 
# Format and Fstring 

print('Hi my name is {} {}.I am {} years old. I am from {}'.format(Fname,Lname,Age,Place))
print(f"Hi my name is {Fname} {Lname}.I am {Age} years old. I am from {Place}")
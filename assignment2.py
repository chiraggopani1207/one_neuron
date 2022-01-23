print("Name : CHIRAG GOPANI")
print("ASSIGNMENT 2")
# 1.What are the two values of the Boolean data type? How do you write them?
print("A : True and B : False")
a = True
b = False
print(type(a))
print(type(b))
# What are the three different types of Boolean operators?
# ANS  = There are 3 types of boolean operators : 1)AND ,2) OR ,3)NOT
# Make a list of each Boolean operators truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).
# for AND 1 (True)+ 0(False)  =(False) 0:   0 + 1 = 0   ; 0 + 0 = 0;  1 + 1 = 1
# for OR 1 (True)+ 0(False)  =(True) 1:   0 + 1 = 1  ; 0 + 0 = 0;  1 + 1 = 1
#  for NOT NOT(True)  =(False) 0:   NOT(False)   = 1  ;
''''What are the values of the following expressions?'''
print((5 > 4) and (3 == 5))
print(not (5 > 4))
print((5 < 4) or (3 == 5))
print(not ((5 < 4) or (3 == 5)))
print((True and True) and (True == False))
print((not False) or (not True))
# What are the six comparison operators?
"""Less than ( < )
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)
Equal to ( == )
Not equal to ( != )"""
a = int(10)
b =(20)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)
# How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.
# A = Assignment operator uses sigle "=" sign while equal to uses double "=="sign
x = int(10)


# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print("eggs")
# if spam> 5:
# print("bacon")
# else:
# print("ham)
# print("spam")
# print("spam")


spam = int(input("Enter any value :"))
if spam > 5:
    print("bacon")
elif spam==10:
    print("eggs")
else:
    print("spam")
# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.
spamm = input("Enter your value : ")
if spamm=="1":
    print("hello")
elif spamm=="2":
    print("howdy")
else:
    print("greetings")
# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# ?HIFT + ESC
# 10. How can you tell the difference between break and continue?
# A = break statement is used to stop the loop while certain callable object is reached while contine will be use to skip same object and print all other objects.
l = [1, 2, 3, 4, 5, 6]
for i in l:
    print(i)
    if i == 3:
        break
for i in l:

    if i == 3:
        continue
    print(i)
# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# A =in range(10) it will start from 0 till n-1:range(0,10) starting point is zero and will go till n-1:and in (0,10,1) it will start from 0 till n-1 with difference of 1
# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.
l = range(1,11)
for i in l:
    print(i)
az = 1

while az<11:
    print(az)
    az = az +1
# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?
# A=spam.bacon()
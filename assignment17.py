"""1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif)
 to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7."""
guess_me = 7
num =int(input("Enter your guess number between 1 to 20 : "))
if num==guess_me:
    print("Congrstulation!! you guessed correctly")
elif num>guess_me:
    print("Your guess number is higher")
else:
    print("your guess number is lower")
print("-" * 100)
"""2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while
loop that compares start with guess_me. Print too low if start is less than guess me. If start equals
guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit
the loop. Increment start at the end of the loop."""
start =1
while True:
    if start<guess_me:
        print("Too low")
    elif start==guess_me:
        print("Found it!")
        break
    else:
        print("OOPS")
        break
    start+=1
"""3. Print the following values of the list [3, 2, 1, 0] using a for loop."""
l1 =[3,2,1,0]
for i in l1:
    print(i)
"""4. Use a list comprehension to make a list of the even numbers in range(10)"""
l2 =[]
for x in range(11):
    l2.append(x)
print(l2[0: :2])

print("-"* 100)
"""5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the
keys, and use the square of each key as its value."""
print({x:x**2 for x in range(1,11)})
"""6. Construct the set odd from the odd numbers in the range using a set comprehension (10)."""
set_1 =range(10)
for s in set_1:
    if s%2==1:
        print(s)
"""7. Use a generator comprehension to return the string 'Got' and a number for the numbers in
range(10). Iterate through this by using a for loop."""
gen_com = ('Got_'+str(x) for x in range(10))
for ele in gen_com:
    print(ele, end=' ')


print("-"*100)
"""8. Define a function called good that returns the list ['Harry', &#39;Ron','Hermione']."""
def good():
    lst =["harry","ron","harmione"]
    return lst
print(good())
"""9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a
for loop to find and print the third value returned."""
def get_odds():
    output = []
    for ele in range(10):
        if ele%2 != 0:
            output.append(ele)
    yield output

next(get_odds())[2]

"""10. Define an exception called OopsException. Raise this exception to see what happens. Then write
the code to catch this exception and print &#39;Caught an oops&#39;."""
class OopsException(Exception):
    pass

def test(input):
    if input <0:
        raise OopsException(a)
try:
    test(-100)
except Exception as e:
    print('Caught in Oops ->',e)

"""11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit',
'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop']"""
title =["creature of habit","crewel fate"]
plots =["a nun turns monster","a haunted yarn shop"]
movies=dict(zip(title,plots))
print(movies)
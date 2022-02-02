"""1. Create an assert statement that throws an AssertionError if the variable spam is a negative
integer.
A = """
spam = int(-23)
assert spam >=0, "variable number should not be -ve integer"
print(spam)
"""2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain
strings that are the same as each other, even if their cases are different (that is,'hello' and 'hello' are
considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
A ="""
def raise_assert(egg,bacon):
    egg=egg.upper()
    bacon=bacon.upper()
    assert not(egg==bacon), "eggs/bacon should not be same"
print(raise_assert("hello","HELLO"))

"""3. Create an assert statement that throws an AssertionError every time."""
def assert_always():
    assert False, "always shows error"
print(assert_always())

"""4. What are the two lines that must be present in your software in order to call logging.debug()?
A= import logging
logging.basicConfig(filename ='application_log.txt',level=logging.DEBUG, format = %(asctime)s - %(level)s -%(message)s """
"""5. What are the two lines that your program must have in order to have logging.debug() send a
logging message to a file named programLog.txt?
A= """
"""6. What are the five levels of logging?
A = the five level of logging provided in python are CRITICAL(50),ERROR(40),WARNING(30),INFO(20),DEBUG(10),NOTSET(0)"""
"""7. What line of code would you add to your software to disable all logging messages?
a =logging.disable = True"""
"""8.Why is using logging messages better than using print() to display the same message?
A =post devlopment of your code you can disable logging function without removing logging function whereas you need to manually remove the print()
 which is tedious activity and also print is used when you wish to display any particular message"""
"""9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
A = step in is allow debugger to run next line of code and take pause again
step out will cause the debugger to run at full speed until it return to current place
step over function will run next line of code similar to step in however if next line of code is function call then it will step over the code in function"""
"""10.After you click Continue, when will the debugger stop ?
A = this will cause the program to run normally untill it reaches end or terminates"""
"""11. What is the concept of a breakpoint?
A = breakpoint is setting on line of code if debugger reaches that line that it will stop execution"""
import datetime
# Code to Add current date to the today.txt file
file = open('today.txt','w')
file.write(datetime.datetime.now().strftime("%d-%m-%Y"))
file.close()
# Code to Read current date from today.txt file
file = open('today.txt','r')
print(file.read())
file.close()
"""1. Add the current date to the text file today.txt as a string."""
"""2. Read the text file today.txt into the string today_string"""
file =open("today.txt","r")
today_string=file.read()
print(today_string)
file.close()
# """3. Parse the date from today_string."""
from datetime import datetime
parsed_data = datetime.strptime(today_string, '%d-%m-%Y')
print(parsed_data)

"""4. List the files in your current directory"""
import os
for folders,subfolders ,files in os.walk(os.getcwd()):
    for file in files:
        print(file)
"""5. Create a list of all of the files in your parent directory (minimum five files should be available)."""
import os
print(os.listdir())
"""6. Use multiprocessing to create three separate processes. Make each one wait a random number of
seconds between one and five, print the current time, and then exit."""
import time
import random
import multiprocessing
import datetime
def process1():
    print(f'process1 start time ->{datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'process1 end time ->{datetime.datetime.now()}')
def process2():
    print(f'process2 start time ->{datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'process2 end time ->{datetime.datetime.now()}')
def process3():
    print(f'process3 start time ->{datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'process3 end time ->{datetime.datetime.now()}')
# if __name__=="__main__":
#     p1 = multiprocessing.process(target=process1)
#     p2 = multiprocessing.process(target=process2)
#     p3 = multiprocessing.process(target=process3)

# print(p1.start())
# print(p2.start())
# print(p3.start())
#
# print(p1.join())
# print(p2.join())
# print(p3.join())

"""7. Create a date object of your day of birth."""
from datetime import datetime
my_birth_date = datetime.strptime("12-07-1992", "%d- %m- %y")
print(my_birth_date)

"""8. What day of the week was your day of birth?"""
from datetime import datetime
my_dob = datetime(1997,4,22)
my_dob.strftime("%A")
"""9. When will you be (or when were you) 10,000 days old?"""
from datetime import datetime, timedelta
my_dob = datetime.strptime("22/04/1997",'%d/%m/%Y')
future_date = my_dob-timedelta(10000)
future_date
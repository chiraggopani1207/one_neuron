"""1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the
number of seconds in a minute (60) by the number of minutes in an hour (also 60).
A ="""
seconds_in_min =60
min_hour =60
total_seconds_in_1_hour=seconds_in_min*min_hour
print("there is total ",total_seconds_in_1_hour ,"seconds in 1 hour")
"""2. Assign the result from the previous task (seconds in an hour) to a variable called
seconds_per_hour."""
seconds_per_hour = total_seconds_in_1_hour
"""3. How many seconds do you think there are in a day? Make use of the variables seconds per hour
and minutes per hour.
A ="""
seconds_in_day=(seconds_in_min*min_hour)*24
print("total seconds in a day is :",seconds_in_day)
"""4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day
A="""
seconds_per_day = seconds_in_day
"""5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
A ="""
a = seconds_per_day/seconds_per_hour
print(a)
"""6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree
with the floating-point value from the previous question, aside from the final .0?
A ="""
b =seconds_per_day//seconds_per_hour
print(b)
"""7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to
its next() method: 2, 3, 5, 7, 11, ...
A = """


def genPrimes():
    n = 0
    while True:
        if n == 2 or n == 3:
            yield n
        elif ((n - 1) % 6 == 0 or (n + 1) % 6 == 0) and n != 1:
            yield n
        n = n + 1


output = genPrimes()
for ele in range(10):
    print(next(output))
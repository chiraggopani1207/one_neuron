"""1. What exactly is []?
A = list is represented in [] brackets so its empty list"""
""""2. In a list of values stored in a variable called spam, how would you assign the value hello as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)"""
spam = [2,4,6,8,10]
spam.insert(2,"hello")
print(spam)
"""Let's pretend the spam includes the list ["a","b","c","d"] 
for the next three queries.
3. What is the value of spam[int(int('3' * 2) / 11)]?"""
spam =["a","b","c","d"]
print(spam[int(int('3'*2)/11)])
# "ans = d"
"""4. What is the value of spam[-1]?"""
print(spam[-1])
# Ans = d
"""5. What is the value of spam[:2]?"""
print(spam[ : 2])
# Ans = ["a","b"]
"""Let's pretend bacon has the list [3.14,"cat", 11, "cat", True] for the next three questions.
6. What is the value of bacon.index("cat")?"""
bacon = [3.14,"cat",11,"cat",True]
print(bacon.index("cat"))
# ans = it will take first "cat" position in list that is 1
"""7. How does bacon.append(99) change the look of the list value in bacon?"""
bacon.append(99)
print(bacon)
# Ans = append function will add value to last
"""8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?"""
bacon.remove("cat")
print(bacon)
# Ans = first "cat" is removed from list and if we run again second time same function then it will remove secont "cat"also
"""9. What are the list concatenation and list replication operators?
Ans = for concatenation same data type + is used and for replication of data type list * is used """
a1 = ["orange","mango" ," apple"]
a2 = ["cat","dog","rat"]
print(a1 + a2)#list concatination
print(a1 * 3)#list relication
"""10. What is difference between the list methods append() and insert()?
Ans = in list if you wish to add any data at end of list you can use append function while in indexing function can be used to add data to specific index number"""
a1.append("banana")
a2.insert(2,"rabbit")
print(a1)
print(a2)
"""11. What are the two methods for removing items from a list?
Ans = ypu can use .remove() function or del function to delete data from list"""
"""12. Describe how list values and string values are identical.
Ans = both list and string used in len() function,it can also be used in for loop, can be used in in and not in operator"""
"""13. What's the difference between tuples and lists?
Ans = tuple are immutable while list is mutable , tuple is written in() and list in [] """
"""14. How do you type a tuple value that only contains the integer 42?"""
t1 =(42,)
print(type(t1))
"""15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?"""
t1 = list(t1)
print(type(t1))
"""16. Variables that contain list values are not necessarily lists themselves. Instead, what do they
contain?
Ans  =strings,reference to list values """
"""17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans = copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list"""

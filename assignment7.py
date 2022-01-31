"""1. What is the name of the feature responsible for generating Regex objects?
A = REGEX means regular expression """
import re
x = re.compile("REGULAR EXPRESSION ")
print(type(x))
print(x)
"""2. Why do raw strings often appear in Regex objects?
A = As we have seen in previous assignment some special escape sequence are useful but if you use regex then this string will be used as raw string and not as escape sequence"""
"""3. What is the return value of the search() method?"""
match = re.search("i","INEURON tech company", flags=re.IGNORECASE)
print(match)
match1 = re.search("X","INEURON tech company", flags=re.IGNORECASE)
print(match1)
"""4. From a Match item, how do you get the actual strings that match the pattern?"""
match = re.search("chirag","chirag is good boy", flags=re.IGNORECASE)
print("output",match.group())
"""5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d), what does group zero cover?
Group 2? Group 1?
A = In the regex zero group covers entire pattern while first group covers (\d\d\d) and second group covers(\d\d\d-\d\d\d\d) """
isd_num = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mob = isd_num.search("my number is 222-333-4455")
print(mob.groups())
print(mob.group())
print(mob.group(1))
print(mob.group(2))
"""6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell
a regex that you want it to fit real parentheses and periods?
A = in regex \. ,\( and \) will match actual paranthesis"""
"""7. The findall() method returns a string list or a list of string tuples. What causes it to return one of
the two options?
A = If regex method has not groups then list of strings matched will be return and if regex method has groups then tuple will return"""
"""8. In standard expressions, what does the | character mean?
A = | == used as OR"""
"""9. In regular expressions, what does the character stand for?
A = in regular expression ? represents zero or one match of the preceeding group"""
sup_1 = re.search("super(man)?is alive","superman ")
sup_2 = re.search("super(woman)?is alive","superwoman")
print(sup_1)
print(sup_2)
"""10.In regular expressions, what is the difference between the + and * characters?
A= in regular expression * signifies zero or more occurances of preceeding group and + means more occurences of preceeding group"""
"""11. What is the difference between {4} and {4,5} in regular expression?
A = in regex if {4} is given the preceeding group is repeated 4 times and if {4,5} is given the it repeats minimum 4 and maximum 5 times"""
"""12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular
expressions?
A = \w matches word in regex expression from A-Z,a-z
\d matches digits from 0-9
and \s matches whitespace character like tab,space,newline etc"""
"""13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?
A=\W matched the non alphanumeric character
\D = matched the non digit character and 
\S matched all non whitespace character"""
"""14. What is the difference between .*? and .*?
A = .*? means greedy mode which returns longest string that matches and .* returns shortest string that matched"""
"""15. What is the syntax for matching both numbers and lowercase letters with a character class?
A =the syntex for matching is (a-z,0-9) or (0-9,a-z)"""
"""16. What is the procedure for making a normal expression in regax case insensitive?
A = use re.IGNORECASE"""
"""17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd
argument in re.compile()?
A =. matches everthing except newline character ,
by passing re.DOTALL as flag to re.complie() you can match all character including new line"""
"""18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X','11 drummers, 10 pipers, five rings, 4
hen') return?"""
numReg = re.compile(r'd+')
print(numReg.sub( "x" , "11 drumers , 10 pipers, five rings , 4 hen"))
"""19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
A = re.VERBOSE will allow whitespace and comments to string passed to re.compile()"""
""""20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
'42','1,234', '6,368,745'but not the following: '12,34,567' (which has only two digits between the commas) '1234' (which lacks commas)

import re
pattern = r'^\d{1,3}(,\d{3})*$'
pagex = re.compile(pattern)
for ele in ['42','1,234', '6,368,745','12,34,567','1234']:
    print('Output:',ele, '->', pagex.search(ele))
Output: 42 -> <re.Match object; span=(0, 2), match='42'>
Output: 1,234 -> <re.Match object; span=(0, 5), match='1,234'>
Output: 6,368,745 -> <re.Match object; span=(0, 9), match='6,368,745'>
Output: 12,34,567 -> None
Output: 1234 -> None
21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'

but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)"""

Ans: pattern = r'[A-Z]{1}[a-z]*\sWatanabe'

import re
pattern = r'[A-Z]{1}[a-z]*\sWatanabe'
namex = re.compile(pattern)
for name in ['Haruto Watanabe','Alice Watanabe','RoboCop Watanabe','haruto Watanabe','Mr. Watanabe','Watanabe','Haruto watanabe']:
    print('Output: ',name,'->',namex.search(name))


"""22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'

but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'

Ans: pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'

import re
pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
casex = re.compile(pattern,re.IGNORECASE)
for ele in ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.'
,'ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']:
    print('Output: ',ele,'->',casex.search(ele))
"""

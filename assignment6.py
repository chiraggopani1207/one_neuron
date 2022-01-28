"""1.What are Escape characters ? and how do you use them ?
A = escape characters will generally merge with string if not used with backslash for ex \n for new line and \t for tab"""
"""2.What do the escape characters n and t stand for ?
A = \n is for creating new line and \t for giving tab"""
"""3.What is the way to include backslash character in a string?
A = to create single back slash you need to use  double backslash\\"""
"""The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem ?
A= you can use single quote inside doble quote,if you are using single quote for string also then you have to use \' toescape the character
"""
"""5.How do you write a string of newlines if you don't want to use the n character?
A = if you wish to break with new line without actually going in new line there you can select escape sequence \n"""
"""6.What are the values of the given expressions ?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
A = in above example strring slicing is used find below solution
'Hello, world!'[1] = e
'Hello, world!'[0:5]=Hello
'Hello, world!'[:5]=Hello
'Hello, world!'[3:]=lo, world!
"""
"""7.What are the values of the following expressions ?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
A = 'hello'.upper() will create string in uppercase  = 'HELLO'
'Hello'.upper().isupper() will check whether string is in upper case or not = True
'Hello'.upper().lower() is converting hello in lower case again = 'hello'"""
"""8.What are the values of the following expressions ?
'Remember, remember, the fifith of July.'.split()
-'.join('There can only one'.split())
A = split function is used to split any string according to users specification in parentheses() and converting it into list
'Remember, remember, the fifith of July.'.split() -> ['Remember,', 'remember,', 'the', 'fifith', 'of', 'July.']
'-'.join('There can only one'.split()) -> 'There-can-only-one'"""
"""9.What are the methods for right-justifying, left-justifying and centering a string ?
A = rjust(),ljust() and center() is the methods for justifying any string"""
"""10.What is the best way to remove whitespace characters from the start or end ?
A = to remove whitspaces we use lstrip() and rstrip() methods"""
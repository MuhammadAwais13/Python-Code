#To understand f string we first have to understand string formatting
# String formatting in Python refers to the process of inserting variables, expressions, or values into strings.

str="my name is {} and your name is {}" #now using string formatting i can replace these curly brackets with values of variables 

name1="Awais"
name2="Ali"

print(str.format(name1,name2)) #this format function will replace name1 with first bracket and name2 with second 
#this is called string formatingin which we are inserting variables inside strings

#another example
str="my name is {} and my money {}"
name1="Awais"
money=10*30
print(str.format(name1,money)) #in this an expression is replaced in brackets


str="my name is {1} and my money {0}" #we can also give indexes in this now place of name1 and money is changed 
name1="Awais"
money=10*30
print(str.format(name1,money)) #in this an expression is replaced in brackets


#THIS way of string formatting is difficult we have to use vrain in understandin curly brackets and indexes

#so we can also use f string
str=f"my name is {name1} and my money {money}" #by using fstring we can directly add variables in curly brackets
str=f"my name is {name1} and my money {100*30}"
print(str)

#in fstring we simply write f before starting string brackets





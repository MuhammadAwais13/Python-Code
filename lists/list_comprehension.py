#LIST COMPREHENSION 

#it is a way in which we create a new list by:

list=["apple", "banana", "cherry", "kiwi", "mango"]

new_list=[x for x in list if "a" in x]
print(new_list)
#now it is like this value of x will be return to new list then for loop starts and in for loop it will 
#chexk if conditions if a is found in list then that whole of x will be return to starting x and will be stored as value in new lsit
#if there is no if condition it will return all values of x hence a duplicate will be formed
new_list=[x for x in list ]
#this line is same for all after that we can add any condition of aur liking 

print(new_list)

#if we do any changes to starting x it will it will accept values with modifications like this 

new_list=[x.upper() for x in list ]
#first values will be made upper then stored to new list
print(new_list)



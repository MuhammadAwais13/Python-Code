#Tupples: these are same like list and we can itrate them like lists but 
tup=(1,2,3,4,5)#they are made with round brackets 
#tupples cannot be changed means we can not add or remove same values of tupple 
#tup[5]=12 #this will give error as we cannot change or add new values 
#there is one by which we can change them is by firsst converting them to list
llist=list(tup)#first change to list
llist[4]=123#change value in list 
tup=tuple(llist)#list change back to tuple
print(tup)
#we can conncatinate or add two tupples but result will be stored in new tupple 
sectup=(12,2,3,4,4,5,5)
new_tup=tup+sectup          
print(new_tup)

#so by this we can concatinate tupples but cannot change a tupple

#and all methods use in list which dosent change anything inside list like index count etc. we can also use these in tuples
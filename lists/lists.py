
marks=[34,67,34,67,98,23,67]
for i in marks:         #this for loop will itrate on list 
    print(i)

print(marks[:])    #this will automatically print list from 0:6
print(marks[3:6])   #this will only print from index 3 to index 6
print(marks[3:-2])   #whenever there is a minus index python will replace it with lenth of list - 2
print(marks[0:6:2])  #this additional 2 tells that ist element will be printed then 2 will be left then 3rd will be printed and so on

#list methods

#1 append
l=[1,12,3,4,5,6,7,8]

l.append(12) #12 will be added at last of list 


#2 sort

l.sort()     #this will sort list in assending order 

print(l)

l.sort(reverse=True)     #this will sort list in opposite order


#3 index

l.index(4) #it will find number 4 in list and then will print index of it if there are more than one then it will print index of frst occourance 


#4 count

l.count(1) #it will count how many times one has appeared in list 

#5 insert 

l.insert(1,123)   #it will insert 123 at 1st index 


#6 extend

m=[1,23,4,5,6,7]

l.extend(m) #it will extend m by puttig values of m at end 







#what is list comprehension 

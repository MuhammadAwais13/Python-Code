# #how to declare a function 

# def newfunc(a,b):         #this is how we declare a function in python def kefword is used with name of function 
#     sum=a+b                #there are no brackets we only give indentation at start
#     return sum            


# a=2
# b=3
# print(newfunc(a,b))           


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#





#now in function arguments if we dont know how many values will function take we can make aregument a list or tupple 

def average(*a): #as a is a list which contain many values so in order to use values of a we have to itrate in a using for loop
    sum=0
    for x in a:
        sum=sum+x
    average = sum/len(a)
    print(average)    


average(2,3,4,5,6,6,8,65,4) #now we can give as many values as possible
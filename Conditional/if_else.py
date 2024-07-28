# a=int(input())

# if(a>12):
#     print("you have won ")   #this space before print is called indentation in python we dont use indentation
#                              #rather we use space before or statement whenever we put this space below if 
#                              #consectively we are in body of if 


# elif(a<4):  #elif is just like elseif in c++
#     print("these are less tha 4")                            

    
     
# else:     #now as here space is not putted we are outside if
#     print("lost")    
# print("thsi print statement is outside else bode as no indentation ")


#exercise for if else 


import time 

# timecheck=int(time.strptime('%H:%M:%S'))
timecheck=int(time.strftime('%H'))
if(timecheck>9):
    print("good morning")
elif(timecheck>12):
    print("good afternoon")

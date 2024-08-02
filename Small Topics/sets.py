#there used  for collections of data 
#we use these when we dont want to have multiple copies in set
#they are enclosed in curly brackets
s={1,2,3,4,5,2,2,3,4,5,6,5,5,4,3,2,1}
#as we can see all repeted are only once taken in output
print(s)
#there is no garantuee of order mentainance in sets means if we print same set multiple times there values may
#change there index 
#so we cannot give indexes to sets values 
d={"awais",1,1.2,True,"ashraf"}
print(d)
#so when i print d multy times sometimes awais is at start and somtimes at end and so on 
awais={}
print(type(awais)) #type will be dictionary because when there are only curly brackets it will assume it a dict


##############################################################################
##############################################################################

#Methods IN SETS 

##############################################################################
##############################################################################
#union
#union is just like union of mathmatics 
a={1,2,3}
b={3,4,5}
print(a.union(b)) #same like math union but it dosenot update a or b they remain same 

#update
a.update(b)  #this updaate act as union now answer will be stored in a means in this a will be changed 

#intersection
#intersection only same in both sets will remain 
print(a.intersection(b))

#intersection_update
#this is same like privios update but previous act as union but this aaact as intersection 
a.intersection_update(b)


#symetric difference = AuB - AnB 
#this means common will be removed from union #

print(a.symmetric_difference(b))

#symmetric_difference_update this update is also same but will act as symetric diff update
a.symmetric_difference_update(b)
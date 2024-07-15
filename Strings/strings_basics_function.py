#some functions for working with strings 


# 1-   len() ----------------------------------

a="my name is awais "
print(len(a)) #this prints lenth of a string

  
#2-   upper() -----------------------------------

#changes string to upper case letter 

print(a.upper())


#3-    lower() --------------------------------
#changes string to lower case

print(a.lower())


#4-    rstrip("thing to be strip") ------------------------------
#this strip anything written inside rstrip from steing

print(a.rstrip(" "))#this will remove spaces from a string 


#5-     replace() ---------------------------

print(a.replace("awais","ashraf")) #it will replace awais with ashraf in a string 



#6-     split() ------------------------------


print(a.split(" ")) #it will split a string into list whenever space is encountered


#7-     center()

print(a.center(50)) #this will write every thing in a in center such that it will leave spaces at start to 
#complete 50 length now new length of string is 50------we can always change 50 to any other length 


#8-    endswith it check if your string ends with what you are asking it ends with if yes then prints true 
# #if false then prints -1

print(a.endswith("asas"))# as our a string dosenot ends with aa so it will return -1


#9-


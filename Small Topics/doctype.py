#Doctypes:  Python documentation strings (or docstrings) provide a convenient way of associating documentation 
# with Python modules, functions, classes, and methods. It’s specified in source code that is used,
#  like a comment, to document a specific segment of code. Unlike conventional source code comments, 
# the docstring should describe what the function does, not how.

def adition(n1,n2):
    '''adding of n1 with n2'''    #these are written just after function defination if anything is written before them python will not reconize it
    return n1+n2
print(adition(12,3))
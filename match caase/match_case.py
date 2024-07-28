#match case is just like switch case of c++

x=int(input())

match x:
    case 1:#there is no break statement in python 
        print("case one is being printed")
    case 2 if x<3: #we can also write conditions in cases 
        print("case 2 is printed ")
        y=int(input())
        match y:  #nested match case statements
            
            case 1:
                print("xyz")
    case _:#default is printed by using this 
        print("default is printed")        

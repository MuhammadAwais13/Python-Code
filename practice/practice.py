#first practice assignment KAUN BANE GA CAROREPATI

print("Welcome to kaun bane ga carore patii ")

ques=["QUESTION 1: Capital of pakistan","QUESTION 2: How many provinces are in pakistan","QUESTION 3: who is priminister of Pakistan"]
balance=0
for i in range(len(ques)):
    print(ques[i])
    match i+1:
        case 1:
            ans1=["1: Karachi","2: islamabad"]
            print(ans1)
            inp=input()
            if(inp==1):
                print("you lost")
                print("you lost yor balance",balance)
                quit()
            else:
                balance+=1000000
                print("congratulation you won 1000000")
        case 2:
            ans1=["1: Four","2: Three"]
            print(ans1)
            inp=input()
            if(inp==2):
                print("you lost")
                print("you lost yor balance",balance)
                quit()
            else:
                balance+=1000000
                print("congratulation you won 1000000")  
        case 3:
            ans1=["1: Imran Khan ","2: SHAHBAZ Sharif"]
            print(ans1)
            inp=input()
            if(inp==1):
                print("you lost")
                print("you lost yor balance",balance)
                quit()
            else:
                balance+=1000000
                print("congratulation you won 1000000")              

print("Final Balance::",balance)
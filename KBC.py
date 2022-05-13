print("Toh taiyar rhein, hmare swalon ke jwab ke sath..,")
print("computer ji inhen question dikhaiye..ye rha screen pe hmara phle swal.... ")
qu=["Q.1 how many color in rainbow?",
"Q.2 who is the father of indian consitution of india?",
"Q.3 what is the national flower of india?",
"Q.4 what is the national animal of india?"]
op=[["two","seven","four","eight"],
["BR Ambedkar","Dr.Rajendra prasad","mahatma gandhi","mohammd ali zinna"],
["rose","lotus","sunflower","hibiscus"],
["lion","elephant","dog","tiger"]]
sol=[2,1,2,4]
anslist=[
    ["2.seven","3.four"],
["2.BR Ambedkar","3.mahatma gandhi"],
["1.rose","2.lotus"],
["1.lion","4.tiger"]]
i=0
count=0
price=0
while i<len(qu):
    print(qu[i])
    j=i
    sno=0
    while (sno<len(op[i])):
        a=op[j][sno]
        print(sno+1,a)
        sno+=1 
    if count==0:    
        lifeline=input("do u want lifeline:-yes/no")
        if lifeline=="yes":
            count+=1 
            print("select your option")
              
            se=0
            b=i
            while se<len(anslist[i]):
                c=anslist[b][se]
                se+=1
                print(c)
            ans=int(input("choose your answer")) 
            if ans==sol[i]:
                price+=1000
                print("your answer is correct, and your winning price is",price)
                print("congraculation")
                print("your next que is:")
            else:
                print("your answer is wrong")
                print("your next que is:")
                # break  
            count+=1
        else:
            print("you already use ur lifeline")
            ans1=int(input("plz enter your answer"))
            if ans1==sol[i]:
                price+=1000
                print("your answer is correct, and your winning price",price) 
                print("congraculation")
            else:
                print("your answer is wrong")
                print("your next que is")
                break
    else:
        ans2=int(input("enter your answer:"))
        if ans2==sol[i]:
            price+=1000
            print("your answer is correct and your winning price is",price)   
        else:
            print("wrong answer")    
    i+=1
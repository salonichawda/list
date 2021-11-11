question_list = [
    "How many continents are there?",              # pehla question

    "What is the capital of India?",            # doosra question

    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]
options_list = [
    #pehle question ke liye options

    ["Four", "Nine", "Seven", "Eight"],

    #second question ke liye options

    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],

    #third question ke liye options

    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
anslist=[
    ["2.nine","3.seven"],
    ["3.bhopal","4.delhi"],
    ["1.Software Engineering","2.Counseling"]
]
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
i=0
count=0
price=0
while i<len(question_list):
    print(question_list[i])
    j=i
    serialno=0
    while serialno<len(options_list[i]):
        k=options_list[j][serialno]
        print(serialno+1,k)
        serialno+=1
    lifeline=input("do you want 50-50 lifeline..yes/no:")
    if lifeline=="yes":
            print("you choose 50-50")
            if count<1:
                serial=0
                a=i
                while serial<len(anslist[i]):
                    b=anslist[a][serial]
                    serial+=1
                    print(b)
                ans=int(input("choose your answer:"))
                if ans==solution_list[i]:
                    price+=10000
                    print("right answer and your wining price is",price)
                else:
                    print("your answer is wrong,you lost the game")
                    break
                count+=1
            else:
                print("you already use your life line")
                ans1=int(input("plz enter your answer:"))
                if ans1==solution_list[i]:
                    price+=10000
                    print("right answer and price is",price)
                else:
                    print("your answer is wrong and price is",price)
                    break
    else: 
        pass
        ans2=int(input("enter your answer:"))
        if ans2==solution_list[i]:
            price+=10000
            print("your answer is right and price is",price)
        else:
            print("wrong answer")
            break
    i+=1

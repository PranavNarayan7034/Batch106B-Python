a = "Welcome to the Quiz"
print(a)
points = 0
que_no = 0

que_no += 1
que = input("1.What is the largest ocean on the earth?").lower()
if que == 'pacific ocean':
    print("Your answer is correct")
    points += 2
else:
    print("Your answer is wrong")
    print("correct answer is Pacific ocean")
    
con = input("Do you want to continue the quiz?(y/n)").lower()
if con == 'y':
    que_no +=1
    que = input("2.Which gas do plants absorb from the atmosphere").lower()
    if que == 'carbon dioxide':
        print("Your answer is correct")
        points += 2
    else:
        print("Your answer is wrong")
        print("correct answer is Carbon dioxide")
    con = input("Do you want to continue the quiz?(y/n)").lower()
    if con == 'y':
        que_no +=1
        que = input("3.What is the fastest land animal").lower()
        if que == 'cheetah':
            print("Your answer is correct")
            points += 2
        else:
            print("Your answer is wrong")
            print("correct answer is cheetah")
        con = input("Do you want to continue the quiz?(y/n)").lower()
        if con == 'y':
            que_no +=1
            que = input("4.Which planet is known as the Red Planet").lower()
            if  que == 'mars':
                print("Your answer is correct")
                points += 2
            else:
                print("Your answer is wrong")
                print("correct answer is Mars")
            con = input("Do you want to continue the quiz?(y/n)").lower()
            if con == 'y':
                que_no +=1
                que = input("5.Which animal is known as the king of the Jungle").lower()
                if que == 'lion':
                    print("Your answer is correct")
                    points += 2
                else:
                    print("Your  answer is  wrong")
                    print("correct answer is Lion")
            else:
                print("Total no of questions answered:",que_no)
                print("Your total points is:",points)
        else:
            print("Thank you for the participation")

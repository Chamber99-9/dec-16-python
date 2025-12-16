"""5 == 5
5!=2
5>3"""      # Just testing operators


"""print("and" True and True)
print("or" True or True)            
print("not" not(False))"""      #Just testing logical operators

"""data = True
data = not(data)

if(data):
    print("The data is true")
else:                               
    print("The data is false")

"""                                 #Just testing if else condition

dept="IT"
exp=10
per_sc=90

if(dept=="IT"):
    if(exp>=5):
        if(per_sc>=90):
            print("Bonus is 20 percent")
        elif(per_sc>=70 and per_sc<=89):
            print("Bonus is 12 percent")
        else:
            print("Bonus is 5 percent")
    elif(exp<=5):
        if(per_sc>=85):
            print("Bonus is 10 percent")
        else:
            print("Bonus is 3 percent")
elif(dept=="HR"):
    if(per_sc>=80):
        if(exp>3):
            print("Bonus is 15%")
        else:
            print("Bonus is 7 percent")
    else:
        print("Bonus is 4 percent")
else:
    if(exp>4):
        print("Bonus is 6 percent")
    else:
        print("Bonus is 2 percent")
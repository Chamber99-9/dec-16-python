"""
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
"""

# Assignment : Get input from everyone and do it


department = input("What department do you work on ? ")
experience = int(input("What's the work experience you have got ? "))
performance_score = int(input("What's the percentage score you have got ? "))
salary = float(input("Enter the salary you have got ? "))

if department == "IT":
    if experience >= 5:
        if performance_score >= 90:
            bonus = 0.20 * salary
            total_money=salary+bonus
            print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
        elif performance_score >= 70 and performance_score <= 89:
            bonus = 0.12 * salary
            total_money=salary+bonus
            print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
        else:
            bonus = 0.05 * salary
            total_money=salary+bonus
            print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
    elif(experience<5):
        if performance_score >= 85:
                bonus=0.10* salary
                total_money=salary+bonus
                print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
        else:
            bonus=0.03*salary
            total_money=salary+bonus
            print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')

elif(department=="HR"):
    if(performance_score>=80):
        if(experience>=3):
            bonus=0.15*salary
            total_money=salary+bonus
            print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
        else:
            bonus=0.07*salary
            total_money=salary+bonus
            print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
    else:
        bonus=0.04*salary
        total_money=salary+bonus
        print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
else:
    if(experience>=4):
        bonus=0.06*salary
        total_money=salary+bonus
        print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
    else:
        bonus=0.02*salary
        total_money=salary+bonus
        print(f'The total salary after the bonus is {total_money} and the only bonus is {bonus}')
#List comprehension
# It means using the list loop inside it along not creating a longer syntax model using for loop

#finding if a is present in those lists words
"""
ls=["apple","banana","cherry","cardboard","reference"]
finls=[x for x in ls if "a" in x]
print(finls)"""

#Create a list of numbers from 1 to 10 using list comprehension.


"""lamy=(x for x in range(1,11)):
    print(lamy)"""

#Create a list of squares of numbers from 1 to 10.

"""l=[x**2 for x in range(1,11)]
print(l)"""

#Create a list of even numbers from 1 to 20.

"""even=[x for x in range(1,21) if x%2==0]
print("X is even", even)"""

#Create a list of odd numbers from 1 to 20.

"""odd=[x for x in range(1,21) if x%2!=0]
print(odd)"""

#Convert a list of integers to strings.
"""inte=[1,2,3,4,5]
conv=[str(x) for x in inte ]
print(conv)"""

#Convert a list of strings to uppercase.
'''st=["apple","banana","rodeo"]
Up=[x.upper() for x in st ]
print(Up)'''

#Create a list of lengths of each word in a list.
"""lys=["Apple","Commander","Gegegogo"]
wo=[len(x) for x in lys ]
print(wo)"""

#Extract the first letter of each word in a list.

"""lys=["Poem","Restrict","India"]
ext=[x[0] for x in lys] 
print(ext)

"""

#Add 5 to each element in a list.

"""lys=[1,2,3,4]
xin=[x+5 for x in lys]
print(xin)"""

#Create a list of boolean when numbers are greater than 5
"""bol=[5,10,15,20,25]
gre=[x>5 for x in bol]
print(gre)
"""

#Create a list of numbers divisible by 3 from 1 to 50.
"""num=[x for x in range(1,51) if x%3==0 ]
print(num)
"""

#Filter out negative numbers from a list.
"""numlist=[-1,2,-4,7,9,10,-11]
lys=[x for x in numlist if x<0  ]
print(lys)
"""

#Extract words longer than 5 characters.
"""lys=["Apples","Wowo","Ramu","Ninjas"]
les=[x for x in lys if len(x)>5]
print(les)"""

#Create a list of squares of even numbers only.
"""lys=[1,2,3,4,5,6,7,8]
nbs=[x**2 for  x in  lys if x%2==0 ]
print(nbs)"""

#Create a list of numbers that are multiples of both 2 and 5.
"""X=[1,2,3,4,5,6,7,8,9,10]
Y=[x for x in X if x%2==0 and x%5==0]
print(Y)"""

#Replace negative numbers with 0.
"""X=[1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
=[x==0 for x in X if x<0 ]
print(X)
"""

#Create a list of vowels from a string.
"""lys=["Ramboisalive"]
vow=["aeiouAEIOU"]
per=[x for x in lys if vow in lys]
print(per)"""

#Extract numbers greater than the average of the list.
lys=[10,12,15,18,20]
avg=[x for x in lys if sum(lys>avg(lys))]
# Create a class Car with attributes brand and color. Create two objects and print their values.
"""class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

car1=Car("BMW","Maroon")
car2=Car("Porsche","Grey")

print(car1.brand,car2.brand)
print(car1.color,car2.color)
"""
# Create a class Student with a constructor that takes name and age. Create an object and display the values.

"""class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
Student1=Student("Rishi",20)
Student2=Student("Manoj",75)

print(Student1.name, Student1.age)
print(Student2.name,Student2.age)
"""

# Write a class Dog with a method bark() that prints “Woof!”. Create an object and call the method.

"""class Dog:
    def bark(self):
        print("Woof!")        
d=Dog()
d.bark()
"""

# Make a class Mobile with attributes model & price. Use constructor to assign values. Print values.
"""class Mobile:
    def __init__(self,model,price):
        self.model=model
        self.price=price
Mobile1=Mobile("Huawei",1000)
Mobile2=Mobile("Xiaomi",2000)
Mobile3=Mobile("Apple",100000)

print(Mobile1.model,Mobile1.price)
print(Mobile2.model,Mobile2.price)
print(Mobile3.model,Mobile3.price)"""

# Create a class Rectangle with length and width. Write a method to calculate Area.
"""class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width
    
Area=Rectangle(10,5)    
print(Area.area())
        """


# TO find the volume of the following
"""class Volume:
    def __init__(self,length,breadth,width):
        self.length=length
        self.breadth=breadth
        self.width=width

    def volume(self):
        return self.length * self.breadth * self.width

Vol=Volume(5,10,5)
print(Vol.volume())
    """

# Create a class Person with constructor taking name & country. Add a method introduce().
"""class Person:
    def __init__(self,name,country):
        self.name=name
        self.country=country

    def intro(self):
        print(f'The name is {self.name} and country is {self.country}')
    
Pery=Person("Kratos","Nepal")
Pery.intro()"""

# Create a class BankAccount with attributes name, balance. Add methods: deposit(amount) and withdraw(amount).**
"""class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        

    def deposit(self,amount):
        self.balance+= amount

    def withdraw(self,amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Insufficient balance")
BA=BankAccount("Kratos",10000)
BA.deposit(150000)
BA.withdraw(50000)
print(BA.balance)
"""

# Make a class Employee with:
"""name
salary
position
Write a method to increase salary by 10%.**
"""


""""class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def increment_salary(self):
        self.salary*=0.10


e = Employee("Kratos", 10000, "Dev")
e.increment_salary()
print(e.salary)"""

# *9. Create a class Book with title, author, pages.
#Add method: is_big_book() → return True if pages > 300.**

"""class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def is_big_book(self):
        if(self.pages>300):
            return True
        else:
            return False
pg=Book("Heartwarming","Sukule",200)
print(pg.is_big_book())"""

#Create a class Calculator with add, subtract, multiply, divide methods.

"""class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def addition(self):
       return self.num1 + self.num2
    
    def subtract(self):
        
       return self.num1-self.num2
    
    def multiply(self):
        
        return self.num1*self.num2
    
    def divide(self):
        return self.num1/self.num2
    
calc=Calculator(10,11)


print(calc.addition(),calc.subtract(),calc.multiply(),calc.divide())

"""

#Create a class Laptop with attributes (brand, RAM, price).
#Add method upgrade_ram(new_ram) that changes RAM.*
"""
class Laptop:
    def __init__(self,brand,RAM,price):
        self.brand=brand
        self.RAM=RAM
        self.price=price
    def upgrade_ram(self, new_ram):
        self.RAM =new_ram
    
Niu=Laptop("Dell",8,1999)
Niu.upgrade_ram(16)
print(Niu.RAM)"""

# Build a class ShoppingCart that stores a list of items and has methods:
# add_item(item)
# remove_item(item)
# total_items()**

"""class ShoppingCart:
    def __init__(self):
        self.lists=[]
    def add_item(self,item):
        self.lists.append(item)
    def remove_item(self,item):
        self.lists.remove(item)
    def total_items(self):
        return len(self.lists)
Shop=ShoppingCart()
Shop.add_item("Roblox")
Shop.add_item("Insta")
Shop.remove_item("Roblox")
print(Shop.total_items())
        """

#Create a class Point with x and y.
#Add a method to calculate distance between two points.

"""import math

class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    def distance(self,others):
        return math.sqrt((self.x - others.x)**2 +(self.y - others.y)**2)
P1=Point(5,6)
P2=Point(7,8)
print(P1.distance(P2))

"""

#Create a class Car that counts how many objects are created.

"""class Car:
    count=0
    def __init__(self):
        Car.count +=1
c1=Car()
c2=Car()
c3=Car()
print(Car.count)"""

#Create a class Employee with a private salary attribute.
#Add getter and setter methods.

"""class Employee:
    def __init__(self,ssalary):
        self.ssalary=ssalary
    def setsalary(self):
        self.
"""

#Create a class AnimeCharacter with name and power.
#Add a method fight().

"""class AnimeCharacter:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def fight(self,other):
        if(self.power >= other.power):
            return self.name +"wins"
        elif(self.power <= other.power):
            return other.name +"wins"
        else:
            print("Draw ")
an1=AnimeCharacter("Apple",800)
an2=AnimeCharacter("Anike",700)
print(an1.fight(an2))
    

"""
#Best among SUVs
class Cars:
    def __init__(self,name,clearance):
        self.name=name
        self.clearance=clearance
        
    def comparision_model(self,other):
        if(self.name=="Elevate"):
            if(self.clearance >= other.clearance):
                return self.name +"best"
            else:
                return("Please go scrap that car")
    
c1=Cars("Elevate",220)
c2=Cars("Nexon",180)
c3=Cars("Seltos",190)

c1.comparision_model()
c2.comparision_model()
c3.comparision_model()

print(c1.comparision_model(c2))
print(c2.comparision_model(c3))
        
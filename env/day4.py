#data removal from list
# To remove data use syntax :del data
# delete method
"""lst=[7,8,9]
del lst"""          # if given an empty list then it will delete the variable of the lst
"""del lst[1]"""    #giving index number is for delete
"""print(lst)"""

#.remove method
"""lst.remove(9)""" # Giving the value of the variable

#.pop() method
"""lst.pop()        # Deletes the last value of the list
lst.pop(0)"""       # Deletes the indexing of the list

# Printing the value 8
"""data=[1,2,3,4,[5,6,7,[8,9,0]]]
print(data[-1][-1][0])""" # it becomes like 
                        # a= data(-1) i.e it becomes [5,6,7,[8,9,0]]
                        #b=a(-1) i.e it becomes [8,9,0]
                        #c=b(0) i.e it becomes [8]



#Dict  follows Polymorphism

data={
    "id":101,
    "name":"Sisam",
    "class":8,
    "age":13,
    "marks":[7.8,10,11,12],
    "address":"VIP"
}


"""print(data["name"]).  # Printing of data according to the key 
print(data.values())     # It accesses all of the values of the dict
print(data.keys())       # It access all the key of the dict
print(data.clear())"""   # Clears all the data of dict

"""data['bike']='SuperDuke' 
print(data)"""                                      # Adds the value one at a time

"""data.update({"name":"Ronaldo","bike":"Kawasaki H2"})     # updates the multiple value at the same time 
print(data)"""

"""data.update({"marks":[8,12,15,18,25]})"""

#Deleting data 

"""del data['class']   #Delets the key 'class'
data.pop('name')  #Deletes the key 'name'
data.popitem()         # Deletes the key of the last index i.e deletes 'address' key   
data.clear()            # Clears the entire dictionary

# Using get 
print(data)
print(data.get("ags","No data found")) # Only used for specific purpose
"""

#Nested dict
"""student = {
    "id": 101,
    "name": "Sudan",
    "age": 22,
    "course": "Python",
    "marks": [78, 85, 90],
    "is_active": True,
    "num":{
        "ntc":980,
        "ncell":{
            "telecom":"nepal"
        }
    }
}

tot_marks= student['mars']

print(f"{student['name']}'s total marks is {student ['marks'][0]+ student['marks'][1]+ student['marks'][2]} and the course is {student['course']}")
"""

"""
You are given a dictionary containing a students details:
name
marks (list of integers)
status
Write a program that checks using conditional statements whether:
the student is "active"
the total marks are greater than 350
the number of subjects is at least 5
Print "Eligible" or "Not Eligible" accordingly.
2️

"""

"""dice={
    "name":"Shashwot",
    "marks":[500,800,1000],
    "subject":["English","Nepali","Science","COplar","DataSc"],
    "status":"active"
}
if ((dice['status']=='active') and (dice['marks'][0]+dice['marks'][1]+dice['marks'][2]> 350) and len(dice['subject'])>=5):
    print("Eligible")

else:
    print("Not Eligible")


"""

"""You are given a dictionary representing a product with keys:
price, discount, and stock.
Write a conditional program to determine whether:
discount should be applied only if price > 1000
final price after discount is less than 2000
stock is not zero
Print "Purchase Allowed" or "Purchase Not Allowed".
"""

"""product={
    "price": 5500,
    "discount": 500,
    "stock": 150,
    "final_price": 4000
}

if (((product['price'])>=1000 and (product['final_price'])=<2000 and (product['stock']!==0))):
    print("Purchase Allowed")
else:
    print("Purchase not allowed")
"""

# python dictionary 
person ={
    "first name" : "John" ,
    "Last name"  :  "Doe" ,
    "Age"  :  25 ,
    "Favourite colors" : ["blue","green"] ,
    "salary"  :  5000
}
#  show output 
print(person) 
# access the key value 
# 1. age 
print(person["Age"])

# 2.salary
print(person["salary"])

# 3. last name 
print(person["Last name"])

# updating
person["Age"] =34
# show output 
print(person)
person["Last name"] = "silayo"
# show output
print(person)

# add new key value 
person["passport"] = "2294850"

# show output
print(person)

# delete key value 
# 1. delete last name 
del person["Last name"]
# show output 
print(person)
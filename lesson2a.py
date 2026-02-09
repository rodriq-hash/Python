# python list 
cars =["Honda", "Nissan", "Surf", "Mazda", "Volkswagon"]
# print the cars 
print(cars)

# access item at index 2 
print(cars[2])
# access item at index 3 
print(cars[3])

# appending items in a list 
cars.append("BMW")
# show output 
print(cars)

# inserting items at specific index 
# insert Toyota at index 2
cars.insert(2,"Toyota")
# show output 
print(cars)

# slicing 
# 1. print items from index 2 upto index 5 
print(cars[2:5])

# 2. print from index 2 and above 
print(cars[2:])

# 3. print up to index 4 and below 
print(cars[ :4])
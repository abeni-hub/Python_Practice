# TO get list type
lst = [1,2,3]
print(type(lst))

# TO create lists
names = ["Grum","Biruk","Firea"]
print(names)

# Accessing list elements
fruits = ["banana","apple","orange","kiwi"]
print(fruits[0])
print(fruits[3])
print(fruits[-1])

# To get all elements as alternatives
print(fruits[0:])
print(fruits[0:3])


# Modifiying the list elements
fruits[1] = "watermelon"
print(fruits[1])


## List Methods
fruits.append("gauva") # Add an item to the end
print(fruits)


# Insert method
fruits.insert(2,"mango")
print(fruits)


# Removing the first occurence of elements
fruits.remove("banana") # Removing the first occurence of an item           
print(fruits)

# Remove and return the last elements
popped_fruits =fruits.pop()
print(popped_fruits)

print(fruits)


# To identify the index 
index = fruits.index("mango")
print(index)


# TO know the number of the occurence of elements
print(fruits.count('banana'))

# if we want to sort
fruits.sort() # sort the list in the ascending order
fruits

# To reverse which means in descending order
fruits.reverse()
print(fruits)

# Remove all elements of list

my_list = ["Cherry", "Apple"]

print(f"the initial list {my_list}")

#Add an item to the list
my_list.append("Pear")

print(f"adding a pear {my_list}")

#get the first Item
print(f"The first item in the list is {my_list[0]}")

#print the last item in the list
print(f"The last item in the list is {my_list[-1]}")

#remove to assignment from list
print(f"the current list {my_list}")
print(f"get the second item :{my_list.pop(1)}")
print(f"The new list {my_list}")

additional_list = ["pineapple", "coconut", "lemon"]

#add one list to another to the right
print(f"initial list {my_list}")
my_list.extend(additional_list)
print(f"The updated list {my_list}")

#add to the left
my_list[:0] = ['avocado', 'grapes']
print(f"added to the left {my_list}")

#insert one somewhere
my_list.insert(3,"strawberry")
print(f"Added straberry to position 4 : {my_list}")

#iterate over a list
for fruit in my_list:
    print(f"a fruit is : {fruit}")


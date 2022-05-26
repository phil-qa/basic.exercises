my_list = ["Cherry", "Apple"]

print(my_list)

#Add an item to the list
my_list.append("Pear")

print(my_list)

#get the first Item
print(my_list[0])

#get the last item in the list
print(my_list[-1])

#remove to assignment from list
print(f"the current list {my_list}")
print(f"get the second item :{my_list.pop(1)}")
print(f"The new list {my_list}")

additional_list = ["pineapple", "coconut", "lemon"]

#add one list to another
print(f"initial list {my_list}")
my_list.extend(additional_list)
print(f"The updated list {my_list}")

#iterate over a list
for fruit in my_list:
    print(f"a fruit is : {fruit}")

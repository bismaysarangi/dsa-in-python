my_list = [1, 2, 3, 4, 5, 6, 10, [12, 7]]
print(my_list)

#Updation of list
my_list[2] = 15
print(my_list)

my_list[7][1] = 4
print(my_list)

#Insertion

my_list.insert(0, 9)
print(my_list)

my_list.append(88)
print(my_list)

new_list = [9, 10, 7]
my_list.extend(new_list)
print(my_list)

#Slicing

print(my_list[0:2])
print(my_list[2:]) 

#Deletion
print(my_list.pop(3)) 
print(my_list)

del my_list[7:9]
print(my_list)

my_list.remove(10)
print(my_list)

#Opeartions

a = [2, 4, 6]
b = [1, 4, 6]

print(a + b)
print(a * 2)

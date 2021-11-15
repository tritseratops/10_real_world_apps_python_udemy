my_list = [1, [1,2], {2:3, 4:"5"}, "my string"]
obj1 = [1,2]
obj2 = {2:3, 4:"5"}
obj3 = "my string"
obj4 = 1
obj5 = 2
obj6 = "string"
obj7 = {2:3, 4:"6"}
obj8 = [1,3]


def add_object_to_list(my_list, my_object):
    if not my_object in my_list:
        my_list.append(my_object)
    return my_list

print(add_object_to_list(my_list, obj1))
print(add_object_to_list(my_list, obj2))
print(add_object_to_list(my_list, obj3))
print(add_object_to_list(my_list, obj4))
print(add_object_to_list(my_list, obj5))
print(add_object_to_list(my_list, obj6))
print(add_object_to_list(my_list, obj7))
print(add_object_to_list(my_list, obj8))

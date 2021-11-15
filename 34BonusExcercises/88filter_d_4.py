def filter_d_4(my_dict):
    new_dict = {}
    for key in my_dict:
        if my_dict[key]>4:
            new_dict[key]=my_dict[key]
    return new_dict

dict = {'a':5, 'b':3, 'c':10}
print(filter_d_4(dict))
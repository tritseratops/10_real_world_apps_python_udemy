def get_mid(my_list):
    if (len(my_list)%2!=1 or not my_list):
        return "Bad List"
    return my_list[int((len(my_list)-1)/2)]

print(get_mid([2,5]))
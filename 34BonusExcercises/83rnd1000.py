import random
def get_1000_rnd():
    my_list = []
    for i in range(1,1001,1):
        my_list.append(random.randint(1,10))
    return my_list

print(len(get_1000_rnd()))
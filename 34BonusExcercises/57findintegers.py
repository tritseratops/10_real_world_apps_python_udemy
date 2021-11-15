elements = [
    [1, 4, 6, 7],
    [4, 5, 6],
    [6, 7, 8],
    [],
    ["nodata", "nodata"],
    [1, 3]
   ]

def find_first_int_in_lists(my_list):
    for l1_list in my_list:
        for el in l1_list:
            if(type(el) == int):
                print(el)
                break

find_first_int_in_lists(elements)
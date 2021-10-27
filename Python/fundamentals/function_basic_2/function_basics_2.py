def countDownTwo(num):
    decrementList = []
    while num >= 0:
        decrementList.append(num)
        num -= 1
    return decrementList

def print_and_Return(lst):
    print(lst[0])
    return lst[1]

def first_plus_length(a_list):
    x = a_list[0]
    x = x + len(a_list)
    return x

def greater_than_second(a_list):
    if len(a_list) < 2:
        return False
    comp = a_list[1]
    b_list = []
    for x in a_list:
        if x > comp:
            b_list.append(x)
    print(len(b_list))
    return b_list

def this_length_that_value(size,value):
    that_value = []
    for x in range(0,size):
        that_value.append(value)
    return that_value
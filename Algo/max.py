def arr_max(arr):
    """takes the values of an array and returns the max"""
    keep = []
    trash = []
    for value in arr:
        if len(arr) == 1:
            break
        elif value >= arr[-1]:
            keep.append(value.pop())
        else:
            trash.append(value.pop())
    print(keep)
    print(trash)
    print(arr)

arr_max([1,4,3,9,10,-2,4])

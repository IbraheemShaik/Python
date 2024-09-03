def remove_element(arr, element):
    l=[]
    for i in arr:
        if i!=ele:
            l.append(i)
    return l

numbers = [150, 240, 310, 120, 550, 510]
ele = 310
updated_list = remove_element(numbers, ele)

print(updated_list)

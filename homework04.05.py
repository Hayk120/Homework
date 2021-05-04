

#1
'''def bubble_sort(lst=[7, 30, -8, 414, 9]):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = [lst[j + 1], lst[j]]
    return lst
print(bubble_sort([7, 30, -8, 414, 9]))'''


#2
'''def mix_lists(lst1=[], lst2=[]):
    if len(lst1) == len(lst2):
        for i in range(0, len(lst1), 1):
            print(lst1[i] + lst2[i], end=' ')
    else:
        print("The number of members on your list isn't equal")'''


#3
'''def each_item_to_its_square(lst=[]):
    new_lst = []
    for each in lst:
        each = each ** 2
        new_lst.append(each)
    return new_lst


print(each_item_to_its_square([65, 41, 8, 9, 0]))'''


#4
'''def sum_of_lists_members(lst=[1,2]):
    sum = 0
    for each in lst:
        sum += each
    return sum'''


#5
'''def remove_duplicates(lst=[]):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


print(remove_duplicates([ 111, 112 ]))'''


#6
'''def unique_values(lst=[]):
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    return new_lst


print(unique_values([4, 11, 9, 33]))'''

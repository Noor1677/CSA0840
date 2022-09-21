list1 = [1,2,3,4,5]
list2= [10,20,30,40,50,60]
#Using stack
sorted_list =[]
while list1 and list2:
    if list1[0] <  list2[0]:
        sorted_list.append(list1.pop(0))
    else:
        sorted_list.append(list2.pop(0))
sorted_list += list1
sorted_list += list2
print(sorted_list)

list1 = []
list2= [0]
newlist =[]
while list1 and list2:
    if list1 <  list2 :
        newlist.append(list1.pop(0))
    else:
        newlist.append(list2.pop(0))
newlist += list1
newlist += list2
print(newlist)


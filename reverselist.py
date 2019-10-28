list1= [1,2,3]
list2= [1,2,3,4]

def reverselist(mylist):
    for val in range(len(mylist)//2):
        temp = mylist[val]
        mylist[val] = mylist[len(mylist)-1-val]
        mylist[len(mylist)-1-val] = temp
    return mylist

print(reverselist(list1))

print(reverselist(list2))
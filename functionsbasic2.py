def countdown(number):
    newlist=[]
    for val in range(number,-1,-1):
        newlist.append(val)
    return newlist
# print(countdown(100))


def printreturn(a,b):
    print(a)
    return b
# c=printreturn(1,2)
# print(c)


def firstpluslength(arr):
    return arr[0] + len(arr)
mylist=[1,2,3]
# print(firstpluslength(mylist))


def valuesgreaterthansecond(arrlist):
    newarr=[]
    count=0
    for val in arrlist:
        if len(arrlist) < 2:
            return False
        elif val > arrlist[1]:
            newarr.append(val)
            count += 1
    print(count)
    return newarr

numz1=[5,3,5,5]
numz2=[1]
# print(valuesgreaterthansecond(numz1))
# print(valuesgreaterthansecond(numz2))

def thislengththatvalue(size, value):
    newlist=[]
    for val in range(size):
        newlist.append(value)
    return newlist
# print(thislengththatvalue(4,7))
# print(thislengththatvalue(6,9))


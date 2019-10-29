def biggiesize(numlist):
    for val in range(len(numlist)):
        if numlist[val] > 0:
            numlist[val]='big'
    return numlist
num1 = [1,1,0,2,0]
num2 = [1,1,2,3,4]
# print(biggiesize(num2))

def countpos(arr):
    count=0
    for val in range(len(arr)):
        if arr[val] > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr

newlist1 = [-1,1,1,1]
newlist2 = [1,6,-4,-2,-7,-2]
# print(countpos(newlist1))
# print(countpos(newlist2))

def sumtotal(arr):
    sum = 0 
    for val in arr:
        sum += val
    return sum
list1= [1,2,3,4]
list2= [6,3,-2]
# print(sumtotal(list1))
# print(sumtotal(list2))

def avg(arr):
    sum = 0
    for val in arr:
        sum += val
    avg = sum/len(arr)
    return avg
avgthis = [1,2,3,4,5]
# print(avg(avgthis))

def length(arr):
    return len(arr)
lengthlist=[]
# print(length(lengthlist))

def minimum(arr):
    min = arr[0]
    for val in range(len(arr)):
        if len(arr) == 0:
            return False
        elif arr[val] < min:
            min = arr[val]
    return min
# print(minimum([37,2,1,-9]))

def maximum(arr):
    max = arr[0]
    for val in range(len(arr)):
        if len(arr) == 0:
            return False
        elif arr[val] > max:
            max = arr[val]
    return max
# print(maximum([37,2,1,-9]))

def ultimate(arr):
    numbers = {'sumtotal':0, 'average':0, 'minimum':0, 'maximum':0, 'length':0}
    sumtotal = 0
    average = 0
    minimum = 0 
    maximum = 0

    length = len(arr)
    for val in range(len(arr)):
        if arr[val] > maximum:
            maximum = arr[val]
            sumtotal += arr[val]
        elif arr[val] < minimum:
            minimum = arr[val]
            sumtotal += arr[val]
    average = sumtotal/len(arr)
    numbers['sumtotal'] = sumtotal
    numbers['average'] = average
    numbers['minimum'] = minimum 
    numbers['maximum'] = maximum
    numbers['length'] = length
    return numbers
ultlist = [37,2,1,-9]
# print(ultimate(ultlist))


def reverselist(arr):
    for val in range(len(arr)//2):
        temp = arr[val]
        arr[val] = arr[len(arr)-1-val]
        arr[len(arr)-1-val] = temp
    return arr

arrlist= [37,2,1,-9]
print(reverselist(arrlist))




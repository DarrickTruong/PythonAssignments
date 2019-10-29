import random
def randInt(min=0, max=100):
    if min > max:
        print("Please choose a min that is less than max")
        return
    elif max < 0:
        print("Please choose a positive number for max")
        return 
    num = random.random() * (max - min) + min
    return round(num)
# print(randInt())                # should print a random integer between 0 to 100
# print(randInt(max=50))          #should print a random integer between 0 to 50
# print(randInt(min=50))              # should print a random integer between 50 to 100
print(randInt(min=500, max=50))    # should print a random integer between 50 and 500

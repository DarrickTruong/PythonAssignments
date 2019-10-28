
def basic():
    for val in range(151):
        print(val)

# basic()


def multiplesfive():
    for val in range(0,1001,5):
        print(val)

# multiplesfive()


def dojocount():
    for val in range(101):
        if val % 10 == 0:
            print('Coding Dojo')
        elif val % 5 == 0:
            print('Coding')
        else:
            print(val)

# dojocount()


def whoa():
    final_sum = 0
    for val in range(1,500000,2):
        final_sum += val
    print(final_sum)

# whoa() 


def countdownbyfours():
    for val in range(2018,-1,-4):
        print(val)

# countdownbyfours()



def flexiblecounter(lowNUM, highNUM, mult):
    for val in range(lowNUM, highNUM+1,1):
        if val % mult == 0:
            print(val)

flexiblecounter(3,100,3)
class Underscore:
    def map(self, iterable, callback):
        # your code here
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        # your code here
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
    def filter(self, iterable, callback):
        # your code
        new = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                new.append(iterable[i])
        return new
    def reject(self, iterable, callback):
        # your code
        new = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == False:
                new.append(iterable[i])
        return new
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print(evens)

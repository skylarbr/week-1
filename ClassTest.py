class CounterClass:

    count = 0

    def __init__(self, inputValue):
        self.count = inputValue

    def addToCounter(self, inputValue):
        self.count += inputValue

    def getCount(self):
        return self.count




myCounter = CounterClass(10)


myCounter.addToCounter(3)

myCounter.addToCounter(5)

print myCounter.getCount()

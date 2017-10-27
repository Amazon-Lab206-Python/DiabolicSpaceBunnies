class MathDojo (object):
    def __init__(self, value):
        self.value = value

    def add(self, *values):
        for val in values:
            if type(val) == list or type == tuple:
                for data in val:
                    self.value += data
            else:
                self.value += val
        return self

    def sub(self, *values):
        for val in values:
            if type(val) == list or type(val) == tuple:
                for data in val:
                    self.value -= data
            else:
                self.value -= val
            return self

    def displayInfo(self):
        print 'total is: {}'.format(self.value)


md = MathDojo(0)
md.add(2, 5).sub(2, 5).displayInfo()
md.add([1], 3, 4).add([3, 5, 7, 8], [2, 4, 3, 1.25]).sub(
    2, [2, 3], [1, 1, 2, 3]).displayInfo()

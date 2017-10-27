class Bike(object):
    '''def__init__(price, max_speed, miles) -- def not showing up as function
        bike.price = price
        bike.speed = speed
        bike.miles = miles'''

    def __init__(self, price, max_speed): '''why is self here?'''
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 '''why??? because when you buy a bike, its new, has 0 miles on it, can hard code.'''


###p1.talk("I'm the instructor").code().talk("what's up").code()

    def price(self):
        Print "I am ${} USD".format(self.price)
        return self


b1 = Bike(2.99, "RedBike")

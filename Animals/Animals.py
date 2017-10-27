class Animal(object):
    def __init__(self, name):
        self.name = name
        print "I am {}".format(self.name)
        self.health = 100  # why?

    def walk(self):
        self.health -= 1
        print "I am being walked"
        return self

    def run(self):
        self.health -= 5
        print "My owner is making me run"
        return self

    def display_health(self):
        print "Health {}".format(self.health)
        return self


    # what type of animal is this "Fluffy"? Just a generic "animal"?
a1 = Animal("Fluffy")
a1.walk().walk().walk().run().run().display_health()


class Rabbit (Animal):
    def __init__(self, name):
        # 'super(ChildClassName, self).parent_method()'. why does it show __init__(name) and NOT (self, name)?
        super(Rabbit, self).__init__(name)
        print "I am a {}.".format(Rabbit)
        self.health = 550

    def pet(self):
        self.health += 100
        print "Petting me makes me live longer by 100 points"
        return self


r1 = Rabbit("Cinnabun")
r1.walk().walk().walk().run().run().pet().display_health()


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health
        print "I am a scary dragon, hear me roar, I burn housies to the ground and love well done steak"


dr1 = Dragon("TootyFireMonsterSmokeSnout")
dr1.fly().fly().display_health()

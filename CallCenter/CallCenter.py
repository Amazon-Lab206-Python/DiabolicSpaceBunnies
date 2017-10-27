import datetime


class Call(object):
    id_counter = 0

    def __init__(self, name, number, reason):
        self.name = name
        self.number = number
        self.reason = reason
        self.time = datetime.datetime.now()
        Call.id_counter += 1
        self.id = Call.id_counter

    def display(self):
        print "Call name: {}".format(self.name)
        print "Call number: {}".format(self.number)
        print "Call reason: {}".format(self.reason)
        print "Call time: {}".format(self.time)
        print "Call id: {}".format(self.id)
        print "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"


class CallCenter(object):
    def __init__(self):
        self.call_list = []
        #self.queue_size = 0

    def add(self, call):
        self.call_list.append(call)
        #self.queue_size += 1
        return self

    def remove(self):
        if (len(self.call_list)):
            self.call_list.pop(0)
            #self.queue_size -= 1
        return self

    def info(self):
        for call in self.call_list:
            print call.name, call.number
        # print "{} many people waiting in line".format(self.queue_size)
        print "{} people waiting in line".format(len(self.call_list))

    def blockBasedOnNumber(self, number):
        for index, call in enumerate(self.call_list):
            if (call.number == number):
                self.call_list.pop(index)

    def sortByTime(self):
        self.call_list.sort()  # didn't work

    def display(self):
        for call in self.call_list:
            call.display()


c1 = Call("Todd", "555-1212", "I need help troubleshooting")
c2 = Call("Jayme", "555-1215", "I need help coding things")
c3 = Call("Brad", "555-1219", "I need help growing hair")
c4 = Call("Noah", "555-1210", "I need help not to look like a doppelganger")

cc1 = CallCenter()

cc1.add(c1)
cc1.add(c2)
cc1.add(c3)
cc1.add(c4)
cc1.info()

# cc1.remove()

# cc1.call_list[0].display()
# cc1.call_list[1].display()

cc1.blockBasedOnNumber("555-1215")
# for call in cc1.call_list:
# call.display()
cc1.display()

# print cc1.call_list

# print c1.id
# print c4.id

print "Hello World!"
x = "Hello Python"
print x
y = 42
print y

name = "Zen"
print "My name is", name

name = "Zen"
print "May name is" + name

name = 5
print 7 + name

name = 5
print 7, 5

hw = "hello %s" % 'world'
print hw


first_name = "cadence"
last_name = "bunneh ^_^"
print "My name is {}^_^ {}".format(first_name, last_name)
print last_name.upper()
print first_name.upper()
print last_name.endswith("eh")
print last_name.endswith("h")
print last_name.count("n")
print last_name.find("e")
print last_name.isalnum()
print last_name.join(last_name)
print last_name.join("let")
print last_name.split("u")
x = [1, 2, 3, 4]
x.append(99)
print x
print len(first_name)
x.extend(last_name)
y = [5, 6, 7, 8]
print x.extend(y)
print x
print y.pop(2)
print y
print y.index(6)
z = [0, 4, 5, 6, 8]
print y.extend(z)
print y


def say_hi(name):
    print "Hi," + name


say_hi('Bunny')


def multiply(arr, num):
    for x in arr:
        x *= num
    return arr


a = [2, 4, 10, 16]
b = multiply(a, 5)
print b

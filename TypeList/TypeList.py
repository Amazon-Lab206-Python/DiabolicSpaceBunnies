# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# input: always a list. string : concat. number= sum
# print string, number, type
# what does it contain

"""#type==
if type == string
print "string
print concat

if type == number
print number
print sum

If both == &&,
then "mixed'
print number concat
print sum

"""
ml = ["grumbly", "pink", 14, 429, "rabbit"]
il = [2, 3, 1, 7]
sl = ['magical', 'unicorns']


testlist = sum = 0
phrase = ""
listtype = None

for val in ml:
    if(type(val)is int):  # checks data type of  value in the list
        sum += val
        if(listtype is "string"):
            listtype = "mixed"
        elif(listtype is None):
            listtype = "integer"
    else:
        phrase += val
        if (listtype is "integer"):
            listtype = "mixed"

        elif (listtype is None):
            listtype = "string"

print "The list you entered is of {} type".format(listtype)

if (listtype is "integer" or listtype is "mixed"):
    print "Sum: {}".format(sum)
if (listtype is "string" or listtype is "mixed"):
    print "String: {}".format(phrase)

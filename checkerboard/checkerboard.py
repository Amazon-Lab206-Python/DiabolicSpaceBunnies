'''*=1 space=-1
each line has to equal 0 and alternate

for *, make sure next is space
next line after 8 characters.
for (i=0, i <= 8, i +=)
    if previous char = *
        print " "
    else print *'''


def checkerboard():

    for i in range(0, 8):
        if i % 2 == 0:
            print "* " * 4
        else:
            print " *" * 4


checkerboard()

'''Score: 60 - 69
Grade - D
Score: 70 - 79
Grade - C
Score: 80 - 89
Grade - B
Score: 90 - 100
Grade - A
'''
import random
x = random.random() * 100


def scoregrader(60, 100):
    for y in range(60 - 69):
        print "Score is {} and you have a D. Try harder"
    for y in range(70 - 79):
        print "score is {} and you have a C. Yay, you're average"
    for y in range(80 - 89):
        print "score is {} and you have a B. Better than average"
    for y in range(90 - 100):
        print "score is {} and you have an A, excellent!"

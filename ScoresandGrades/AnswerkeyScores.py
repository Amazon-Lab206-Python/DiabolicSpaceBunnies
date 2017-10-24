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


def grade(reps):
    print "Scores and Grades"
    for y in range(0, reps):
        score = random.randint(60, 101)
        if score in range(60, 70):
            print "Score is {} and you have a D. Try harder"
        elif score in range(70, 80):
            print "score is {} and you have a C. Yay, you're average"
        elif score in range(80, 90):
            print "score is {} and you have a B. Better than average"
        elif score in range(90, 101):
            print "score is {} and you have an A, excellent!"
        else:
            print "LOL YOU FAILED!"
    print "Thats all folks!"


grade(7)

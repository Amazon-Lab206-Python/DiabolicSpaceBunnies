def drawStars(numberOfStarsToBePrintedList):
    for numberOfStarsToBePrinted in numberOfStarsToBePrintedList:
        if type(numberOfStarsToBePrinted) is int:
            print "*" * numberOfStarsToBePrinted
        elif type(numberOfStarsToBePrinted) is str:
            firstLetter = numberOfStarsToBePrinted[0].lower()

            print firstLetter * len(numberOfStarsToBePrinted)
        else:
            print str(type(numberOfStarsToBePrinted))


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
drawStars(x)
# listOfNumbers = [4, 6, 10]
# drawStars(listOfNumbers)

weekend = {"Sun": "Sunday", "Sat": "Saturday"}  # literal notation


def printPerson(personDictionary):
    print "my name is " + personDictionary["name"]
    print "I am " + str(personDictionary["age"]) + "years old"


Cadence = {"name": "Cadence"}
Cadence["age"] = 2
Gordon = {}
Gordon["name"] = "Gordon"
Gordon["age"] = 32
Gordon["countryOfBirth"] = "USA"
Gordon["favoriteLanguage"] = "English"
printPerson(Gordon)
printPerson(Cadence)

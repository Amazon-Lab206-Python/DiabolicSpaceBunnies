name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider",
                   "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(name, favorite_animal):
    new_dict = zip(name, favorite_animal)

    return dict(new_dict)


print make_dict(name, favorite_animal)

class Product(object):
    def __init__(self, price, itemName, weight, brand):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        # if for sale, "for sale" this is the default, if not for sale, "sold". boolean
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        return self.price + (self.price * tax)

    def return_product(self, reason):
        if (reason == "defective"):
            self.status = "Defective"
            self.price = 0
        elif (reason == "returned in boxie"):
            self.status = "For Sale"
        elif(reason == "opened"):
            self.status = "used"
            self.price = self.price - (self.price * 0.2)
        return self

    def display_all(self):
        print "Price: " + str(self.price) + " USD"
        print "item name: " + str(self.itemName)
        print "weight: " + str(self.weight) + " oz"
        print 'brand: ' + str(self.brand)
        print "Status: " "{}".format(self.status)
        print "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
        return self


item1 = Product(50.50, "gold plated pile of cards", 2, "squigly brand")
item2 = Product(500, "jewelry tree", 3, "blingbling brand")
item2.return_product("defective").display_all()
item1.display_all()

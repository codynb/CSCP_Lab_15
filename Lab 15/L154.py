#The authors are Maggie Dunn and Cody Brown L154

class Fabric:
    """the attributes are countryOfOrigin and color"""

    def __init__(self, countryOfOrigin, color):
        self.countryOfOrigin = countryOfOrigin
        self.color = color

    def __str__(self):
        return self.countryOfOrigin + "("+ str(self.color)+")"

Fab1 = Fabric("Italy", "red")

print(Fab1)

#this prints:
    # Italy(red)

#Multiple inheritance
class Watch:
    def feature(self):
        print("Show time")

class Bracelet_Watch:
    def character(self):
        print("fashion")

class Smart_Watch(Watch,Bracelet_Watch):
    def property(self):
        print("show's step count")
        
titan=Watch()
titan.feature()

print()

bracelet=Bracelet_Watch()
bracelet.character()

print()

fastrack=Smart_Watch()
fastrack.feature()
fastrack.character()
fastrack.property()
#Inheritance and types may or may not have same properties and behaviour, but MRO must

#Single inheritance
class Watch:
    def feature(self):
        print("Show time")

class Smart_Watch(Watch):
    def property(self):
        print("show's step count")
        
titan=Watch()
titan.feature()

print()

fastrack=Smart_Watch()
fastrack.feature()
fastrack.property()
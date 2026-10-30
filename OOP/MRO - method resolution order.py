#MRO (Method resolution order)
'''class Watch:
    def feature(self):
        print("Show time")

class Bracelet_Watch:
    def character(self):
        print("fashion")
        
    def feature(self):
        print("party wear")

class Smart_Watch(Watch,Bracelet_Watch):
    def property(self):
        print("show's step count")
    
    def feature(self):
        print("small mobile")
        
titan=Smart_Watch()
titan.feature()

print(--------------------------------------------------------------------------)'''

'''class Watch:
    def feature(self):
        print("Show time")

class Bracelet_Watch:
    def character(self):
        print("fashion")
        
    def feature(self):
        print("party wear")

class Smart_Watch(Watch,Bracelet_Watch):
    def property(self):
        print("show's step count")
        
titan=Smart_Watch()
titan.feature()

print(--------------------------------------------------------------------------)'''

'''class Watch:
    pass

class Bracelet_Watch:
    def character(self):
        print("fashion")
        
    def feature(self):
        print("party wear")

class Smart_Watch(Watch,Bracelet_Watch):
    def property(self):
        print("show's step count")
        
titan=Smart_Watch()
titan.feature()

print(-----------------------------------------------------------------------)'''

class Watch:
    def feature(self):
        print("Show time")

class Bracelet_Watch:
    def character(self):
        print("fashion")
        
    def feature(self):
        print("party wear")

class Smart_Watch(Watch,Bracelet_Watch):
    def property(self):
        print("show's step count")
        
titan=Smart_Watch()
titan.feature()
bracelet=Bracelet_Watch()
Bracelet_Watch.feature(bracelet)
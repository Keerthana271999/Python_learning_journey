#Duck typing - you need to a feature of duck
class Watch:
    def feature(self):
        print("show time")
class Smart_Watch:
    def feature(self):
        print("step count")
class Mobile:
    def property(self):
        print("big screen")
class Machine:
    def use_case(self,mac:Watch):
        mac.feature()
        print("reduce human effort")
w=Watch()

sw=Smart_Watch()

m=Mobile()

ma=Machine()
ma.use_case(w)
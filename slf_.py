class Chaicup:
      size = 150 #ml

      def describe(self): # SELF can be refer to any func/val 
          return f"A {self.size} ml chai cup"

cup = Chaicup()
print(cup.describe()) # reference taken frm object i.e cup
print(Chaicup.describe(cup)) # "cup" is writtn as chaicup is modify ,rslt'll be same

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two)) # RFRNC taken frm class i.e cup-two

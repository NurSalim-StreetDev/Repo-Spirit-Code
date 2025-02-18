class Hero:

    def __init__(self, InputName, InputATK, InputHP, InputDEF):
        self.name = InputName
        self.ATK  = InputATK
        self.HP   = InputHP
        self.DEF  = InputDEF
        # print (self.name)
        # print (self.ATK)
        # print (self.HP)
        # print (self.DEF)

hero1 = Hero('Balmond', 10,100,4)
hero2 = Hero('Tigreal', 5, 120, 7)
hero3 = Hero('Mage', 20, 75, 0)

print (hero1.__dict__)
print (hero2.__dict__)
print (hero3.__dict__)
class Hero:
    pass


hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Balmond'
hero1.ATK  = 10
hero1.HP   = 100
hero1.DEF  = 4

hero2.name = 'Granger'
hero2.ATK  = 15
hero2.HP   = 90
hero2.DEF  = 1

hero3.name = 'Tigreal'
hero3.ATK  = 5
hero3.HP   = 120
hero3.DEF  = 7

print (hero1)
print (hero1.__dict__)
print (hero1.name)

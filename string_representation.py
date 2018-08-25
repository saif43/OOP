class Fighter:
    
    def __init__(self,name,health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self,attacked_to):
        attacked_to.health -= self.damage
        print("{} attacked {}".format(self.name,attacked_to.name))


    def __str__(self):
        return "{} health: {}".format(self.name,self.health)

jason = Fighter(input("Jason name: "),int(input("Jason health: ")),int(input("Jason damage: ")))
bruce = Fighter(input("Bruce name: "),int(input("Bruce health: ")),int(input("Bruce damage: ")))

print(jason)
print(bruce)

jason.attack(bruce)

print(jason)
print(bruce)



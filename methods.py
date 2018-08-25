class Fighter:

    def __init__(self,name,health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self,attacked_to):
        attacked_to.health -= self.damage

    def status(self):
        print(self.name)
        print("Damage: ",self.damage)
        print("Health: ",self.health)

jason = Fighter("RedHood",1500,50)
bruce = Fighter("Batman",1800,80)

jason.status()
bruce.status()

print("\nJason attacked Bruce\n")
jason.attack(bruce)

jason.status()
bruce.status()

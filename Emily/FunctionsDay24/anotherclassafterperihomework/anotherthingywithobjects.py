class GameObject:
    def __init__(self, name):
        self.name = name

    def pickUp(self, player):
        pass
        #put some random things here
        #but the listing that's not actually a lsiting doesn't say
        
class Coin(GameObject):
    def __init__(self, value):
        GameObject.__init__(self, 'coin')
        self.value = value

    def spend(self, buyer, seller):
        pass
        #no idea what to put here
        #wait, i'm reading the stuff
        #so i kinda know-...ish

game1 = GameObject("mytest")
print(game1.name)
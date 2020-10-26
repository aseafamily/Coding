class GameObject:
    def __init__(self, name):
        self.name = name

    def pickUp(self, player):
        pass
        # put code here to add the object
        # to the player's collection
class Coin(GameObject):
    def __init__(self, value):
        GameObject.__init__(self, "coin")
        self.value = value

    def spend(self, buyer, seller):
        pass
        #Put code here to remove the coin
        #form the buyer's money
        #add it to the seller money

#game1 = GameObject()
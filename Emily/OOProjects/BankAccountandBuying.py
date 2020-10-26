class mall:
    def __init__(self, name, budget):
        self.budget = budget
        self.name = name

    def __str__(self):
        msg = 'You have ' + budget + ' left.'  
    def burgerrestaurant(self, items, spent):
        self.budget  = self.budget - spent
    
    def clothesstore(self, items, spent):
        self.budget = self.budget - spent
    
    def toystore(self, items, spent):
        self.budget = self.budget - spent
    
    def petstore(self, items, spent):
        self.budget = self.budget - spent
    
    def flowershop(self, items, spent):
        self.budget = self.budget - spent
    
    def bookstore(self, items, spent):
       self.budget = self.budget - spent
    
    def coffeeshop(self, items, spent):
        self.budget = self.budget - spent
    
    def seafoodshop(self, items, spent):
        self.budget = self.budget - spent
    
    def artstore(self, items, spent):
        self.budget = self.budget - spent

thename = input('Welcome to Everything Mall! What is your name?')
thebudget = int(input('Alright. What is your budget?'))
Everythingmall = mall(thename, thebudget)

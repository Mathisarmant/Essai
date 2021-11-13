class Article:
    
    def __init__(self, designation, price):
        self.designation = designation
        self.price = price

    def getDesignation(self):
        return self.designation
    
    def getPrice(self):
        return self.price
   
    def setPrice(self, NewPrice):
        self.price = NewPrice
        
    def __repr__(self):
        return ' {} / {} '.format(self.designation, self.price)
    




cc = Article("Coca-Cola", 3.95)

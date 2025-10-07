class Order:
    def __init__(self, item, price):
        self.item=item
        self.price=price
    def __gt__(self, ord2): # greater than dunder
        return self.price > ord2.price # retrun true or false
ord1=Order("tea", 40)
ord2=Order("bag", 50)
print(ord1>ord2) # false

# class test():
#     def __init__(self):
#        self.x=6


# class car(test):
#     def __init__(self):
#         super().__init__()
        
#     def test(self):
#         self.y=self.x*2
#         print(self.y)
# cara=car()
# cara.test()
# """"the Car class. Sell a few of the cars. Call the print function on all of them.
"""""
Continue on your code from the previous exercise with a new class named Customer.
Give it one field (name) and properly implement it.
Also create a method print that returns all fields in a for humans readable way.
Modify the Car class with a field sold_to, set this field to a object of Customer within the sell method (which now needs a parameter with a Customer object).
Edit the print method of the Car to also print the information about the Customer if the car has been sold.
Adjust other code were needed to get everything working properly.

The car dealer wants to extend his business by selling motorcycles as well.
Write all code to properly introduce this into the existing application.
"""


class Car:
        def __init__(self,brand,model,color,price):
            self.brand=brand
            self.model=model
            self.color=color
            self.price=price
            self.sold=False
        def print(self):
           print("brand",self.brand)
           print("model",self.model) 
           print("color",self.color)
           print("price",self.price)
        def sell(self,abc):
            self.sold=True
            self.costumer=abc
        def sold_to(self):
            print("brand",self.brand)
            print("model",self.model) 
            print("color",self.color)
            print("price",self.price)
            print(self.costumer.name)

class Customer(Car):
    def __init__(self,Customer):
           self.name=Customer             
if __name__ =="__main__":  
    
    car2=Car('ape','ape','ape',123)
    Customer1=Customer("tom")
    car2.sell(Customer1)
    car2.sold_to()
    car2.print()
    


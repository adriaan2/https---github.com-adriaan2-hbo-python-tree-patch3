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

# class  car:
    
#     def __init__(self,brand,model,color,price):
#             self.brand=brand
#             self.model=model
#             self.color=color
#             self.price=price
        
# if __name__=="__main__":
#     test=car.__init__('czxvcx','xvxcv','gd','123')
"""We're going to create a small application for a car dealer.

The problem is split up into three steps to help you set up a proper structure for the application.

Create a class named Car.
Create four fields (brand, model, color, price) and implement these using the init function.
Also create a fifth field called sold. The default value for sold is False.
Create a method called sell that changes the value of sold to True.
Create another method called print that prints all fields in a for humans readable way.
Create 4 objects of the Car class. Sell a few of the cars. Call the print function on all of them.

Continue on your code from the previous exercise with a new class named Customer.
Give it one field (name) and properly implement it.
Also create a method print that returns all fields in a for humans readable way.
Modify the Car class with a field sold_to, set this field to a object of Customer within the sell method (which now needs a parameter with a Customer object).
Edit the print method of the Car to also print the information about the customer if the car has been sold.
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
        def sell(self):
            self.sold=True
            print(self.sold)
           
            
class customer(Car):
    def __init__(self):
          pass                  
                
             
if __name__ =="__main__":  
    testInstance = Car('bmw','x5','red',200)
    testcar=Car('Audi','fag','blue',5)
    car2=Car('ape','ape','ape',123)
    car2.sell()


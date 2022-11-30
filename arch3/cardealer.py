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

# class  cardealer:
    
#     def __init__(self,brand,model,color,price):
#             self.brand=brand
#             self.model=model
#             self.color=color
#             self.price=price
        
# if __name__=="__main__":
#     test=cardealer.__init__('czxvcx','xvxcv','gd','123')



class TestClass:
        def __init__(self,brand,model,color,price):
            self.b=brand
            self.m=model
            self.c=color
            print(price)
        def cardealer(self):
             pass
testInstance = TestClass('bmw','x5','red',200)

testInstance.cardealer()


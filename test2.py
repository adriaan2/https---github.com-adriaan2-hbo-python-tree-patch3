x=3
loop=0
charset={"!",  "@" ,"*" ,"?"} 
charcounter=0
while loop<x:
    password=input("password")
    xt=len(password)
    passet=set(password)
    for i in passet:
      if i.isupper():
        print("test")
      if i.isnumeric():
        print("num")
      if xt>7 and xt<21:
        print("size")
        i+=len(passet)
        
    


            

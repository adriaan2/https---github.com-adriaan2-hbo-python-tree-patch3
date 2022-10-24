

i =False
def checkpassword():
    while i==False:
        password=input("getpassword")
        if len(password)>7 and len(password)<21:
            print("test")
                
        else :
            print("invalid password")
if __name__=="__main__":
    checkpassword()
class converter():
    def __init__(self,number,measure) -> None:
        self.number=number
        self.measure=measure
        print(measure)
    def test(self):
        print(self.measure)



if __name__=="__name__":
    number=int(input("a number please"))
    measure=input("convert to what ")
    convert=converter(number,measure)
    convert.test()

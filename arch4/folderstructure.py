""""CarParkingMachine class with the following attributes:

capacity (int, default 10) - how many cars can be checked-in at the same time.
hourly_rate (float, default 2.50) - used to calculate the parking fee.
parked_cars (dict => key: license_plate, value: ParkedCar object) - keeps track of the cars present in the car parking
This class has the following methods:

init (construtor) that receives the capacity, hourly_rate and sets the parked_cars dict as empty.
check_in that receives the license_plate (str), the time (datetime) that the car is parked. If the maximum capacity is reached it should return False and not check-in the car.
check-out that receives the license_plate (str) and returns the owed parking fee total (by calling the get_parking_fee method).
get_parking_fee that receives the license_plate (str) and calculates/returns the parking fee (hourly_rate * whole parking hours rounded-up, with max of 24 hours).
ParkedCar class storing information of a parked car with the following attributes:

license_plate (str) - license plate of the car
check-in (datetime) - datetime object of the time checked-in
This class has the following methods:

init (construtor) that receives the license_plate and check-in
Additional research is required on how to handle datetime objects to calculate the difference between the check-in and check-out time and how to round-up in hours. Hint: import the datetime module (datetime and timedelta objects)

To test your class, use the provided unit test file and complete the test functions with your own code.

For the main of this program use a CarparkingMachine with default values (capacity: 10, rate: 2.50) build menu structure as following the input can be case-insensitive (so E and e are valid inputs)


[I] Check-in car by license plate
output: License registered (only if checked-in)
or: Capacity reached!
[O] Check-out car by license plate
output: Parking fee: {parking_fee} (2 decimals!) EUR (if license is found)
or: License {license_plate} not found!
[Q] Quit program

"""
from datetime import datetime



class ParkedCar:
    def __init__(self,license_plate,checkintime):
        self.license_plate=license_plate   
        self.checkintime=checkintime
        

class CarParkingMachine:
        def __init__(self, capacity=10,hourly_rate=2.50) -> None:
            self.capacity=capacity
            self.license_plate=license
            
            self.parked_cars={}
            self.hourly_rate=round(hourly_rate,2)
        def check_in(self,licenses,checkintime=datetime.now()):
            self.parked_cars[licenses]=ParkedCar(licenses,checkintime)
            return False
               
        def check_out(self, licenses ):
                testing=True
                self.licenses=licenses
                
                for i in self.parked_cars:
                    
                    if i==licenses:
                        self.get_parking_fee(self.licenses)
                        testing==False
                if testing==False:
                    self.parked_cars.pop(licenses)

 
        def get_parking_fee(self,licenses,checkouttime=datetime.now()):
                self.licenses=licenses
                self.checkoutime=checkouttime
                checkintime=self.parked_cars[licenses].checkintime
                timestayed=checkintime-checkouttime
                timeparked=timestayed.seconds//3600-22
                print(timeparked)
                if timeparked>24:
                      timeparked=24
                parkingfee=(self.hourly_rate*timeparked)
                print("parking fee",parkingfee)




                
                
                


                        
                    
       

                
def main():
    test=CarParkingMachine()
    x=True   
    while x:
        print("[I] Check-in car by license plate\n[O]  Check-out car by license plate")
        

      
        yourchoice=input("[Q]  quit program  ").lower()
        if yourchoice=="i":
            licenseplate=input("license")
            
             
            if len(test.parked_cars)>=test.capacity:
                print("capacity reached")

            
            else:
                test.check_in(licenseplate)
                print("license registered")

             
        elif yourchoice=="o":
             license=input("licence plate")
             test.check_out(license)
             
        else :
            x=False

    
         

        
        
if __name__ == "__main__":
    main()


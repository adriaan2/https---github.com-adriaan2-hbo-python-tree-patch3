
from datetime import datetime



class ParkedCar:

    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingMachine:

    def __init__(self, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    def check_in(self, license_plate, check_in=datetime.now()):
        if len(self.parked_cars) >= self.capacity:

            return False
        else:
            self.parked_cars[license_plate] = ParkedCar(
                license_plate, check_in)

            return True

    def check_out(self, license_plate): 
        parking_fee = self.get_parking_fee(license_plate)
        del self.parked_cars[license_plate]
        if parking_fee == 2.5:
            print(f"Parking Fee: {parking_fee}0 EUR")
        else: 
            return parking_fee

    def get_parking_fee(self, license_plate):
        now = datetime.now()
        checkin = self.parked_cars[license_plate].check_in
        difference = now - checkin
        diff_hour = difference.total_seconds() / 60 / 60
        fee = self.hourly_rate * int(diff_hour+1)
        max_fee = self.hourly_rate * 24
        if fee >= max_fee:
            return max_fee
        else:
            return fee


def main():
    test = CarParkingMachine()
    while True:
        print("""
        [I] Check-in Car By License Plate
        [O] Check-out Car By License Plate
        [Q] Quit Program 
        """)
        u_input = input(": ")
        if u_input == "I" or u_input == "i":
            output = test.check_in(license_plate=input())
            if not output:
                print("Capacity Reached")
            else:
                print("License Registered")
            continue    

        if u_input == "O" or u_input == "o":
            test.check_out(license_plate=input())
            continue

        if u_input == "Q" or u_input == "q":
            exit()


if __name__ == "__main__":
    main()

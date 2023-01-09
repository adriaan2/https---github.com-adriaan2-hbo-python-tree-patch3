from datetime import datetime


class ParkedCar:

    def __init__(self, license, check_in):
        self.license = license
        self.check_in = check_in

    def timeslot(self):
        return self.check_in


class CarParkingMachine:

    def __init__(self, id=str, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.logger = CarParkingLogger(id)

    def check_in(self, license, check_in=datetime.now()):
        if len(self.parked_cars) >= self.capacity:

            return False
        else:
            self.parked_cars[license] = ParkedCar(
                license, check_in)
            self.logger.incheck(check_in, license)
            return True

    def check_out(self, license):
        fee = self.get_parking_fee(license)
        self.logger.outcheck(datetime.now(), license, fee)
        del self.parked_cars[license]
        if fee == 2.5:
            print(f"Parking fee: {fee}0 EUR")
        else:
            return fee

    def get_parking_fee(self, license):
        now = datetime.now()
        checkin = self.parked_cars[license].check_in
        difference = now - checkin
        diff_hour = difference.total_seconds() / 60 / 60
        fee = self.hourly_rate * int(diff_hour+1)
        max_fee = self.hourly_rate * 24
        if fee >= max_fee:
            return max_fee
        else:
            return fee


class CarParkingLogger():

    def __init__(self, id):
        self.id = id

    def get_total_car_fee():
        ...

    def incheck(self, check_in, license):
        with open('carparklog.txt', 'a') as f:
            check_in = check_in.strftime("%d-%m-%Y %H:%M:%S")
            f.write(
                f"{check_in};cpm_name={str(self.id)};license={license};action=check-in")

    def outcheck(self, check_out, license, fee):
        with open('carparklog.txt', 'a') as f:
            f.write(
                f"{check_out};cpm_name={str(self.id)};license={license};action=check-out;parking_fee={fee}")

    def get_machine_fee_by_day():
        ...


def main():
    test = CarParkingMachine(id)
    while True:
        print("""
        [I] Check-in car by license plate
        [O] Check-out car by license plate
        [Q] Quit program 
        """)
        up = input(": ")
        if up == "I" or up == "i":
            output = test.check_in(license=input(": "))
            if not output:
                print("Capacity reached")
            else:
                print("License registered")
            continue

        if up == "O" or up == "o":
            test.check_out(license=input(": "))
            continue

        if up == "Q" or up == "q":
            exit()


if __name__ == "__main__":
    main()

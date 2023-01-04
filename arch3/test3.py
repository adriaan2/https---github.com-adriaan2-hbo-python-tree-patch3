from datetime import datetime
import json
import os
import sys
# write json


def save(data: list[dict], filename: str):
    with open(os.path.join(sys.path[0], filename), 'w') as file:
        json.dump(data, file, indent=4)


# read json
def load(filename: str) -> list[dict]:
    with open(os.path.join(sys.path[0], filename)) as file:
        return json.load(file)


class CarParkingMachine:

    def __init__(self, capacity=10, hourly_rate=2.50, parked_cars={}, id="North"):

        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    # def check_in(self, carObj):
    def check_in(self, license_plate: str, check_in: datetime = datetime.now()):
        if self.capacity <= len(self.parked_cars):
            return False

        self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
        name = f'{self.id}_state.json'
        if not os.path.exists(os.path.join(sys.path[0], name)):
            data = []

        else:
            data = load(name)
        # example

        format = "%d-%m-%Y %H:%M:%S"
        data.append({"license_plate": license_plate,
                    "check_in": check_in.strftime(format)})
        save(data, name)
        # print(self.parked_cars)
        CarParkingLogger.log_check_in(self.id, license_plate)

        return True

    def check_out(self, license_plate: str):
        if license_plate not in self.parked_cars:
            return False

        # laad hier
        #car = self.parked_cars[license_plate]
        fee = self.get_parking_fee(license_plate)
        name = f'{self.id}_state.json'
        if not os.path.exists(os.path.join(sys.path[0], name)):
            data = []
        else:
            data = load(name)
        for entry in data:
            if entry['license_plate'] != license_plate:
                continue
            data.remove(entry)
            break
        save(data, name)
        self.parked_cars.pop(license_plate)
        #del car
        # print(fee)
        CarParkingLogger.log_check_out(self.id, license_plate, fee)
        return fee

    def get_parking_fee(self, license_plate):
        from math import ceil
        car = self.parked_cars[license_plate]
        delta = datetime.now() - car.check_in
        hours = ceil(delta.total_seconds() / 3600)
        return self.hourly_rate * (hours if hours <= 24 else 24)


class ParkedCar:

    def __init__(self, license_plate: str, check_in: datetime = datetime.now().strftime("%H")):

        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingLogger:

    def log_check_in(cpm_name, license_plate):
        log_line = f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')};cpm_name={cpm_name};license_plate={license_plate};action=check-in"
        with open(os.path.join(sys.path[0], "carparklog.txt"), "a") as log_file:
            log_file.write(log_line + "\n")

    def log_check_out(cpm_name, license_plate, parking_fee):
        log_line = f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')};cpm_name={cpm_name};license_plate={license_plate};action=check-out;parking_fee={parking_fee:.2f}"
        with open(os.path.join(sys.path[0], "carparklog.txt"), "a") as log_file:
            log_file.write(log_line + "\n")

    @classmethod
    def get_machine_fee_by_day(cls, cpm_name: str, search_date: str) -> float:
        total_fee = 0
        with open("carparklog.txt", "r") as log_file:
            for line in log_file:
                fields = line.strip().split(";")
                if fields[1] == f"cpm_name={cpm_name}" and fields[0].startswith(search_date):
                    if fields[3] == "check-out":
                        total_fee += float


def main():

    parking_object = CarParkingMachine()

    stop = False

    while not stop:
        print("""[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program""")
        answer = input("What do you want to do? ").upper()
        if answer == "I":
            plate = input("Fill in your license plate: ")
            if not parking_object.check_in(plate):
                print("Capacity reached!")
                continue
            print("License registered")
        elif answer == "O":
            licenseDel = input("Which Car needs to go? ")

            result = parking_object.check_out(licenseDel)
            if not result:
                print("error: license has not been checked in")
                continue
            print(f"Parking fee: {result:.2f} EUR")
        elif answer == "Q":
            print("quiting program...")
            stop = True


if __name__ == "__main__":
    main()

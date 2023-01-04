
    from datetime import datetime


class ParkedCar():
    def __init__(self,license):
        self.License_plate = license
        self.check_in = ""
    


class CarParkingMachine():
    def __init__(self, name):
        self.Capacity = 10
        self.hourly_rate = 2.50
        self.parked_cars = dict()
        self.Name = name
    
    def check_in(self, car):
        if(len(self.parked_cars) < self.Capacity):
            self.Capacity += 1
            license = car.License_plate
            self.parked_cars[license] = car
            car.check_in = str(datetime.now()).replace("-", "/")
            logger.writeToLog(self, car, "check-in", 0)
            return True
        return False
    
    def check_out(self,car):
        payment = self.get_parking_fee(car)
        logger.writeToLog(self, car, "check-out", payment)

        del self.parked_cars[car.License_plate]
        print("The total fee is " + str(payment))
    
    def get_parking_fee(self,car):
        date_format_str = "%Y/%m/%d %H:%M:%S.%f"
        check_in_time = datetime.strptime(str(car.check_in), date_format_str)
        check_out_time = datetime.strptime(str(datetime.now()).replace("-", "/"), date_format_str)
        diff = check_out_time - check_in_time
        diff_in_hours = diff.total_seconds() / 3600
        return round((diff_in_hours + 1) * self.hourly_rate, 2)


class carParkingLogger():
    def writeToLog(self, Machine, car, action, fee):
        if(fee == 0):
            writing_string = car.check_in + ";cpm name = " + Machine.Name + ";license_plate = " + car.License_plate + ";action = " + action + "\n"
        else:
            writing_string = car.check_in + ";cpm name = " + Machine.Name + ";license_plate = " + car.License_plate + ";action = " + action + ";fee = " + str(fee) + "\n"
        with open("carparklog.txt", "a") as f:
            f.write(writing_string)
    
    def get_machine_fee_by_day(self, Machine, date):
        with open("carparklog.txt", "r") as f:
            data = f.read()
        data = data.splitlines()
        total = 0.0
        for x in data:
            s = x.split(";")
            if(Machine in x and date in x and "action = check-out" in x):
                s = s[4].split(" ")
                total += float(s[2])
        print(total)

    def get_total_car_fee(self,license):
        with open("carparklog.txt", "r") as f:
            data = f.read()
        data = data.splitlines()
        total = 0.0
        for x in data:
            s = x.split(";")
            if(license in x and "action = check-out" in x):
                s = s[4].split(" ")
                total += float(s[2])
        print(total)

        
        

logger = carParkingLogger()
logger.get_machine_fee_by_day("Arnold", str(datetime.date(datetime.now())).replace("-", "/"))
logger.get_total_car_fee("abcdef")
# car1 = ParkedCar("abcd")
# car2 = ParkedCar("abcde")
# car3 = ParkedCar("abcdef")
# car4 = ParkedCar("abcdefg")

# machine1 = CarParkingMachine("Arnold")
# machine2 = CarParkingMachine("Beta")
# machine1.check_in(car1)
# machine1.check_in(car2)
# machine2.check_in(car3)
# machine2.check_in(car4)

# machine1.check_out(car1)
# machine2.check_out(car3)
# for value in machine1.parked_cars.values():
#     print(value.License_plate)
# for value in machine2.parked_cars.values():
#     print(value.License_plate)



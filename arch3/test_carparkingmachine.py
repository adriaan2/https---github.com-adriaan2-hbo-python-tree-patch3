from carparking import *
from datetime import datetime, timedelta

# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():

    CPM = CarParkingMachine()
    CPM.check_in("XXX")
    CPM.check_in("XYZ")

    assert True == CPM.check_in("AAA")
    assert True == ("XXX" in CPM.parked_cars)

# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
       cpm=CarParkingMachine(capacity=2 )
       cpm.check_in("t")
       cpm.check_in("a")
       cpm.check_in("b")
       assert False ==("b" in cpm.parked_cars)
      
          
       
# Test for checking the correct parking fees
def test_parking_fee():
    cpm=CarParkingMachine()
    # Assert that parking time 2h10m, gives correct parking fee
    # Assert that parking time 24h, gives correct parking fee
    # Assert that parking time 30h == 24h max, gives correct parking fee
          
# Test for validating check-out behaviour
    pass

def test_check_out():
    CPM = CarParkingMachine()
    CPM.check_in("XXX")
    assert True==("XXX" in CPM.parked_cars)
    CPM.check_out("XXX")
    assert True==("XXX" in CPM.parked_cars)


    # Assert that {license_plate} is in parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    # Aseert that {license_plate} is no longer in parked_cars
    pass


test_check_in_capacity_reached()


   

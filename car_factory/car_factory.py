from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car import Car

from datetime import date

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine



class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine()
        battery = SpindlerBattery()
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine()
        battery = SpindlerBattery()
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine()
        battery = SpindlerBattery()
        return Car(current_date, last_service_date, warning_light_on, engine, battery)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine()
        battery = NubbinBattery()
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine()
        battery = NubbinBattery()
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)
from .battery import Battery
from serviceable import Serviceable
import datetime

class SpindlerBattery(Battery, Serviceable):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

        return service_threshold_date < datetime.today().date()
        
from abc import ABC, abstractmethod
from serviceable import Serviceable



class Battery(Serviceable, ABC):

    @abstractmethod
    def needs_service():
        pass
    

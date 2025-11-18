from abc import ABC, abstractmethod

class Ride(ABC):
    
    def __init__(self, id:str, name:str, min_height_cm:int):
        self.id = id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self) -> str:
        pass    

    @abstractmethod    
    def base_wait(self) -> str:
        pass
    
    def info(self) -> dict:
        return {"id": self.id, 
                "name": self.name, 
                "min_height_cm": self.min_height_cm, 
                "category": self.category()}
    
    def wait_time(self, crowd_factor: float = 1.0):
        return self.base_wait() * crowd_factor
    
class RollerCoaster(Ride):

    def __init__(self, id, name, min_height_cm, inversions:int):
        super().__init__(id, name, min_height_cm)
        self.inversions = inversions

    def category(self):
        return "roller_coaster"

    def base_wait(self):
        return super().base_wait()

    def info(self):
        return {"id": self.id, 
                "name": self.name, 
                "min_height_cm": self.min_height_cm, 
                "category": self.category(),
                "inversions": self.inversions}

class Carousel(Ride):

    def __init__(self, id, name, min_height_cm, animals:list[str]):
        super().__init__(id, name, min_height_cm)
        self.animals = animals

    def category(self):
        return "family"
    
    def base_wait(self):
        return super().base_wait()
    
    def info(self):
        return {"id": self.id, 
                "name": self.name, 
                "min_height_cm": self.min_height_cm, 
                "category": self.category(),
                "animals": self.animals}

class Park:

    def __init__(self, rides:dict[str, Ride]):
        self.rides = {}

    def add(self, ride):
        self.rides [id] = ride

    def get (self, ride_id):
        if ride_id not in self.rides:
            return None
        else:
            pass



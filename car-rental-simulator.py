from datetime import datetime
from typing import Optional, List,Dict
from abc import ABC,abstractmethod


#-------EXCEPTIONS-------
class CarNotAvailableError(Exception):
    pass

class CarNotFoundError(Exception):
    pass

class ClientNotFoundError(Exception):
    pass

class RentalAlreadyClosedError(Exception):
    pass

#-------DOMAIN MODELS-------
class Car:
    def __init__(self,number_plate:str,make:str,model:str,year:int):
        self.number_plate=number_plate
        self.make=make
        self.model=model
        self.year=year
        self.is_available=True
        
        
    @property
    def is_available(self)->bool:
        return self._is_available
    
    def mark_as_rented(self):
        if not self._is_available:
            raise ValueError("Car has already been rented") 
        self._is_available=False
        
    def mark_as_returned(self):
        self._is_available=True
        
        
class Client:
    def __init__(self,name:str,email:str):
        self.name=name
        self.email=email
        
        
class Rental:
    def __init__(self,car:Car,client:Client,rental_date:datetime):
        self.car=car
        self.client=client
        self.rental_date=rental_date
        self.return_date:datetime | None=None
        
    def close_rental(self,return_date:datetime):
        if self.return_date is not None:
            raise RentalAlreadyClosedError("Rental has already been closed")
        self.return_date=return_date
        self.car.mark_as_returned()
        
#-------REPOSITORIES-------
class CarRepository(ABC):
    @abstractmethod
    def add(self, car: Car) -> None:
        pass

    @abstractmethod
    def get(self, number_plate: str) -> Car:
        pass

    @abstractmethod
    def list_all(self) -> List[Car]:
        pass


class ClientRepository(ABC):
    @abstractmethod
    def add(self, client: Client) -> None:
        pass

    @abstractmethod
    def get(self, email: str) -> Client:
        pass

    @abstractmethod
    def list_all(self) -> List[Client]:
        pass


class RentalRepository(ABC):
    @abstractmethod
    def add(self, rental: Rental) -> None:
        pass

    @abstractmethod
    def list_active(self) -> List[Rental]:
        pass

    @abstractmethod
    def list_all(self) -> List[Rental]:
        pass

    
#-------IN-MEMORY REPOSITORIES-------

class InMemoryCarRepository(CarRepository):
    def __init__(self):
        self._cars: Dict[str, Car] = {}

    def add(self, car: Car) -> None:
        self._cars[car.number_plate] = car

    def get(self, number_plate: str) -> Car:
        if number_plate not in self._cars:
            raise CarNotFoundError(
                f"Car with number plate {number_plate} not found."
            )
        return self._cars[number_plate]

    def list_all(self) -> List[Car]:
        return list(self._cars.values())


class InMemoryClientRepository(ClientRepository):
    def __init__(self):
        self._clients: Dict[str, Client] = {}

    def add(self, client: Client) -> None:
        self._clients[client.email] = client

    def get(self, email: str) -> Client:
        if email not in self._clients:
            raise ClientNotFoundError(
                f"Client with email {email} not found."
            )
        return self._clients[email]

    def list_all(self) -> List[Client]:
        return list(self._clients.values())


class InMemoryRentalRepository(RentalRepository):
    def __init__(self):
        self._rentals: List[Rental] = []

    def add(self, rental: Rental) -> None:
        self._rentals.append(rental)

    def list_active(self) -> List[Rental]:
        return [r for r in self._rentals if r.return_date is None]

    def list_all(self) -> List[Rental]:
        return self._rentals.copy()


# =========================
# Service Layer
# =========================

class RentalService:
    def __init__(
        self,
        car_repo: CarRepository,
        client_repo: ClientRepository,
        rental_repo: RentalRepository
    ):
        self.car_repo = car_repo
        self.client_repo = client_repo
        self.rental_repo = rental_repo

    def register_car(self, number_plate: str, make: str, model: str, year: int):
        car = Car(number_plate, make, model, year)
        self.car_repo.add(car)

    def register_client(self, name: str, email: str):
        client = Client(name, email)
        self.client_repo.add(client)

    def rent_car(self, number_plate: str, client_email: str) -> Rental:
        car = self.car_repo.get(number_plate)
        client = self.client_repo.get(client_email)

        if not car.is_available:
            raise CarNotAvailableError(
                f"Car {number_plate} is not available."
            )

        car.mark_as_rented()
        rental = Rental(car, client, datetime.now())
        self.rental_repo.add(rental)

        return rental

    def return_car(self, rental: Rental):
        rental.close(datetime.now())

    def list_available_cars(self) -> List[Car]:
        return [car for car in self.car_repo.list_all() if car.is_available]

    def list_active_rentals(self) -> List[Rental]:
        return self.rental_repo.list_active()
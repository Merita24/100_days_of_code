from datetime import datetime
from typing import List,Dict
from abc import ABC, abstractmethod
import logging

#-------LOGGING CONFIGURATION-------
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")
logger=logging.getLogger(__name__)



#------EXCEPTIONS-------

class ProductNotFoundError(Exception):
    pass

class InvalidThresholdError(Exception):
    pass

class NegativeStockError(Exception):
    pass

#-------DOMAIN MODELS-------
class Product:
    def __init__(self,product_id:str,name:str,quantity_in_stock:int):
        if quantity_in_stock < 0:
            raise NegativeStockError("Quantity cannot be negative")
        self.product_id=product_id
        self.name=name
        self.quantity_in_stock=quantity_in_stock       
    def increase_stock(self,amount:int)->None:
        if amount <= 0:
            raise ValueError("Amount to increase must be non-negative")
        self.quantity_in_stock+=amount   
        logger.info(f"Increased stock for{self.name}by {amount}")
        
    def decrease_stock(self,amount:int)->None:
        if amount <= 0:
            raise ValueError("Amount to decrease must be non-negative")
        if self.quantity_in_stock-amount<0:
            raise NegativeStockError("Cannot decrease stock below zero")
        self.quantity_in_stock-=amount
        logger.info(f"Decreased stock for {self.name} by {amount}")
        
class RestockNotification:
    def __init__(self,product:Product,threshold:int):
        if threshold < 0:
            raise InvalidThresholdError("Threshold must be a non-negative integer")
        self.product=product
        self.threshold=threshold
        
    def is_low_stock(self)-> bool:
        return self.product.quantity_in_stock<=self.threshold   
    
    def create_message(self)->str:
        return(
            f"[{datetime.now()}]"
            f"LOW STOCK ALERT: {self.product.name} (ID: {self.product.product_id})" 
            f"Current Quantity:{self.product.quantity_in_stock}"
        )
    def send_notification(self)-> None:
        if self.is_low_stock():
           logger.warning(self.create_message())
            
#-------REPOSITORIES-------
class ProductRepository(ABC):
    @abstractmethod
    def add_product(self,product:Product)->None:
        pass
    @abstractmethod
    def get_product(self,product_id:str)->Product:
        pass
    @abstractmethod
    def list_all_products(self)->List[Product]:
        pass
    
    
#------IN MEMORY IMPLEMENTATION-------
class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._product: Dict[str,Product]={}
        
    def add_product(self,product:Product)->None:
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists.")
        self._product[product.product_id]=product
        logger.info(f"Prdoduct:{product.name}added successfully.")
        
    def get_product(self,product_id:str)->Product:
        if product_id not in self._product:
            raise ProductNotFoundError(f"Product with ID {product_id} not found.")
        return self._product[product_id]
    
    def list_all_products(self)->List[Product]:
        return list(self._product.values())
    
#--------SERVICE LAYER-------

class InventoryRestockManager:
    def __init__(self,product_repo:ProductRepository):
        self.product_repo=product_repo
        
    
    def register_product(self,product_id:str,name:str,quantity_in_stock:int)->None:
        product=Product(product_id,name,quantity_in_stock)
        self.product_repo.add_product(product)
        
    def list_all_products(self):
        return self.product_repo.list_all_products()
    
    def get_notification(self,product_id:str,threshold:int):
        product=self.product_repo.get_product(product_id)
        notification=RestockNotification(product,threshold)
        notification.send_notification()
        
    def check_all_products_for_restock(self,threshold:int):
        for product in self.product_repo.list_all_products():
            notification=RestockNotification(product,threshold)
            notification.send_notification()
import logging
import json
from collections import Counter

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')

def load_inventory(file):
   try:
       with open(file,"r")as f:
           data=json.load(f)
           
       if "items" not in data:
            raise KeyError("Missing 'items' key in JSON file")
       if not isinstance(data['items'],list):
            raise TypeError("'items' should be a list")
       inventory=[]
       for item in data['items']:
            if not isinstance(item,str):
                raise TypeError("All items should be strings")
            item=item.strip()
            if item:
                inventory.append(item)
            else:
                logging.warning("Empty item found and skipped")
       return inventory
   except FileNotFoundError:
         logging.error(f"File {file} not found")
   except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file {file}")
   except (KeyError,TypeError)as e:
            logging.error(e)
   return []

def count_items(inventory):
    item_counter=Counter(inventory)
    return item_counter

def display_counts(item_counter):
    for item,count in item_counter.items():
        print(f"{item}:{count}")
        
if __name__=="__main__":
    inventory=[]
    item_counter=None
    while True:
        print("\n------INVENTORY COUNTER------")
        print("1.Load Inventory from file")
        print("2.Count Items")
        print("3.Display Item Counts")
        print("4.Exit")
        
        choice=input("Enter your choice(1-4):").strip()
        if choice=="1": 
            file=input("Enter inventory file name:").strip()
            inventory=load_inventory(file)
            if inventory:
                logging.info("Inventory loaded successfully")
            else:
                logging.warning("No inventory loaded")
        elif choice=="2":  
                try:
                    item_counter=count_items(inventory)
                    logging.info("Items counted successfully")
                except Exception as e:
                    logging.warning(e)
        elif choice=="3":  
           if item_counter:
                display_counts(item_counter)
           else:
               logging.warning("No item counts available. Please count items first.")
        elif choice=="4":  
            logging.info("Exiting the program")
            break
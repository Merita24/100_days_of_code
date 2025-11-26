import os
import json

class TodolistItems:
    def __init__(self,name):
        self.name=name
        
        
    def to_dict(self):
        return{
            
            "name":self.name
        }
        
        
        
class Todolist:
    def __init__(self,filename='todo.json'):
        self.filename=filename
        self.items=self.load_items()
        
        
    def load_items(self):
        if not os.path.exists(self.filename):
            return []
        
        else:
            with open(self.filename,'r') as file:
                try:
                    data=json.load(file)
                    return data
                    
                except json.JSONDecodeError:
                    print("Error: JSON file is corrupted. Starting with an empty to-do list.")
                    return []
    
    def save_items(self):
        with open(self.filename,'w') as file:
            json.dump(self.items,file,indent=4)
            
    def add_item(self,name):
        item=TodolistItems(name)
        self.items.append(item.to_dict())
        self.save_items()
        
    def delete_item(self,index):
      if index<0 and index>len(self.items):
          print("Invalid index,please try again")
          return
      else:
        deleted=self.items.pop(index)
        self.save_items()
        print("Item deleted succcessfully")
      
    
    def view_items(self):
        with open(self.filename,'r')as file:
            items=json.load(file)
            
            if not items:
                print("No items in the to-do list.")
            
            print("\n Your To-Do List:")    
            for index,item in enumerate(items,start=1):
                print(f"{index}.{item['name']}")
import os
import json


class Contacts:
  def __init__(self,name,number,email):
    self.name=name
    self.number=number
    self.email=email

  def to_dict(self):
    return {
     "name":self.name,
     "number":self.number,
     "email":self.email   
     }
    

class ContactBook:
  def __init__(self,filename='contacts.json'):
    self.filename=filename
    self.contacts=self.load_contacts()
    
  def load_contacts(self):
    if not os.path.exists(self.filename):
        return []
    with open(self.filename, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

  def save_contacts(self):
    with open(self.filename,'w') as file:
      json.dump(self.contacts, file, indent=4)

  def add_contact(self,contact):
    self.contacts.append(contact.to_dict())
    self.save_contacts()


  def search_contact(self,name):
    for c in self.contacts:
      if c['name'].lower()==name.lower():
        return c
    
    print("contact not found")

  def delete_contact(self,name):
    contact=self.search_contact(name)
    if contact:
      self.contacts.remove(contact)
      self.save_contacts()
      print(f"{name} has been deleted successfully!")
    else:
      print("This contact does not exist")
    
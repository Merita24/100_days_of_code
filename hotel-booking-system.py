import json
from datetime import date

class Room:
    def __init__(self,room_id,room_name,room_description,room_price):
        self.room_id=room_id
        self.room_name=room_name
        self.room_description=room_description
        self.room_price=room_price
        self.is_available=True
        
    def get_room_info(self):
        return f"Room ID:{self.room_id}\nRoom Name:{self.room_name}\nRoom Description:{self.room_description}\nRoom Price:{self.room_price}\nAvailable:{self.is_available}"
    
    def to_dict(self):
        return {
            "room_id":self.room_id,
            "room_name":self.room_name,
            "room_description":self.room_description,
            "room_price":self.room_price,
            "is_available":self.is_available
            
        }
    @classmethod    
    def from_dict(cls,data):
        room=cls(
            data["room_id"],
            data["room_name"],
            data["room_description"],
            data["room_price"],
    
            )
        room.is_available=data["is_available"]
        return room
        
class Guest:
    def __init__(self,name,guest_id,contact_info):
        self.name=name
        self.guest_id=guest_id
        self.contact_info=contact_info
        self.bookings=[]
        
        
    def get_guest_info(self):
        return f"Guest ID:{self.guest_id}\nName:{self.name}\nContact Info:{self.contact_info}"
    
    def to_dict(self):
        return {
            "name":self.name,
            "guest_id":self.guest_id,
            "contact_info":self.contact_info,
            
        }
    @classmethod    
    def from_dict(cls,data):
        return cls(
            data["name"],
            data["guest_id"],
            data["contact_info"]
            
        )
        
    
class Booking:
    def __init__(self,booking_id,guest,room,check_in_date,check_out_date):
        self.booking_id=booking_id
        self.guest=guest
        self.room=room
        self.check_in_date=check_in_date
        self.check_out_date=check_out_date
        
    def get_booking_info(self):
        return f"Booking ID:{self.booking_id}\nGuest:{self.guest.name}\nRoom:{self.room.room_name}\nCheck-in Date:{self.check_in_date}\nCheck-out Date:{self.check_out_date}"
    def to_dict(self):
        return{
            "booking_id":self.booking_id,
            "guest_id":self.guest.guest_id,
            "room_id":self.room.room_id,
            "check_in_date": self.check_in_date.isoformat(),
            "check_out_date": self.check_out_date.isoformat()
        }
class HotelmanagementSystem:
    def __init__(self,name):
        self.name=name
        self.rooms={}
        self.guests={}
        self.bookings={}
        
    def add_room(self,room):
        self.rooms[room.room_id]=room
        
    def add_guest(self,guest):
        self.guests[guest.guest_id]=guest
    
    def create_booking(self,booking_id,guest_id,room_id,check_in,check_out):
        guest=self.guests.get(guest_id)
        room=self.rooms.get(room_id)
        
        if not guest or not room:
            raise ValueError("Invalid guest ID or room ID")
        if not room.is_available:
            raise ValueError("Room is not available for booking")
            
        booking=Booking(booking_id,guest,room,check_in,check_out)
        room.is_available=False
        guest.bookings.append(booking)
        self.bookings[booking_id]=booking
        
        return booking 
    
    
    def check_out(self,booking_id):
        booking=self.bookings.get(booking_id)
        if not booking:
            raise ValueError("Invalid booking ID")
        booking.room.is_available=True
        booking.guest.bookings.remove(booking)
        del self.bookings[booking_id]
        
    def save_to_file(self,filename):
        data={
            "rooms":[room.to_dict() for room in self.rooms.values()],
            "guests":[guest.to_dict()for guest in self.guests.values()],
            "bookings":[booking.to_dict()for booking in self.bookings.values()]
            
        }
        with open(filename,"w")as file:
            json.dump(data,file,indent=4)
            
    def load_from_file(self,filename):
        with open(filename,"r")as file:
            data=json.load(file)
            
        for room_data in data["rooms"]:
            room=Room.from_dict(room_data)
            self.rooms[room.room_id]=room
            
        for guest_data in data["guests"]:
            guest=Guest.from_dict(guest_data)
            self.guests[guest.guest_id]=guest
            
        for booking_data in data["bookings"]:
            guest=self.guests[booking_data["guest_id"]]
            room=self.rooms[booking_data["room_id"]]
            booking=Booking(
                booking_data["booking_id"],
                guest,
                room,
                date.fromisoformat(booking_data["check_in_date"]),
                date.fromisoformat(booking_data["check_out_date"])  
                
            )
            room.is_available=False
            self.bookings[booking.booking_id]=booking
            guest.bookings.append(booking)
            
        
if __name__=="__main__":
    hotel=HotelmanagementSystem("Grand Hotel")
    room1=Room(101,"Deluxe Suite","A luxurious suite with sea view",250)
    room2=Room(102,"Standard Room","A comfortable room with all amenities",150)
    
    hotel.add_room(room1)
    hotel.add_room(room2)
    
    guest1 = Guest("Merita", 1, "merita@email.com")
    guest2 = Guest("Alex", 2, "alex@email.com")

    hotel.add_guest(guest1)
    hotel.add_guest(guest2)
    booking1 = hotel.create_booking(
    booking_id=1,
    guest_id=1,
    room_id=101,
    check_in=date(2026, 2, 1),
    check_out=date(2026, 2, 5))
    
    hotel.save_to_file("hotel_data.json")
    print("\nDATA SAVED TO FILE")


    new_hotel = HotelmanagementSystem("Serenity Hotel Reloaded")
    new_hotel.load_from_file("hotel_data.json")

    print("\nLOADED DATA")
from functools import wraps
import logging
from datetime import datetime
import os
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')


def track_size(func):
    @wraps(func)
    def wrapper(self,*args,**kwargs):
        result=func(self,*args,**kwargs)
        self.log_size()
        return result
    return wrapper
        

class FileManager:
    def __init__(self,filepath):
        self.filepath=filepath
        self.file_history=[]
        
    def ensure_directory(self):
        directory=os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
            
    @track_size
    def create_file(self,content):
        self.ensure_directory()
        with open(self.filepath,'w') as file:
            file.write(content)
              
    @track_size      
    def append_file(self,content):
        try:
            with open(self.filepath,'a') as file:
                file.write(content)
        except FileNotFoundError:
            logging.warning("File did not exist initially......creating now")
            self.create_file(content)
            
    def get_file_size(self):
        if os.path.exists(self.filepath):
            return os.path.getsize(self.filepath)
        return 0
    
    def log_size(self):
        size=self.get_file_size()
        timestamp=datetime.now()
        self.file_history.append((timestamp,size))
        
class MemoryTracker:
    def __init__(self):
        self.filemanagers={}
      
    def track_file(self, name, filemanager):
        self.filemanagers[name] = filemanager

    def track_multiple_files(self):
        if not self.filemanagers:
            print("No files are being tracked.")
            return

        for name, fm in self.filemanagers.items():
            print(f"\nFile: {name}")
            for timestamp, size in fm.file_history:
                print(f"{timestamp} -> {size} bytes")
                
                
if __name__=="__main__":
    filemanager1=None
    memorytracker1=MemoryTracker()
    
    while True:
        print("\n Welcome to file manager and memory tracker usage")
        print("1.Create a file")
        print("2.Make changes to a file")
        print("3.List all files and memory usage:")
        print("4.Track memory usage of a specific file")
        print("5.Exit")
        
        choice=input("Enter choice:") 
        
        if choice=="1":
            filemanager1=FileManager(r"\Users\ADMIN\Desktop\merita\example.txt")
            filemanager1.create_file("Hello world, welcome to python")
            logging.info("file created successfully")
            
        if choice=="2":
            if not filemanager1:
                print("create a file first!")
                continue
            filemanager1.append_file("We are learning python basics")
            logging.info("File appended successfully")

        if choice=="3":
            memorytracker1.track_multiple_files()
            
        
        if choice=="4":
            if not filemanager1:
                print("No file to track")
                continue
            memorytracker1.track_file("example",filemanager1)
            print("file added to tracker")
            logging.info("file added to tracker")
            
        if choice=="5":
            print("Goodbye")
            break 
           
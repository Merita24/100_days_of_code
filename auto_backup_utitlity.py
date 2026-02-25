import os
import shutil
import logging
from datetime import datetime

logging.basicConfig(filename="backup.log",level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")

#EXCEPTIONS


class BackupError(Exception):
    pass

class SourceNotFoundError(BackupError):
    pass

class BackupFailedError(BackupError):
    pass


#CONTEXT MANAGER

class BackupSession:
    def __enter__(self):
        logging.info("Backup session started.")
        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            logging.error("Backup failed")
            print("Backup session failed. Check backup.log for details.")
        else:
            logging.info("Backup session completed successfully.")
            print("Backup session completed successfully.")
            
            
            
#BACKUP LOGIC

def backup_manager(source_dir,backup_dir):
    if not os.path.exists(source_dir):
        raise SourceNotFoundError("Source directory not found.")
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    for file_name in os.listdir(source_dir):
        source_path=os.path.join(source_dir,file_name)
        backup_path=os.path.join(backup_dir,file_name)
        try:
            if os.path.isfile(source_path):
                shutil.copy2(source_path,backup_path)
                logging.info(f"Backed up: {source_path} to {backup_path}")
        except Exception as e:
            logging.error("Backup failed due to error")
            raise BackupFailedError("failed to backup file")
        
        
if __name__=="__main__":
    source_directory="C:/Users/ADMIN/Desktop/source"
    backup_directory="C:/Users/ADMIN/Desktop/backup"
     
    
    with BackupSession():
        backup_manager(source_directory,backup_directory)
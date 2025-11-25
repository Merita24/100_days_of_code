class filecontextmnger:
  def __init__(self,filename,mode):
    self.filename=filename
    self.mode=mode
    self.file=None

  def __enter__(self):
    try:
      self.file=open(self.filename,self.mode)
      return self.file

    except FileNotFoundError:
      print("file not found.....creating a new one")
      if 'w' in self.mode:
        self.file=open(self.filename,self.mode)
        return self.file
      return None

  def __exit__(self,exc_type,exc_value,traceback):
    if self.file:
      self.file.close()
    

    if exc_type is not None:
      print(f"An error has ocurred:{exc_value}")
      return False
    return None








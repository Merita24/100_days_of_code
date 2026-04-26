
def data_chunks():
  li=["Apples","Oranges","Mangoes","Beetroot","Loquat","Pineapple","Grapes","Berries"]
  for i in li:
    yield i


class data_chunk_loader:
  def __init__(self,generator,chunk_size=4):
   self.generator=generator
   self.chunk_size=chunk_size


  def __enter__(self):
    print("Opening data stream.....")
    return self

  def __exit__(self,exc_type,exc_value,traceback):
    print("Exiting data stream")


  def __iter__(self):
    return self

  def __next__(self):
    chunk=[]
    try:
      for _ in range(self.chunk_size):
        chunk.append(next(self.generator))
    except StopIteration:
      if not chunk:
        raise
      return chunk


with data_chunk_loader(data_chunks(),4) as chunks:
  for chunk in chunks:
    print(chunk)
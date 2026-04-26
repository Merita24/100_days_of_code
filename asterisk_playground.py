def greet(*args,**kwargs):
  for arg in args:
    print("hello",arg)

  for k,v in kwargs.items():
    print(k,'=',v)


greet("Merita",Country="Kenya",Age=27)



def shopping_cart(*items,**details):
  for item in items:
    print(item)


  for k,v in details.items():
    print(k,'=',v)

shopping_cart("Pads","Rice","Wimbi","Minced-beef",total=655,points=6)


def comp_shopping_cart(*cart,**info):
  print(cart,info)

cart=["Laptop","Mouse","tablet","pc"]
info={"brand":"Apple","payment":"card","delivery":"Lang'ata"}
comp_shopping_cart(*cart,**info)

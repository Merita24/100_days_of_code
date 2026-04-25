def is_prime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
    return True

def prime_number_streamer():
    num=2
    while True:
      if is_prime(num):
        yield num
        num+=1
    
streamer=prime_number_streamer()
for _ in range(20):
    print(next(streamer))
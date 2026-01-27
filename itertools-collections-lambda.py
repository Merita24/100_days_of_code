from itertools import product
x=[1,2,3,6,7,8,9,12,14,16,18]
y=[4,5,10,11,13,15,17,19,20]
result=lambda a,b: (a,b) for a,b in product(x,y) if a*b>20
for pair in result:
    print(pair)
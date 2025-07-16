#custom iterators
#1 countdown iterator
class Countdown:
    def __init__(self,start):
        self.start=start


    def __iter__(self):
        return self
    

    def __next__(self):
        if self.start<0:
            raise StopIteration
        current=self.start
        self.start=self.start-1
        return current
    
for num in Countdown(5):
    print(num) 

#2 generate evens generator
def generate_evens(n):
    for x in range(n+1):
        if x%2==0:
            yield x
for num in generate_evens(20):
    print(num)
#3 reverse iterator

'''class ReverseList:
    def __init__(self,list_of_num):
        self.list_of_num=list_of_num


    def __iter__(self):
        return self

    def __next__(self):
        result=[]
        for i in self.list_of_num:
            return i+result
        
#4 fibonnaci generator

#5 skipiterator
class SkipIterator:
    def __init__(self,list_num):
        self.list_num=list_num

    def __iter__(self):
        return self
    

    def __next__(self):
        for x in self.list_num:
            result=x+2
        return result'''

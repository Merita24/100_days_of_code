import itertools
import random

names = ["Alice", "Brian", "Cynthia", "David", "Eve","Peter","John","Mary","Steve","Rachel"]
random.shuffle(names)
picker=itertools.cycle(names)
picked=set()


while True:
    user=input("Press Enter to pick a random name or CTRL+C to exit....")
    name=(next(picker))
    if name in picked:
        print(f"{name} has already been picked. Picking again...")
        picked.clear()
        random.shuffle(names)
        picker=itertools.cycle(names)
        name=(next(picker))
        picked.add(name)
    
    picked.add(name)
    print(f"Picked name: {name}")
        
    
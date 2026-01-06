from itertools import cycle,chain,groupby,accumulate,product
from collections import Counter,defaultdict,deque
#1
workers = ["Alice", "Bob", "Charlie"]
tasks_completed = 10
rotation_cycle=cycle(workers)
task_count=Counter()

for _ in range(tasks_completed):
    worker =next(rotation_cycle)
    task_count[worker]+=1
    
print(f"tasks per worker:{task_count}")

#2
store1 = ["apple", "banana", "apple"]
store2 = ["banana", "orange", "apple"]
combo=chain(store1,store2)
total=Counter(combo)
print(f"Total of each item from both stores:{total}")

#3
sales = [
    ("Mon", 100),
    ("Mon", 50),
    ("Tue", 200),
    ("Tue", 150),
    ("Wed", 300),
]

sorted_sales=sorted(sales,key=lambda x:x[0])
grouped_sales=groupby(sorted_sales,key=lambda x:x[0])
total_sales_per_day=defaultdict(int)
for day,items in grouped_sales:
    total_sales_per_day[day] +=sum(amount for _,amount in items)
    print(f"Total sales per day:{dict(total_sales_per_day)}")
    
#4
numbers = [1, 2, 1, 3, 2, 1, 4]
window_size = 3
sliding_window=deque(maxlen=window_size)
for num in numbers:
    sliding_window.append(num)
    if len(sliding_window)==window_size:
        frequency=Counter(sliding_window)
        print(frequency)
#5
users = ["U1", "U2", "U3"]
actions = ["login", "view", "logout"]
total_events = 12
users_rotate=cycle(users)
actions_cycle=cycle(actions)
activity=defaultdict(Counter)

for _ in range(total_events):
    user=next(users_rotate)
    action=next(actions_cycle)
    activity[user][action]+=1
    
print(activity)

#6
transactions = [
    ("A", 100),
    ("A", -20),
    ("B", 50),
    ("A", -30),
    ("B", 70),
]

sorted_transactions=sorted(transactions,key=lambda x:x[0])
grouped_transactions=groupby(sorted_transactions,key=lambda x:x[0])
running_balance=defaultdict(list)
for account,items in grouped_transactions:
    amounts=[amount for _,amount in items]
    running_balance[account]=list(accumulate(amounts))
print(running_balance)

#7
chars = ["a", "b", "1"]
length = 2
passwords=product(chars,repeat=2)

for pwd in passwords:
    print(''.join(pwd))

#8
events = ["A", "A", "A", "B", "B", "C", "A", "A"]
event_count=[f"{event}-{len(list(items))}" for event,items in groupby(events)]
print(event_count)
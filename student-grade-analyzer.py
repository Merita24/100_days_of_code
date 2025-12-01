from itertools import groupby
from collections import defaultdict

records=[
    ('Alex','discrete-math',86),
    ('Clyde','Signal-processing',90),
    ('Alex','Signal-processing',78),
    ('Clyde','discrete-math',85),
    ('Bob','Signal-processing',82),
    ('Bob','discrete-math',75)
      
]

grades=lambda s:"A" if s>=80 else "B" if s>=70 else "C" if s>=60 else "D" if s>50 else "F"
student=defaultdict(list)
for name,subject,score in records:
    student[name].append(score)
    
print("----student average grades----")
for name,scores in student.items():
    avg_score=sum(scores)/len(scores)
    print(f"{name}:{avg_score}:{grades(avg_score)}")
    
sorted_records=sorted(records,key=lambda x:x[1])
for subject,group in groupby(sorted_records,key=lambda x:x[1]):
    group_score=[g[2]for g in group]
    average_score=sum(group_score)/len(group_score)
    print(f"{subject}:{average_score}")
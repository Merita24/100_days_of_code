#lambda functions
#1 use filter and lambda to filter only palindromes
words = ['deed', 'noon', 'radar', 'moon', 'sun']
pal=lambda x: x==x[::-1]
result=list(filter(pal,words))

#2 sort the list by age in ascending
users = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
key= lambda x:x['age']
sorted_users=sorted(users,key)

emails = ['alice@gmail.com', 'bob@yahoo.com', 'eve@protonmail.com']
domains = list(map(lambda x: x.split('@')[1], emails))
print(domains)

#list comprehension
list_of_num=[2,4,6,9,12,14,16,18,21]
squares=[x**2 for x in list_of_num if x%3==0 and x%2!=0]

matrix = [[5, 12], [7, 14], [3, 20]]
flatten_list=[num for row in matrix for num in row if num>10]
print(flatten_list)

the_range=range(10)
multiplication_table=[x*5 for x in the_range]

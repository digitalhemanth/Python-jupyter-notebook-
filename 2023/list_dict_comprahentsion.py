lists = [4,2,8]

duble = [num*2 for num in lists]
print(duble)


names = ['hemanth','Hem']
ages = [27,28]

candiates = {name:age for name in names for age in ages}
print(candiates)



records = [    {'id': 1, 'name': 'Alice', 'age': 25},    {'id': 2, 'name': 'Bob', 'age': 35},    {'id': 3, 'name': 'Charlie', 'age': 20},    {'id': 4, 'name': 'David', 'age': 30},    {'id': 5, 'name': 'Eva', 'age': 40},    {'id': 6, 'name': 'Frank', 'age': 22},    {'id': 7, 'name': 'Gina', 'age': 28},    {'id': 8, 'name': 'Henry', 'age': 33},    {'id': 9, 'name': 'Iris', 'age': 27},    {'id': 10, 'name': 'John', 'age': 45}]

filtered_records = [r for r in records if 25 <= r['age'] <= 30]

print(filtered_records)

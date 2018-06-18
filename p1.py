import pandas as pd


students=['jane','willo','amy','penny','rach']
lowercase_names=(student.lower() for student in students)

print(lowercase_names)

print(next(lowercase_names))
print(list(lowercase_names))

#lambda function

pipeline = [lambda x: x **2 - 1 + 5,
            lambda x: x **20 - 2 + 3,
            lambda x: x **200 - 1 + 4]

for f in pipeline:
    print(f(3))

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
print(df)




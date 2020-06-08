ALGORITHM_choice = {'a': '1', 'b': '2'}

case = '2'

if case in ALGORITHM_choice.values():
    print(case)

for k in ALGORITHM_choice.values():
    print(k == case)
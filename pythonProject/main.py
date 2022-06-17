my_dict = {'key_1': [20, 80, 50], 'key_2': [200, 10, 100], 'key_3': [300, 20, 400]}
sort_my_dict = {a: sorted(b) for a, b in my_dict.items()}
print(sort_my_dict)

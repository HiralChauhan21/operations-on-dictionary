# empty dictionary
my_dict = {}

# dictionary with integers
my_dict = {1: 'apple', 2: 'balls'}

# dictionary with mixed keys
my_dict = {'name':'John', 1: [2,3,4]}

my_dict = {'name': 'Jack', 'age': 26}

# output : Jack
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

# remove perticulard element
my_dict.clear()
print(my_dict)
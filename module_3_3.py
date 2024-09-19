def print_params(a = 1, b = "строка",  c = True ):
    print(a, b, c)

print_params(12,  'stone')
print_params()
print_params(b=25)
print_params(c = [1, 2, 3])

values_list = [45, 'sister', False]
values_dict = {
    'a' : 34,
    'b' : 'goose',
    'c' : 'sunk'
}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [46, 'kick']
print_params(*values_list_2, 42)

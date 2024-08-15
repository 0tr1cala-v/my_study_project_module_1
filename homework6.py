my_dict = {'Valera': 2001, 'Artem': 2002, 'Lyuba': 2004, 'Katya': 2011}
print('Dict:', my_dict)
print('Existing value:', my_dict['Artem'])
print('Not existing value:', my_dict.get('Kolya'))
my_dict.update({'Dima': 2010,'Natasha': 2006})
a = my_dict.pop('Natasha')
print('Deleted value:', a)
print('Modified dict:', my_dict)

my_set = {1,4,5,9,5,2,1,True,'Cadillac'}
print('Set:', my_set)
my_set.add(35)
my_set.add('SRX')
my_set.remove(4)
print('Modified set:', my_set)
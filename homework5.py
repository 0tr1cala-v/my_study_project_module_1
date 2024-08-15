immutable_var = (1,5,'Ford',True)
print(immutable_var)
# сам кортеж неизменяем
# однако он может хранить в себе изменяемые элементы
mutable_list = [1,4,8,'Dodge']
print(mutable_list)
mutable_list.remove(1)
print(mutable_list)
mutable_list.append('Ram')
print(mutable_list)
mutable_list.extend([1500,'Hevy Duty'])
print(mutable_list)
mutable_list.extend('Modified')
print(mutable_list)
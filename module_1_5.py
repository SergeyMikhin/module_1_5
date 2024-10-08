immutable_var = 1, 2, 3, + 4, True, 'String'
print(type(immutable_var))
print(immutable_var)
# immutable_var[0]= 200 - выдает ошибку из-за того, что кортеж не поддерживает обращение по элементам.
immutable_list = [1,2,3 + 4, True, "String"]
print(type(immutable_list))
immutable_list[0] = 200
print(immutable_list)
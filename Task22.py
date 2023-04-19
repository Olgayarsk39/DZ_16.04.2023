# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# Решение

n = int(input("Введите количество элементов 1 множества: "))
list_1 = []
for i in range(n):
    num = int(input("Введите элемент - "))
    list_1.append(num)

m = int(input("Введите количество элементов 2 множества: "))
list_2 = []
for i in range(m):
    num = int(input("Введите элемент - "))
    list_2.append(num)

print(list_1)
print(list_2)
list_3 = set(list_1) & set(list_2)
result = list(list_3)
print (*result)


# Эталонное решение

# mol = [int(x) for x in input("Введите через пробел размеры двух множеств - ").split()]
# n = mol[0]
# m = mol[1]

# set_1 = set()
# set_2 = set()

# list_1 = list()

# a = [int(x) for x in input("Введите через пробел элементы 1-ого множества - ").split()] 
# k = set(a) 
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input("Введите через пробел элементы 2-ого множества - ").split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()

# for i in kool:
#     print(i, end=' ')

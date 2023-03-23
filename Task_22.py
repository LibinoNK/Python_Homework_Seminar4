# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def Input_List(el):
    index = 0
    numbers = []
    while index < el:
        numbers.append(int(input("Введите число: ")))
        index += 1
    return numbers


n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

first_nums = Input_List(n)
second_nums = Input_List(m)

print(f"Первое множество: {first_nums}")
print(f"Второе множество: {second_nums}")

result_list = []

for i in first_nums:
    for j in second_nums:
        if i == j:
            result_list.append(i)

print(f"Числа в обоих списках в порядке возрастания: {sorted(set(result_list))}")

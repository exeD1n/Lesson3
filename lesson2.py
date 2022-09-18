"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д."""


numders = [2, 3, 4, 5, 6]
i, j = 0, len(numders) - 1
result = []
while i < j:
    result.append(numders[i] * numders[j])
    i,j=i+1,j-1
if i == j:
    result.append(numders[i]**2)

print(result)
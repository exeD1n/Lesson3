"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""

import math

list = [1.1, 1.2, 3.1, 5, 10.01]
vesh = []
for i in list:
    y=math.modf(i)
    vesh.append(round(float(y[0]), 5))      
print(vesh)  

vesh.sort()
for i in vesh:
    if i<=0:
        vesh.remove(i)
        
print(max(vesh)-min(vesh))
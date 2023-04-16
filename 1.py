from random import randint
mass = [randint(0, 10) for s in range(10)]
mx_1, mx_2 = mass[0], mass[1]
if mass[0] < mass[1]:
    mx_1, mx_2 = mx_2, mx_1
for i in range(2, 10):
    if mass[i] > mx_1:
        mx_2, mx_1 = mx_1, mass[i]
    elif mass[i] > mx_2 and mass[i] != mx_1:
        mx_2 = mass[i]
# print(mass)
# print(mx_2)
print("Hello")
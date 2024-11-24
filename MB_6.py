## Метод Монте-Карло
import numpy as np
import matplotlib.pyplot as plt


##1 задание
# def f(x):
#     return np.where(
#         (x >= 0) & (x < 9),
#         10 * x/9,
#         10 * (x - 20) / -11
#     )
#
# x = np.linspace(0, 20, 1000)
#
# #
# # def f2(x):
# #     return 10 * (x - 20) / -11
# # def f1(x):
# #     return 10 * x/9
#
#
# N = 100
# a = 10 # по y
# b = 20
# #Генерация случайных точек
# yi = np.random.uniform(0, a, N)
# xi = np.random.uniform(0, b, N)
# #
#
# M = 0
# for j in range(0, len(xi)):
#     if(yi[j] < f(xi[j])):
#         M += 1
#
# S = M / N * a * b
#
# I = 1/2 * a * b # прощадь треугольника по формуле из школы
#
# absol = abs(I - S)
# otnos = absol / abs(I)
#
#
# print(f"Приближённая площадь фигуры: {S}")
# print(f"Абсолютная погрешность: {absol}")
# print(f"Относительная погрешность: {otnos}")
#
# plt.figure(figsize=(8, 5))
# plt.plot(x, f(x), label="y = f(x)", color="red")
# plt.axhline(y=0, color='g', label="y = 0")
# plt.scatter(xi, yi, s=4, label="Точки")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Метод Монте-Карло")
# plt.legend()
# plt.grid()
# plt.show()


# ## 2 задание
# def f(x):
#     return np.sqrt(11-9* np.sin(x)**2)
# x = np.linspace(0, 5, 1000)
# y = np.sqrt(11-9* np.sin(x)**2)
#
#
# N =100
# a = np.sqrt(11)
# b = 5
# #Генерация случайных точек
# yi = np.random.uniform(0, a, N)
# xi = np.random.uniform(0, b, N)
# M = 0
# for j in range(0, len(xi)):
#     if yi[j] < f(xi[j]):
#         M += 1
# S = M / N * a * b
# print(f"Приближённое значение интеграла: {S}")
#
# plt.figure(figsize=(8, 5))
# plt.plot(x, y, label="y = f(x)", color="red")
# plt.axvline(x=0, color='g', label="x = 0")
# plt.axvline(x=5, color='g', label="x = 5")
# plt.scatter(xi, yi, s=4, label="Точки")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Метод Монте-Карло")
# plt.legend()
# plt.grid()
# plt.show()

##3 задание

# R = 9
# N = 1000
# xi = np.random.uniform(0, 2*R, N)
# yi = np.random.uniform(0, 2*R, N)
# M = 0
# for j in range(0, len(xi)):
#     if (xi[j]-R)**2 + (yi[j]- R)**2 < R**2:
#         M += 1
# pi =( M / N) * 4
# print(f"Приближённое значение pi : {pi}")
#
# fi = np.linspace(0, 2 * np.pi, 500)
# x = R + R * np.cos(fi)
# y = R + R * np.sin(fi)
#
# plt.figure(figsize=(8, 8))
# plt.plot(x, y, label=f"Окружность, R={R}")
# plt.scatter(xi, yi, s=4, label="Точки")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Метод Монте-Карло")
# plt.legend()
# plt.grid()
# plt.show()

## 4 задание

def p1(fi):
    return np.sqrt(A * np.cos(fi)**2 + B * np.sin(fi)**2)
A = 20
B = 2
fi = np.linspace(0, 2 * np.pi, 500)
p = np.sqrt(A * (np.cos(fi))**2 + B * (np.sin(fi))**2)
x = p * np.cos(fi)
y = p * np.sin(fi)
a = (np.max(y) - np.min(y)) /2
b = (np.max(x) - np.min(x)) /2

N = 100
xi = np.random.uniform(-b, b, N)
yi = np.random.uniform(-a, a, N)

r = np.sqrt(xi**2 + yi**2)
fi_1 = np.arctan2(yi, xi) # fi = arctg(y/x)
M = 0

for j in range(0, len(xi)):
    if r[j] < p1(fi_1[j]):
        M += 1

S = M / N * a * b
print(f"Приближённая площадь фигуры: {S}")

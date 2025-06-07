print("Завдання 1: Площі трьох прямокутників")

for i in range(1, 4):
    a = float(input(f"Введіть сторону a прямокутника {i}: "))
    b = float(input(f"Введіть сторону b прямокутника {i}: "))
    area = a * b
    print(f"Площа прямокутника {i}: {area}")

import math

print("\nЗавдання 2: Порівняння гіпотенуз")

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Катет 1 трикутника 1: "))
b1 = float(input("Катет 2 трикутника 1: "))
a2 = float(input("Катет 1 трикутника 2: "))
b2 = float(input("Катет 2 трикутника 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гіпотенуза 1: {h1}")
print(f"Гіпотенуза 2: {h2}")

if h1 > h2:
    print("Гіпотенуза 1 більша.")
elif h2 > h1:
    print("Гіпотенуза 2 більша.")
else:
    print("Гіпотенузи рівні.")

print("\nЗавдання 3: Точки в колі")

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Введіть центр кола a: "))
b = float(input("Введіть центр кола b: "))
R = float(input("Введіть радіус кола R: "))

r1, r2 = map(float, input("Координати точки P (через пробіл): ").split())
f1, f2 = map(float, input("Координати точки F (через пробіл): ").split())
l1, l2 = map(float, input("Координати точки L (через пробіл): ").split())

count = 0
if is_inside_circle(r1, r2, a, b, R): count += 1
if is_inside_circle(f1, f2, a, b, R): count += 1
if is_inside_circle(l1, l2, a, b, R): count += 1

print(f"Кількість точок всередині кола: {count}")

print("\nЗавдання 4: Площа чотирикутника")

X = float(input("Сторона X: "))
Y = float(input("Сторона Y (під прямим кутом до X): "))
Z = float(input("Сторона Z: "))
T = float(input("Сторона T: "))

# Перша частина — прямокутник з площeю X * Y
# Друга частина — можна взяти як трикутник чи трапецію,
# але без додаткової інформації обчислимо лише прямий кут

S1 = X * Y  # площа прямокутного трикутника/прямокутника
print(f"Площа чотирикутника (часткова, з прямим кутом): {S1}")

print("\nЗавдання 5: Числа, що діляться на задані")

n = int(input("Введіть верхню межу n: "))
numbers = list(map(int, input("Введіть дільники через пробіл: ").split()))

result = []
for i in range(1, n + 1):
    if all(i % num == 0 for num in numbers):
        result.append(i)

print("Підходящі числа:")
print(result)

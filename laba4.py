class Car:
    def __init__(self, make, model, year):
        self.make = make            # Марка
        self.model = model          # Модель
        self.year = year            # Рік випуску
        self.speed = 0              # Початкова швидкість

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0  # Не дозволяти від’ємну швидкість

    def get_speed(self):
        return self.speed


# Створення об'єкта класу Car
my_car = Car("Toyota", "Corolla", 2020)

print("🚗 Розгін:")
for i in range(5):
    my_car.accelerate()
    print(f"Швидкість після розгону {i+1}: {my_car.get_speed()} км/год")

print("\n🛑 Гальмування:")
for i in range(5):
    my_car.brake()
    print(f"Швидкість після гальмування {i+1}: {my_car.get_speed()} км/год")

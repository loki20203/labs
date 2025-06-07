class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            # Беремо перші 5 елементів
            five = self.buffer[:5]
            print(f"Сума п’ятірки {five} = {sum(five)}")
            # Видаляємо їх з буфера
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer

buf = Buffer()

buf.add(1, 2, 3)
print("Поточні елементи:", buf.get_current_part())

buf.add(4, 5, 6)
# Має надрукувати: Сума п’ятірки [1, 2, 3, 4, 5] = 15

print("Поточні елементи:", buf.get_current_part())  # [6]

buf.add(7, 8, 9, 10, 11)
# Має надрукувати:
# Сума п’ятірки [6, 7, 8, 9, 10] = 40

print("Поточні елементи:", buf.get_current_part())  # [11]

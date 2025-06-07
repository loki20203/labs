from datetime import datetime, date

class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        
        # Розбити строку дати на рік, місяць, день
        year, month, day = map(int, birth_date_str.split('-'))
        self.birth_date = date(year, month, day)
    
    def get_age(self):
        today = date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return str(years)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

# ⬇️ Приклад використання ⬇️
person1 = Person("Шевченко", "Тарас", "1990-03-09", nickname="Кобзар")

print("Повне ім'я:", person1.get_fullname())
print("Вік:", person1.get_age())
print("Псевдонім:", person1.nickname)

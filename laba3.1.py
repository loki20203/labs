import csv

def modifier(filename):
    updated_rows = []

    # Зчитування даних з файлу
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        # Додамо нові колонки: fullname після first_name, age в кінець
        new_fieldnames = fieldnames.copy()
        insert_index = new_fieldnames.index('first_name') + 1
        new_fieldnames.insert(insert_index, 'fullname')
        new_fieldnames.append('age')

        for row in reader:
            person = Person(
                surname=row['surname'],
                first_name=row['first_name'],
                birth_date_str=row['birth_date'],
                nickname=row.get('nickname')
            )
            row['fullname'] = person.get_fullname()
            row['age'] = person.get_age()
            updated_rows.append(row)

    # Перезапис файлу з оновленими даними
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f"Файл '{filename}' оновлено успішно.")

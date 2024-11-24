import sqlite3

con = sqlite3.connect("db01.db")
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS persons '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'fio VARCHAR(30), '
            'registration TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS  personal_data'
            '(id INTEGER PRIMARY KEY AUTOINCREMENT REFERENCES persons(id) ON DELETE CASCADE, '
            'city VARCHAR(30), '
            'birthday TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS work_experience'
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'person_id INTEGER REFERENCES persons(id) ON DELETE CASCADE, '
            'company_name VARCHAR(30),'
            'position VARCHAR(30))')
var_list1 = [
    ('Шишкин Иван Иванович', '2024-11-20'),
    ('Пушкин Александр Сергеевич', '2024-11-20'),
    ('Ломоносов Михаил Васильевич', '2024-11-20')
]
var_list2 = [
    ('Москва', '1732-01-13'),
    ('Москва', '1799-06-06'),
    ('Архангельск', '1711-11-08')
]

sql1 = '''INSERT INTO persons(fio, registration) VALUES (?,?)'''
sql2 = '''INSERT INTO personal_data(city, birthday) VALUES (?,?)'''
cur.executemany(sql1, var_list1)
cur.executemany(sql2, var_list2)

var_list3 = [
    (1, 'Императорская академия художеств', 'Ученик'),
    (2, 'Коллегия иностранных дел', 'Секретарь'),
    (3, 'Питербургская академия наук', 'Профессор химии'),
    (3, 'Географический департамент академии наук', 'Глава департамента')
]
sql3 = '''INSERT INTO work_experience(person_id, company_name, position) VALUES (?,?,?)'''
cur.executemany(sql3, var_list3)

con.commit()

cur.execute("SELECT * FROM persons")
persons = cur.fetchall()
print("Люди в базе:")
for person in persons:
    print(person)
print()

cur.execute("SELECT * FROM personal_data")
persons = cur.fetchall()
print("Данные о людях:")
for person in persons:
    print(person)
print()

cur.execute("SELECT * FROM work_experience")
persons = cur.fetchall()
print("Опыт работы людей:")
for person in persons:
    print(person)
print()

cur.execute("SELECT company_name, position "
            "from work_experience "
            "where person_id = 3")
persons = cur.fetchall()
print("Опыт работы Ломоносова:")
for person in persons:
    print(person)

cur.execute("SELECT fio "
            "from persons per, personal_data data "
            "where data.city = 'Москва' and per.id = data.id")
persons = cur.fetchall()
print("Люди из Москвы:")
for person in persons:
    print(person)

cur.close()
con.close()

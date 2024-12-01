import sqlite3

con = sqlite3.connect("db01.db")
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS persons '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'fio VARCHAR(30), '
            'city VARCHAR(30), '
            'birthday TEXT,'
            'company_name VARCHAR(30),'
            'position VARCHAR(30),'
            'registration TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS vacancies'
            '(id INTEGER PRIMARY KEY AUTOINCREMENT , '
            'title TEXT NOT NULL, '
            'description TEXT,'
            'salary REAL)')
cur.execute('CREATE TABLE IF NOT EXISTS applications'
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'client_id INTEGER NOT NULL,'
            'vacancy_id INTEGER NOT NULL,'
            'application_date DATE DEFAULT CURRENT_DATE,'
            'FOREIGN KEY (client_id) REFERENCES persons(id),'
            'FOREIGN KEY (vacancy_id) REFERENCES vacancies(id))')
var_list1 = [
    ('Шишкин Иван Иванович', 'Москва', '1732-01-13', 'Императорская академия художеств', 'Ученик', '2024-11-20'),
    ('Пушкин Александр Сергеевич', 'Москва', '1799-06-06', 'Коллегия иностранных дел', 'Секретарь', '2024-11-20'),
    ('Ломоносов Михаил Васильевич', 'Архангельск', '1711-11-08', 'Питербургская академия наук', 'Профессор химии', '2024-11-20')
]
var_list2 = [
    ('Кондитер', 'Печь пироженки', '80000'),
    ('Системный аналитик', 'Писать ТЗ', '85000'),
    ('Товаровед', 'Работать на складе', '50000')
]
var_list3 = [
    (1, 1),
    (2, 3),
    (3, 2),
    (2, 2)
]
sql1 = '''INSERT INTO persons(fio, city, birthday,company_name,position, registration) VALUES (?,?,?,?,?,?)'''
sql2 = '''INSERT INTO vacancies(title, description, salary) VALUES (?,?,?)'''
sql3 = '''INSERT INTO applications(client_id, vacancy_id) VALUES (?,?)'''
cur.executemany(sql1, var_list1)
cur.executemany(sql2, var_list2)
cur.executemany(sql3, var_list3)

con.commit()

cur.execute("SELECT * FROM persons")
persons = cur.fetchall()
print("Люди в базе:")
for person in persons:
    print(person)
print()

cur.execute("SELECT * FROM vacancies")
persons = cur.fetchall()
print("Вакансии:")
for person in persons:
    print(person)
print()

cur.execute("SELECT * FROM applications")
persons = cur.fetchall()
print("Отклики:")
for person in persons:
    print(person)
print()

cur.execute("SELECT company_name, position "
            "from persons "
            "where id = 3")
persons = cur.fetchall()
print("Опыт работы Ломоносова:")
for person in persons:
    print(person)
print()

cur.execute("""
        SELECT per.fio
        FROM applications AS a
        INNER JOIN persons AS per ON a.client_id = per.id
        INNER JOIN vacancies AS v ON a.vacancy_id = v.id
        WHERE v.title = 'Системный аналитик'""")
persons = cur.fetchall()
print("На вакансию системного аналитика откликнулись:")
for person in persons:
    print(person)

cur.close()
con.close()

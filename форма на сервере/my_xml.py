import xml.dom.minidom
import sqlite3

# Подключение к базе данных
con = sqlite3.connect("db01.db")
cur = con.cursor()

# Создаем XML-документ
doc = xml.dom.minidom.Document()
root = doc.createElement('database')  # Общий корневой элемент
doc.appendChild(root)


# Функция для добавления данных таблицы в XML
def export_table_to_xml(table_name):
    # Создаем элемент для таблицы
    table_element = doc.createElement(table_name)
    root.appendChild(table_element)

    # Получаем информацию о столбцах
    cur.execute(f"PRAGMA table_info({table_name})")
    info = cur.fetchall()

    # Получаем записи из таблицы
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    # Записываем записи в XML
    for row in rows:
        record = doc.createElement('record')
        table_element.appendChild(record)
        for j in range(len(row)):
            column_name = info[j][1]  # Имя столбца
            element = doc.createElement(column_name)
            element.appendChild(doc.createTextNode(str(row[j])))
            record.appendChild(element)


# Экспортируем таблицы
export_table_to_xml("persons")
export_table_to_xml("vacancies")
export_table_to_xml("applications")

# Записываем XML в файл
with open('table.xml', 'w', encoding="utf-8") as f:
    f.write(doc.toprettyxml(indent="  "))

print("Данные успешно экспортированы в table.xml")


##запишем отдельно человека в persons

with open("table.xml", "r", encoding="utf-8") as f:
    doc = xml.dom.minidom.parse(f)

for element in doc.getElementsByTagName("persons"):
    persons = element
    break
new_record = doc.createElement("record")

# Добавляем данные в запись
columns = {"id": "300", "fio": "Новая запись из XML", "city":"XML", "birthday":"01-12-24", "company_name":"XML", "position":"XML", "registration": "2024-11-22"}
for column_name, column_value in columns.items():
    element = doc.createElement(column_name)
    element.appendChild(doc.createTextNode(column_value))
    new_record.appendChild(element)

persons.appendChild(new_record)

with open("table.xml", "w", encoding="utf-8") as f:
    f.write(doc.toprettyxml(indent="  "))

##экспорт из XML последней записи в бд

xml_file = 'table.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('persons')[0]
user = users.getElementsByTagName("record")[-1]


fio = user.getElementsByTagName('fio')[0].childNodes[0].data
city = user.getElementsByTagName('city')[0].childNodes[0].data
birthday = user.getElementsByTagName('birthday')[0].childNodes[0].data
company_name = user.getElementsByTagName('company_name')[0].childNodes[0].data
position = user.getElementsByTagName('position')[0].childNodes[0].data
registration = user.getElementsByTagName('registration')[0].childNodes[0].data

cur.execute('INSERT INTO persons (fio, city, birthday, company_name, position, registration) VALUES (?, ?, ?, ?, ?, ?)', (fio, city, birthday, company_name, position, registration))
con.commit()
cur.close()
con.close()

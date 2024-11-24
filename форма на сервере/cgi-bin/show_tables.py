import cgi
import sqlite3

con = sqlite3.connect("db01.db")
cur = con.cursor()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
 <html>
 <head>
 <meta charset="utf-8">
 <title>Таблицы </title>
 </head>
 <body>""")

cur.execute("SELECT * FROM persons")
persons = cur.fetchall()
print("<h1>Таблица persons</h1>")
for person in persons:
    print(f"<p>{person}</p>")

cur.execute("SELECT * FROM personal_data")
personal_data = cur.fetchall()
print("<h1>Таблица personal_data</h1>")
for person in personal_data:
    print(f"<p>{person}</p>")

cur.execute("SELECT * FROM work_experience")
work_experience = cur.fetchall()

print("<h1>Таблица work_experience</h1>")
for person in work_experience:
    print(f"<p>{person}</p>")

print("""</body> </html>""")

cur.close()
con.close()
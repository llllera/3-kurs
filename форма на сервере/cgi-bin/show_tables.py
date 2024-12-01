
import sqlite3

def print_table(table_name):
    print(f"<h1>{table_name}</h1>")
    cur.execute(f"PRAGMA table_info({table_name})")
    info = cur.fetchall()
    print(f'<div class="table" style="grid-template-columns: repeat({len(info)}, 1fr);">')
    for col in info:
        print(f'<div class="header">{col[1]}</div>')
    cur.execute(f"SELECT * FROM {table_name}")
    all = cur.fetchall()
    for col in all:
        for i in range(len(col)):
            print(f'<div class="cell">{col[i]}</div>')
    print("</div>")

con = sqlite3.connect("db01.db")
cur = con.cursor()


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
 <html>
 <head>
 <meta charset="utf-8">
 <title>Таблицы </title>
 <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        .table {
            display: grid;
            gap: 10px; /* Отступы между ячейками */
            max-width: 800px;
            margin: auto;
        }

        .header, .cell {
            padding: 10px;
            text-align: center;
            border: 1px solid #ddd;
        }

        .header {
            background-color: #f4f4f4;
            font-weight: bold;
        }

        .row:nth-child(even) .cell {
            background-color: #f9f9f9;
        }
    </style>
 </head>
 <body>""")

# cur.execute("SELECT * FROM persons")
# persons = cur.fetchall()
# print("<h1>Таблица persons</h1>")
# for person in persons:
#     print(f"<p>{person}</p>")

print_table("persons")
print_table("vacancies")
print_table("applications")


print("""</body> </html>""")

cur.close()
con.close()
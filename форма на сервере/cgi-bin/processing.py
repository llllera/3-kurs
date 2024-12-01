import cgi
import sqlite3
from datetime import date

form = cgi.FieldStorage()
fio = form.getfirst("fio", "не задано")
city = form.getfirst("city", "не задано")
birthdate = form.getfirst("birthdate", "не задано")
workplace = form.getfirst("workplace", "не задано")
position = form.getfirst("position", "не задано")
today = date.today().strftime("%Y-%m-%d")

fio_1 = form.getfirst("fio_1", "не задано")
title = form.getfirst("title", "не задано")
descr = form.getfirst("descr", "не задано")
salary = form.getfirst("salary", "не задано")
title_1 = form.getfirst("title_1", "не задано")

con = sqlite3.connect("db01.db")
cur = con.cursor()



if(fio!='не задано'):
    var1 = {"fio": fio, "city": city, "birthday": birthdate, "company_name": workplace, "position": position,
            "registration": today}
    sql1='''INSERT INTO persons(fio, city, birthday, company_name, position, registration) VALUES (:fio, :registration, :birthday, :company_name, :position, :registration)'''
    cur.execute(sql1, var1)

if(title!='не задано'):
    var2 = {"title": title, "description": descr, "salary": salary}
    sql2='''INSERT INTO vacancies(title, description, salary) VALUES (:title, :description, :salary)'''
    cur.execute(sql2, var2)

if(fio_1!="не задано"):
    sql ='''SELECT id FROM persons where fio = ?'''
    cur.execute(sql, (fio_1,))
    id_client = cur.fetchone()
    sql ='''SELECT id FROM vacancies where title = ?'''
    cur.execute(sql, (title_1,))
    id_vacancy = cur.fetchone()

    var3 = {"id_client":id_client[0], "id_vacancy":id_vacancy[0]}
    sql3='''INSERT INTO applications(client_id, vacancy_id) VALUES (:id_client, :id_vacancy)'''
    cur.execute(sql3,var3)

con.commit()
cur.close()
con.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
 <html>
 <head>
 <meta charset="utf-8">
 <title>Таблицы </title>
 <style>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    h1 {
        text-align: center;
    }
</style>
 </head>
 <body>
 <h1>Спасибо, ваши данные отправлены</h1>
 </body> </html>""")

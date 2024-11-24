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

con = sqlite3.connect("db01.db")
cur = con.cursor()

var1 = {"fio":fio, "registration":today}
var2 = {"city":city, "birthday":birthdate}

sql1='''INSERT INTO persons(fio, registration) VALUES (:fio, :registration)'''
sql2='''INSERT INTO personal_data(city, birthday) VALUES (:city, :birthday)'''
cur.execute(sql1,var1)
cur.execute(sql2,var2)

sql ='''SELECT id FROM persons where fio = ?'''
cur.execute(sql, (fio,))
id = cur.fetchone()
var3 = {"person_id":id[0], "company_name":workplace, "position":position}
sql3='''INSERT INTO work_experience(person_id, company_name, position) VALUES (:person_id, :company_name, :position)'''
cur.execute(sql3,var3)

con.commit()
cur.close()
con.close()

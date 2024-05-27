import pandas as pd
import sqlite3	

con = sqlite3.connect('names.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS names(
	name text primary key ,
	first text,
	second text,
	third text,
	fourth text
	)""")
data = [
		('דהרי' , '1', '1' ,'1','1'),
		('אייש' , '1', '1' ,'1','1'),
		('בצר' , '1', '1' ,'1','1'),
		('קדמי' , '1', '1' ,'1','1'),
		('סופר' , '1', '1' ,'1','1'),
		('נגר' , '1', '1' ,'1','1'),
		('נחמן' , '1', '1' ,'1','1'),
		('כץ' , '1', '1' ,'1','1'),
		('שחר' , '1', '1' ,'1','1'),
		('קלישר' , '1', '1' ,'1','1')
		]
statement = "INSERT INTO names(name,first,second,third,fourth) VALUES(?,?,?,?,?)"




query = "SELECT * FROM names"

df = pd.read_sql_query(query, con)
print(df)



con.commit()
con.close()
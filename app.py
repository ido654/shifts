from flask import Flask, render_template,flash, request, jsonify, redirect, url_for
import pandas as pd
import sqlite3
import os
import sqlite3
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/firstName')
def name():
	con = sqlite3.connect('names.db')
	query = "SELECT * FROM names"
	df = pd.read_sql_query(query, con)

	firstName = request.args.get('firstName')
	if firstName in df.name.values:
		return render_template('form.html' ,firstName=firstName)
	else:
		error_msg = 'השם אינו מזוהה במערכת נסה שם אחר'
		return render_template('index.html' , error_msg=error_msg)

@app.route('/sending', methods=['POST'])
def sending():
	if request.method=='POST':
		name = request.form.get('fName')
		a = request.form.get('options-base-1')
		b = request.form.get('options-base-2')
		c = request.form.get('options-base-3')
		d = request.form.get('options-base-4')
		if a != None and b!=None and c !=None and d!=None:
			con = sqlite3.connect('names.db')
			cur = con.cursor()
			cur.execute("""UPDATE names SET 
				first=?,
				second=?,
				third=?,
				fourth=?
				WHERE name = ?""",(a,b,c,d,name) )
			con.commit()
			con.close()
			print("successfully saved!")

		else:
			print('False')


			
		return render_template('prefs.html' , name=name, a=a,b=b,c=c,d=d)



@app.route("/admin")
def admin():
	con = sqlite3.connect('names.db')
	cur=con.cursor()
	cur.execute('SELECT * FROM names')
	names = cur.fetchall()
	con.close()


	return render_template('admin.html', names=names)




if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0')











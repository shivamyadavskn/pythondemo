from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "1234"
app.config['MYSQL_DB'] = "alchemy"
mysql = MySQL(app)



@app.route('/')
def dummy():
    cur = mysql.connection.cursor()
    cur.execute("SELECT*FROM demo")
    account = cur.fetchall()
    print(account)
    return render_template('home.html', account=account)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'students'

mysql = MySQL(app)

@app.route("/", methods=['POST', 'GET'])
def index():
   
    cursor = mysql.connection.cursor()
    

    cursor.execute("SELECT id, name, age, class FROM information")
    students = cursor.fetchall()
    

    cursor.close()

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)

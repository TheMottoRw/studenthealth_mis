from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'Shealthmis'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'super'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'shealthmis'
db = MySQL(app)
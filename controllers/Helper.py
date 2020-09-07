from config import app,db
from flask import jsonify,session,redirect,url_for
import base64
def login(request):
    feed = 'ok'
    password = str(base64.b64encode(request.values['password'].encode('utf-8')),'utf-8')
    print(password)
    try:
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM administrators WHERE phone=%s and password=%s",(request.values['phone'],password))
        data = cur.fetchall()
        if(len(data)==1):
            session['userid'] = data[0][0]
            session['category'] = 'Administrator'
            session['names'] = data[0][1]
            print("success")
        else:#check nurse
            cur.execute("SELECT * FROM nurses WHERE phone=%s and password=%s",(request.values['phone'],password))
            data = cur.fetchall()
            if(len(data)==1):
                session['userid'] = data[0][0]
                session['category'] = 'Nurse'
                session['names'] = data[0][1]
                print("Nurse success")
            else:
                feed = 'fail'
                print("Wrong username or password")
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return feed

def logout(request):
    session.pop('userid')
    session.pop('category')
    session.pop('names')
    return 1
def checkSession(request):
    if('userid' not in session):
        return 0
    return 1

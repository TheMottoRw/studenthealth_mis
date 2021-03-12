from config import app,db
from flask import jsonify,redirect
import base64
def save(names,phone,pwd):
    password = str(base64.b64encode(pwd.encode('utf-8')),'utf-8')
    cur = db.connection.cursor()
    cur.execute("INSERT INTO nurses SET names=%s,phone=%s,password=%s",(names,phone,password))
    db.connection.commit()
    cur.close()
    return "User created"
def get(request):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM nurses")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'phone':obj[2],'password':obj[3],'regdate':obj[6]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return arr

def getById(ids):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM nurses where id=%s",(str(ids)))
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'phone':obj[2],'password':obj[3],'regdate':obj[6]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return arr

def update(ids,names,phone,pwd):
    try:
        password = str(base64.b64encode(pwd.encode('utf-8')),'utf-8')
        cur = db.connection.cursor()
        rs = cur.execute("UPDATE nurses SET names=%s,phone=%s,password=%s WHERE id=%s",(names,phone,password,ids))
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "User updated"

def delete(ids):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("DELETE FROM nurses WHERE id='"+str(ids)+"'")
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return redirect('/v/nurse')
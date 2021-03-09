from config import app,db
from flask import jsonify
def save(department,email):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO hods_email SET department=%s,department_email=%s",(department,email))
    db.connection.commit()
    cur.close()
    return "User created"
def get(request):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM hods_email")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'department':obj[1],'department_email':obj[2],'regdate':obj[3]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return arr
    # return data

def getById(ids):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM hods_email where id=%s",(str(ids)))
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'department':obj[1],'department_email':obj[2],'regdate':obj[4]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return jsonify(arr)

def update(ids,department,email):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("UPDATE hods_email SET department=%s,department_email=%s WHERE id=%s",(department,email,ids))
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "User updated"

def delete(request,ids):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("DELETE FROM hods_email WHERE id=%s",(str(ids)))
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "User updated"
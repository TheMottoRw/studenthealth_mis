from config import app,db
from flask import jsonify
def save(names,phone,pwd):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO administrators SET names=%s,phone=%s,password=%s",(names,phone,pwd))
    db.connection.commit()
    cur.close()
    return "User created"
def get(request):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM administrators")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'phone':obj[2],'password':obj[3],'regdate':obj[4]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return jsonify(arr)
    # return data

def getById(ids):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM administrators where id=%s",(str(ids)))
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'phone':obj[2],'password':obj[3],'regdate':obj[4]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return jsonify(arr)

def update(ids,names,phone):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("UPDATE administrators SET names=%s,phone=%s WHERE id=%s",(names,phone,ids))
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
        rs = cur.execute("DELETE FROM administrators WHERE id='"+str(ids)+"'")
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "User updated"
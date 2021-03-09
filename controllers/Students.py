from config import app,db
from flask import jsonify,redirect
def save(names,phone,department,regno,hasInsurance,insuranceType,insuranceNumber):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO students SET names=%s,phone=%s,department=%s,regno=%s,has_insurance=%s,insurance_type=%s,insurance_number=%s",(names,phone,department,regno,hasInsurance,insuranceType,insuranceNumber))
    db.connection.commit()
    cur.close()
    return "ok"
def get(request):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'phone':obj[2],'department':obj[3],'regno':obj[4],'has_insurance':obj[5],'insurance_type':obj[6],'insurance_number':obj[7],'regdate':obj[8]})
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
        cur.execute("SELECT * FROM students where id=%s",(str(ids)))
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'phone':obj[2],'department':obj[3],'regno':obj[4],'has_insurance':obj[5],'insurance_type':obj[6],'insurance_number':obj[7],'regdate':obj[8]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return jsonify(arr)

def getByRegno(key):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("select * from students where regno='"+key+"'")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'phone':obj[2],'regno':obj[3],'has_insurance':obj[4],'insurance_type':obj[5],'insurance_number':obj[6],'regdate':obj[7]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    print(arr)
    return jsonify(arr)


def update(ids,names,phone,regno,hasInsurance,insuranceType,insuranceNumber):
    try:
        cur = db.connection.cursor()
        cur.execute("UPDATE students SET names=%s,phone=%s,regno=%s,has_insurance=%s,insurance_type=%s,insurance_number=%s WHERE id=%s",(names,phone,regno,hasInsurance,insuranceType,insuranceNumber,ids))
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "Students updated"

def delete(ids):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("DELETE FROM students WHERE id=%s",(str(ids)))
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return redirect('/v/students')

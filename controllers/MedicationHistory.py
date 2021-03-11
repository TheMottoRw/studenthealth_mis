from config import app,db
from flask import jsonify,redirect
from controllers.Consultation import getById
def save(medication_id,current_qty,added,total_qty,expiration,batch):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO medication_history SET medication_id=%s,current_qty=%s,added_quantity=%s,total_qty=%s,expiry_date=%s,batch_no=%s",(medication_id,current_qty,added,total_qty,expiration,batch))
    db.connection.commit()
    cur.close()
    return "ok"
def get(request):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT mh.*,m.names FROM medication_history mh INNER JOIN medications m on mh.medication_id=m.id")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'medication_id':obj[1],'name':obj[8],'current_qty':obj[2],'added_qty':obj[3],'total_qty':obj[4],'expiry_date':obj[5],'batch_number':obj[6],'regdate':obj[7]})
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
        cur.execute("SELECT * FROM medication_history where id=%s",(str(ids)))
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'medication_id':obj[1],'current_qty':obj[2],'added_quantity':obj[3],'total_quantity':obj[4],'expiry_date':obj[5],'batch_number':obj[6],'regdate':obj[7]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return jsonify(arr)

def update(ids,medication_id,current_qty,stock,total_qty,expiration,batch):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("UPDATE medication_history SET medication_id=%s,current_qty=%s,added_quantity=%s,total_qty=%s,expiry_date=%s,batch_no=%s where id=%s",(medid,current_qty,added_quantity,total_qty,expiration,batch,ids))
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "Medication updated"

def delete(ids):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("DELETE FROM medication_history WHERE id='"+str(ids)+"'")
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "ok"
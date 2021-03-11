from config import app,db
from flask import jsonify,redirect
from controllers import MedicationHistory
def save(names,description,stock,unit):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO medications SET names=%s,description=%s,available_stock=%s,unit=%s",(names,description,stock,unit))
    db.connection.commit()
    cur.close()
    return "Medication created"
def get(request):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM medications")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'description':obj[2],'available_stock':obj[3],'unit':obj[4],'regdate':obj[5]})
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
        cur.execute("SELECT * FROM medications where id=%s",(str(ids)))
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'description':obj[2],'available_stock':obj[3],'unit':obj[4],'regdate':obj[5]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return arr


def addQuantity(request,ids):
    try:
        cur = db.connection.cursor()
        current = getById(ids)
        current_qty = int(current[0]['available_stock'])
        added = int(request.values['quantity'])
        total = current_qty + added
        batch = request.values['batch']
        expiry_date = request.values['expiry']
        rs = cur.execute("UPDATE medications SET available_stock=%s where id=%s",(total,ids))

        MedicationHistory.save(ids,current_qty,added,total,expiry_date,batch)
        
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "ok"


def updateRemainingQuantity(ids,quantity):
    try:
        cur = db.connection.cursor()
        current = getById(ids)
        current_qty = int(current[0]['available_stock'])
        remained_qty = current_qty - int(quantity)
        rs = cur.execute("UPDATE medications SET available_stock=%s where id=%s",(remained_qty,ids))
        
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "ok"

def update(ids,names,description,stock,unit):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("UPDATE medications SET names=%s,description=%s,available_stock=%s,unit=%s where id=%s",(names,description,stock,unit,ids))
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
        rs = cur.execute("DELETE FROM medications WHERE id='"+str(ids)+"'")
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "Medication deleted"
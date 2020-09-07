from config import app,db
from flask import jsonify
from controllers import MedicationGiven,Medications
def save(student,height,weight,symptoms,medications,medication_qty,conditions):
    cur = db.connection.cursor()
    rs = cur.execute("INSERT INTO consultation SET student=%s,height=%s,weight=%s,symptoms=%s,medications=%s,medication_qty=%s,conditions=%s",(student,height,weight,symptoms,medications,medication_qty,conditions))
    db.connection.commit()
    cur.close()
    return "Consultation created"

def get(request):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT c.*,s.names,s.regno FROM consultation c inner join students s on s.id = c.student")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            #get prescription details
            cur.execute("SELECT CONCAT(m.names,' - ',mg.quantity,' ',m.unit) as prescription FROM medication_given mg inner join medications m ON m.id=mg.medication WHERE mg.consultation_id="+str(obj[0]))
            # cur.execute("SELECT * FROM medication_given")
            prescription = cur.fetchall()
            prescriptionCount = 0
            prescriptionStr = ''
            while(prescriptionCount<len(prescription)):
                prescriptionStr+= str(prescription[prescriptionCount][0])+'('+obj[7]+')\n'
                prescriptionCount+=1
            
            arr.append({'id':obj[0],'student':obj[1],'names':obj[9],'regno':obj[10],'height':obj[2],'weight':obj[3],'symptoms':obj[4],'medications':obj[5],'medications_quantity':obj[6],'conditions':obj[7],'regdate':obj[8],'prescription':prescriptionStr})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    # print('arr '+str(arr))
    return arr

def getById(ids):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM consultation where id=%s",(str(ids)))
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'student':obj[1],'height':obj[2],'weight':obj[3],'symptoms':obj[4],'medications':obj[5],'medications_quantity':obj[6],'conditions':obj[7],'regdate':obj[8]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return jsonify(arr)



def search(key):
    try:
        arr = []
        cur = db.connection.cursor()
        cur.execute("SELECT c.id,s.names,s.regno,c.regdate FROM consultation c inner join students s on s.id = c.student where s.regno='"+key+"' order by c.regdate desc")
        data = cur.fetchall()
        count = 0
        while(count < len(data)):
            obj = data[count]
            arr.append({'id':obj[0],'names':obj[1],'regno':obj[2],'regdate':obj[3]})
            count += 1
    except Exception as e:
        print(e)
    finally:
        cur.close()
    # print('arr '+str(arr))
    return jsonify(arr)

def update(ids,student,height,weight,symptoms,medications,medication_qty):
    feed = 'ok'
    try:
        cur = db.connection.cursor()
        rs = cur.execute("UPDATE consultation SET student=%s,height=%s,weight=%s,symptoms=%s,medications=%s,medication_qty=%s where id=%s",(student,height,weight,symptoms,medications,medication_qty,ids))
        db.connection.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return feed



def prescribe(consultationId,medicationId,quantity,condition):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("UPDATE consultation SET conditions=%s where id=%s",(condition,consultationId))
        MedicationGiven.save(consultationId,medicationId,quantity)
        #deduce medication quantity from available stock
        Medications.updateRemainingQuantity(medicationId,quantity)
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "Consultation updated"

def delete(ids):
    try:
        cur = db.connection.cursor()
        rs = cur.execute("DELETE FROM consultation WHERE id=%s",(str(ids)))
        db.connection.commit()
        print("result "+str(rs))
    except Exception as e:
        print(e)
    finally:
        cur.close()
    return "Consultation deleted"
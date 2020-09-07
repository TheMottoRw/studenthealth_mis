from config import app,db
from flask import jsonify,session
def save(consultation,medication,quantity):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO medication_given SET consultation_id=%s,medication=%s,quantity=%s,nurse=%s",(consultation,medication,quantity,session['userid']))
    db.connection.commit()
    cur.close()
    return "ok"
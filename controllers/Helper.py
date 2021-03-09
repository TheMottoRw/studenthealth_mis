from flask import jsonify,session,redirect,url_for
import base64,smtplib,random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import app,db


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


def sendGmail(to,subject,message):
    feed = 'ok'
    # subject = subject # The subject line

    msg = MIMEMultipart()
    msg['Message-Id'] = str(random.random()*100000)
    msg['From'] = 'hasua.mr@gmail.com'
    msg['FromName'] = 'Manzi Roger'
    msg['To'] = to
    msg['Subject'] = subject
    msg['Reply-To'] = "hasua.mr@gmail.com"
    msg['Host'] = "smtp.gmail.com"
    msg['SMTPAuth'] = 'true'
    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'html'))
    textMessage = msg.as_string()  # convert object in text
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Next, log in to the server
    server.login("hasua.mr@gmail.com", "Roger2709")
    # Send the mail
    try:
        response=server.sendmail(msg['From'], msg['To'], textMessage)
        print(str(response))
    except:
        feed = 'fail'
    server.quit()
    return feed

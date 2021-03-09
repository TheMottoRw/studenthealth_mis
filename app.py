from flask import Flask,request,json,render_template,redirect,url_for,session,jsonify
from controllers import Nurses,Students,Administrator,Medications,MedicationHistory,Consultation,Helper,HodsEmail
from config import app

@app.route('/',methods = ['GET','POST'])
def index():
    return redirect('/v')

#views
@app.route('/v/',methods = ['GET'])
def vIndex():
    return render_template('index.html',rows = Administrator.get)


@app.route('/v/students',methods = ['GET'])
def vStudents():
    if(Helper.checkSession(request) == 0):
        return redirect('/')
    feed = Students.get(request)
    return render_template('students.html',students = feed)

@app.route('/v/depemail',methods = ['GET'])
def vHodemail():
    if(Helper.checkSession(request) == 0):
        return redirect('/')
    feed = HodsEmail.get(request)
    print(feed)
    return render_template('department_emails.html',hodsemail = feed)
    # return jsonify(feed)

@app.route('/v/stdopenlink',methods = ['GET'])
def vStudentsOpenRegistration():
    feed = Students.get(request)
    return render_template('student_open_registration.html')


@app.route('/v/nurse',methods = ['GET'])
def vNurse():
    if(Helper.checkSession(request) == 0):
        return redirect('/')
    return render_template('nurses.html',nurses=Nurses.get(request))

@app.route('/v/consultation',methods = ['GET'])
def vConsultation():
    if(Helper.checkSession(request) == 0):
        return redirect('/')
    return render_template('consultation.html',consultations = Consultation.get(request))

@app.route('/v/search',methods = ['GET'])
def vSearch():
    return render_template('search.html')

@app.route('/v/prescription',methods = ['GET'])
def vPrescription():
    if(Helper.checkSession(request) == 0):
        return redirect('/')
    return render_template('medication_given.html')

@app.route('/v/medication',methods = ['GET'])
def vMedication():
    if(Helper.checkSession(request) == 0):
        return redirect('/')
    return render_template('medications.html',medications = Medications.get(request))

@app.route('/v/medhistory',methods = ['GET'])
def vMedicationHistory():
    if(Helper.checkSession(request) == 0):
        return redirect('/')
    return render_template('medication_history.html',medications = MedicationHistory.get(request))

#error pages
@app.errorhandler(404)
def page_not_found(request):
    return render_template('error_pages/404.html',data='Error page')
#admin route
@app.route('/admin',methods=['GET'])
def admin():
    feed = "admin created"
    if(request.method == 'POST'):
       feed = Administrator.save("Asua","0726183049","1243")
    else:
        feed = Administrator.get(request)
        print(feed)
    return feed
@app.route('/admin/<int:id>', methods = ['GET','POST'])
def updateAdmin(id):
    if(request.method == 'POST'):
        feed = Administrator.update(id,'Manzi','0726183049')
    else:
        feed = Administrator.getById(id)
    return feed

@app.route('/admin/delete/<int:id>', methods = ['GET'])
def deleteAdmin(id):
    feed = Administrator.delete(id)
    return feed


@app.route('/depemail',methods=['GET','POST'])
def depemail():
    feed = "email created"
    if(request.method == 'POST'):
    #    feed = Students.save('Manzi','0726183049','17rp01001','Yes','RSSB','1232423')
       feed = HodsEmail.save(request.values['department'],request.values['department_email'])
       returnRoute = render_template('department_emails.html',message = feed,hodsemail = HodsEmail.get(request))
    else:
        # feed = HodsEmail.get(request)
        returnRoute = redirect('/v/depemail')
        print(feed)
    return returnRoute



@app.route('/depemail/<int:id>', methods = ['GET','POST'])
def updateDepemail(id):
    if(request.method == 'POST'):
        feed = HodsEmail.update(id,request.values['department_box'],request.values['department_email'])
        returnRoute = redirect('/v/depemail')
        return returnRoute
    else:
        feed = HodsEmail.getById(id)
        returnRoute = redirect('/v/depemail')
        return jsonify(feed)

@app.route('/depemail/delete/<int:id>', methods = ['GET'])
def deleteEmail(id):
    feed = HodsEmail.delete(id)
    return feed

@app.route('/login',methods = ['GET','POST'])
def login():
    if(request.method == 'GET'):
        return redirect('/v')
    data = Helper.login(request)
    if(data=='fail'):
        message = 'Wrong username or password'
        returnRoute = render_template('index.html',message = message)
    else:#check if admin or nurses
        if(session['category'] == 'Administrator'):
            returnRoute = redirect('/v/students')
        else:
            returnRoute = redirect('/v/consultation')
    return  returnRoute

@app.route('/logout',methods = ['GET'])
def logout():
    Helper.logout(request)
    return redirect('/v')

#nurses route
@app.route('/nurse',methods=['GET','POST'])
def nurse():
    feed = "nurse created"
    if(request.method == 'POST'):
       feed = Nurses.save(request.values['names'],request.values['phone'],request.values['password'])
       returnRoute = render_template('nurses.html',message=feed,nurses=Nurses.get(request))
    else:
        feed = Nurses.get(request)
        returnRoute = redirect('/v/nurse')
        print(feed)
    return returnRoute

@app.route('/nurse/<int:id>', methods = ['GET','POST'])
def updateNurse(id):
    if(request.method == 'POST'):
        # feed = Nurses.update(id,'Manzi','0726183049')
        feed = Nurses.update(id,request.values['names'],request.values['phone'],request.values['password'])
        returnRoute = redirect('/v/nurse')
    else:
        feed = Nurses.getById(id)
        returnRoute = feed
    return returnRoute

@app.route('/nurse/delete/<int:id>', methods = ['GET'])
def deleteNurse(id):
    feed = Nurses.delete(id)
    return feed

#students route
@app.route("/gmail")
def sendEmail():
    return Helper.sendGmail("mnzroger@gmail.com","For your information","Hello <b>Roger</b>,We are running and py email.")
@app.route('/students',methods=['GET','POST'])
def students():
    feed = "student created"
    if(request.method == 'POST'):
    #    feed = Students.save('Manzi','0726183049','17rp01001','Yes','RSSB','1232423')
       feed = Students.save(request.values['names'],request.values['phone'],request.values['department'],request.values['regno'],'Yes',request.values['insurance'],request.values['insurance_number'])
       returnRoute = render_template('students.html',message = feed,students = Students.get(request))
    else:
        returnRoute = redirect('/v/students')
        print(feed)
    return returnRoute

@app.route('/openlink',methods=['POST'])
def openLink():
    feed = "student created"
    if(request.method == 'POST'):
    #    feed = Students.save('Manzi','0726183049','17rp01001','Yes','RSSB','1232423')
       feed = Students.save(request.values['names'],request.values['phone'],request.values['regno'],'Yes',request.values['insurance'],request.values['insurance_number'])
       returnRoute = redirect('/v/stdopenlink')
       print(feed)
    return returnRoute

@app.route('/student/<regno>', methods = ['GET','POST'])
def studentByRegno(regno):
    print(regno)
    feed = Students.getByRegno(regno)
    return feed

@app.route('/student/<int:id>', methods = ['GET','POST'])
def studentById(id):
    if(request.method == 'POST'):
        feed = Students.update(id,'Manzi','0726183049','17rp01001','Yes','RSSB','1232423')
    else:
        feed = Students.getById(id)
    return feed

@app.route('/student/delete/<int:id>', methods = ['GET'])
def deleteStudent(id):
    feed = Students.delete(id)
    return feed
    # return redirect('/v/students')

#Medication route
@app.route('/medications',methods=['GET','POST'])
def medication():
    feed = "medication created"
    if(request.method == 'POST'):
       feed = Medications.save(request.values['names'],request.values['description'],request.values['quantity'],request.values['unit'])
       returnRoute = render_template('medications.html',medications = Medications.get(request),message = feed)
    else:
        if('data' in request.values):
            returnRoute = jsonify(Medications.get(request))
        else:
            returnRoute = redirect('/v/medication')
        print(feed)
    return returnRoute

@app.route('/medication/<int:id>', methods = ['GET','POST'])
def medicationById(id):
    if(request.method == 'POST'):
        # feed = Medications.update(id,'Hydrocynone','Ifasha mu kugabanya umuriro','12','Pieces')
       feed = Medications.update(id,request.values['names'],request.values['description'],request.values['quantity'],request.values['unit'])
       returnRoute = redirect('/v/medication')
    else:
        feed = Medications.getById(id)
    return returnRoute

@app.route('/medication/add/<id>', methods = ['POST'])
def medicationAdd(id):
    feed = Medications.addQuantity(request,id)
    return feed

@app.route('/medication/delete/<int:id>', methods = ['GET'])
def deleteMedication(id):
    feed = Medications.delete(id)
    return redirect('/v/medication')


#Medication history route

@app.route('/medhistory/delete/<int:id>', methods = ['GET'])
def deleteMedicationHistory(id):
    feed = MedicationHistory.delete(id)
    return redirect('/v/medhistory')

#consultation route
@app.route('/consultations',methods=['GET','POST'])
def consultation():
    feed = "consultation created"
    if(request.method == 'POST'):
       feed = Consultation.save(request.values['studentId'],request.values['height'],request.values['weight'],request.values['symptoms'],'','','')
       returnRoute = render_template('consultation.html',message=feed,consultations = Consultation.get(request))
    else:
        returnRoute = redirect('/v/consultation')
        print(feed)
    return returnRoute

@app.route('/prescribe', methods = ['GET','POST'])
def prescribePatient():
    if(request.method == 'POST'):
        feed = Consultation.prescribe(request.values['consultationId'],request.values['medicationId'],request.values['quantity'],request.values['condition'])
    else:
        feed = Consultation.getById(id)
    return feed

@app.route('/consultation/<key>', methods = ['GET'])
def searchConsultation(key):
    feed = Consultation.search(key)
    return feed

@app.route('/consultation/<int:id>', methods = ['GET','POST'])
def consultationById(id):
    if(request.method == 'POST'):
        # feed = Consultation.update(id,'1','192','109','Umuriro,kubabara igifu','1,2','3,7','Kimwe ku munsi,ikindi nijoro')
       feed = Consultation.update(id,request.values['studentId'],request.values['height'],request.values['weight'],request.values['symptoms'],'','')
       returnRoute = redirect('/v/consultation')
    else:
        feed = Consultation.getById(id)
        returnRoute = feed
    return returnRoute

@app.route('/consultation/delete/<int:id>', methods = ['GET'])
def deleteConsultation(id):
    feed = Consultation.delete(id)
    return feed

@app.route('/consultation/report', methods = ['GET'])
def reportConsultation():
    feed = Consultation.report()
    return feed

if __name__ == '__main__':
    app.run(debug=True)

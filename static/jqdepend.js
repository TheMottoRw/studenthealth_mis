
function ajax(url, getpars, typ, responseType, responseFunc) {
    $.ajax({
        url: url, type: typ, data: getpars, dataType: responseType, success: responseFunc, statuscode: {
            404: function () {
                alert('Response not found');
            }
        }
    });
}

function loadUser(cate) {
    var data = {}; data.cate = "load";
    ajax("/admin", data, "GET", "json", function (res) {
        if (res.length != 0) {
            switch (cate) {
                case 'setContent':
                    setLoadedUser(res); break;
                default:
            }
        } else {
            $("#registeredNurses").html("");
        }
    });
}
function setLoadedUser(loadeduser) {
    var users = "";
    if (loadeduser.length != 0) {
        for (var i = 0; i < loadeduser.length; i++) {
            var passdata = { cate: 'setContent', reference: loadeduser[i].uid, names: loadeduser[i].names, phone: loadeduser[i].phone, regdate: loadeduser[i].regdate };
            users += "<tr>"
                + "<td>" + (parseInt(i) + 1) + "</td>"
                + "<td>" + loadeduser[i].names + "</td>"
                + "<td>" + loadeduser[i].phone + "</td>"
                + "<td>" + loadeduser[i].regdate.substring(0, 16) + "</td>"
                + "<td><a href='/admin/" + loadeduser[i].id + "' class='btn btn-warning'>Edit</a>"
                + "<a href='delete/" + loadeduser[i].id + "' class='btn btn-danger'>Delete</a></td>"

                + "</tr>";
        }
    } else {
        users += "<tr>"
            + "<td colspan='10'><center>No Users Found</center></td></tr>"
    }
    $("#registeredNurses").html(users);
}

function setEditNurseFormData(obj){
    $("#nurseId").val(obj.getAttribute('data-id'));
    $("#names").val(obj.getAttribute('data-name'));
    $("#phone").val(obj.getAttribute('data-phone'));
    $("#formRegNurse").attr('action','/nurse/'+parseInt(obj.getAttribute('data-id')));
}

function searchStudentByRegno(str, cate) {
    switch (cate) {
        case 'textbox':
            ajax("/student/" + str, {}, "GET", "json", (res) => setStudentFormData(res));
            break;
        case 'tabular':
            ajax("/student/" + str, {}, "GET", "json",(res) => setStudentInfo(res));
            break;
        default: ''; break;
    }
}
function setStudentInfo(obj) {
    var data = ''
    for (let i = 0; i < obj.length; i++) {
        data += "<tr>"
            + "<td>" + (parseInt(i) + 1) + "</td>"
            + "<td>" + obj[i].names + "</td>"
            + "<td>" + obj[i].regno + "</td>"
            + "<td>" + obj[i].phone + "</td>"
            + "<td>" + obj[i].insurance_type + "</td>"
            + "<td>" + obj[i].insurance_number + "</td>"
            + "<td>" + obj[i].regdate.substring(0, 16) + "</td>"
    }
    $("#registeredStudents").html(data);
}
function setStudentFormData(res) {
    if (res.length > 0) {
        $("#names").val(res[0].names);
        $("#studentId").val(res[0].id);
    }
}
//medication

function setAddMedicationFormData(id, name) {
    $("#divAddMedicationQuantity").show();
    $("#divRegMedication").hide();
    $("#addMedicationId").attr('value', id);
    $("#addMedicationNames").attr('value', name);
}
function addMedicationQuantity() {
    ajax("/medication/add/" + $("#addMedicationId").val(), { quantity: $("#addMedicationQuantity").val(), batch: $("#medBathNo").val(), expiry: $("#medExpiryDate").val(), }, "POST", "text", function (res) {
        if (res == 'ok') {
            $("#regAddMedicationResponse").html('Medication added succesful');
        }
    });
}
//prescription
function setRowSelection(obj, tbody) {
    var trs = document.querySelector(tbody).getElementsByTagName('tr');
    for (let i = 0; i < trs.length; i++) {
        trs[i].removeAttribute('style');
    }
    obj.setAttribute('style', 'background-color:rgba(120,222,211,0.2)');
}
function setPrescriptionFormData(consultationId, name) {
    $("#prescribeConsultationId").attr('value', consultationId);
    $("#prescribeName").attr('value', name);
    $("#formPrescription").show();
    $("#formConsultation").hide();
}
function loadMedicationCombo() {
    var data = '';
    // $("#selMedication").html(data);
    ajax("/medications", { data: 'json' }, "GET", "json", function (res) {
        for (let i = 0; i < res.length; i++) {
            data += "<option value='" + res[i].id + "'>" + res[i].names + "(" + res[i].available_stock + ")</option>";
        }

        $("#selMedication").html(data);
    });
    console.log(data);
}
function registerPrescription(){
    ajax("/prescribe", { consultationId: $("#prescribeConsultationId").val(),medicationId: $("#selMedication").val(),quantity: $("#quantity").val(),condition: $("#condition").val(), }, "POST", "text", function (res) {
        if(res=='ok'){
            $("#regPrescriptionResponse").html("Patient given medication recorded");
            $("#quantity").val('');
            $("#condition").val('');
        }
    });
}


function setEditConsultationFormData(obj){
    $("#regno").val(obj.getAttribute('data-regno'));
    $("#names").val(obj.getAttribute('data-name'));
    $("#studentId").val(obj.getAttribute('data-studentid'));
    $("#height").val(obj.getAttribute('data-height'));
    $("#weight").val(obj.getAttribute('data-weight'));
    $("#symptoms").val(obj.getAttribute('data-symptoms'));

    $("#formConsultation").attr('action','/consultation/'+parseInt(obj.getAttribute('data-id')));
}

function setEditMedicationFormData(obj){
    $("#names").val(obj.getAttribute('data-name'));
    $("#description").val(obj.getAttribute('data-description'));
    $("#unit").val(obj.getAttribute('data-unit'));
    $("#quantity").val(obj.getAttribute('data-quantity'));


    $("#formMedication").attr('action','/medication/'+parseInt(obj.getAttribute('data-id')));
}
function searchPrescription(str){
    ajax("/consultation/"+str, {}, "GET", "json", function (obj) {
        var data = '';
        for(let i =0;i<obj.length;i++){
            data += "<tr>"
            + "<td>" + (parseInt(i) + 1) + "</td>"
            + "<td>" + obj[i].names + "</td>"
            + "<td>" + obj[i].regno + "</td>"
            + "<td>" + obj[i].regdate.substring(0, 16) + "</td></tr>";
        }
        if(data==''){
            data = "<tr><td colspan='4'><center>No medication history of <b>"+str+"</b> found.</center></th></tr>";
        }
        $("#searchPrescriptionBody").html(data);
    });
}
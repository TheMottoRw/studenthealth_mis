
$("#btnCloseAddMedicationQuantity").click(function (e) {
    e.preventDefault();
    $("#divAddMedicationQuantity").hide();
    $("#divRegMedication").show();
})
$("#btnAddMedication").click(function (e) {
    e.preventDefault();
    addMedicationQuantity();
})

$("#btnCloseMedicationGivenForm").click(function (e) {
    e.preventDefault();
    $("#formConsultation").show();
    $("#formPrescription").hide();
})

$("#btnRegMedicationGiven").click(function (e) {
    e.preventDefault();
    registerPrescription();
})
$("#btnResetConsultationForm").click(function (e) {
    $("#formConsultation").attr("action", '/consultations');
})
$("#btnResetMedicationForm").click(function (e) {
    $("#formMedication").attr('action', '/medications');
});
function autoLoad() {
    var urlArr = document.URL.split('/');
    urlArr.shift();
    urlArr.shift();
    urlArr.shift();
    console.log(urlArr.join('/'))
    switch (urlArr.join('/')) {
        case 'v/':
            loadUser('setContent'); break;
        case 'v/consultation':
            loadMedicationCombo();
            $("#regno").blur(function (e) {
                e.preventDefault();
                if ($(this).val().length > 5) {
                    searchStudentByRegno($(this).val(), 'textbox');
                }

            });
            break;
        case 'v/stdopenlink':
            $("#regno").blur(function (e) {
                e.preventDefault();
                if ($(this).val().length > 5) {
                    searchStudentByRegno($(this).val(), 'tabular');
                }

            });
            break;
        case 'v/search':
            $("#searchPrescription").keyup(function (e) {
                console.log($(this).val());
                if ($(this).val().length >= 9) {
                    searchPrescription($(this).val());
                }
            });
            break;
        case 'v/medication':
            $("#medExpiryDate").datepicker(); break;
        default:
    }

}
autoLoad();
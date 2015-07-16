/**
 * Created by darwright on 7/14/15.
 */
//unhide the shipping address table
function check() {
    if (document.getElementById("shipequalbill").checked === true){
        $("tr.hidden").show().prop('required',true);
        //$("input").prop('required',true);
        $('td[name=shipAddress2]').prop('required',false);
        //$('td[name=tcol1]')
    }
    else if (document.getElementById("shipequalbill").checked === false){
        $("tr.hidden").hide();
    }
}

function is_email(email){
    var emailReg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$/;
    return emailReg.test(email);
    }

function validateForm() {
    //document.loginForm.username.value;
    var email = document.userInfo.email1.value;
    var email2 = document.userInfo.email2.value;
    if (email === email2){
        is_email()
    }
    if (email !== email2){
        alert("Email addresses must match!")
    }
    var zip = document.userInfo.zip.value;

}
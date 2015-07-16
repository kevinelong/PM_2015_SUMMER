/**
 * Created by darwright on 7/14/15.
 */
//unhide the shipping address table
function check() {
    if (document.getElementById("shipequalbill").checked === true){
        $("tr.hidden").show();
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
    var email = document.getElementById("email1");
    var email2 = document.getElementById("email2");
    if (email === email2){
        is_email()
    }
    if (email !== email2){
        alert("Email addresses must match!")
    }
}
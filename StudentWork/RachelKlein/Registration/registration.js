/**
 * Created by rachel on 7/14/15.
 */

function checkEmail() {
    var email = document.registrationForm.email.value;
    var emailAgain = document.registrationForm.email2.value;
    if (email != emailAgain) {
        alert("Make sure your email is the same in both fields.");
        return false;
    }
    return true;
}

function copyAddress(form) {
    if (form.shipping_same.checked === true) {
        form.shipping_address.value = form.billing_address.value;
    }
}
/**
 * Created by stephen on 7/14/15.
 */








var users = { };

function vallidateFormInput() {
    var username = document.loginForm.username.value;
    var billingAddress = document.loginForm.password.value;
    var maillingAddress =document.loginForm.maillingAddress.value;
    var emailAddress =document.loginForm.emailAddress.value;
    var emailAddressResubmit =document.loginForm.emailAddressResubmit.value;
    var password =document.loginForm.password.value;



    if (user[emailAddress]!==emailAddressResubmit) {
        alert('The email addresses that you entered do not match!!!');
        return false;
    }
    return true;

}
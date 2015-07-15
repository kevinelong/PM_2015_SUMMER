function validateForm() {
    var fullName = document.billingForm.fullName.value;
    var email1 = document.billingForm.email1.value;
    var email2 = document.billingForm.email2.value;
    var billingAddress = document.billingForm.billingAddress.value;
    var shipToBilling = document.billingForm.shipToBilling.checked;
    var mailingAddress = document.billingForm.mailingAddress.value;
    if (!fullName) {
        // full name is required
        alert('Full name is required');
        return false;
    } else if (!email1) {
        // email address is required
        alert('Email address is required');
        return false;
    } else if (!billingAddress) {
        // billing address is required
        alert('Billing address is required');
        return false;
    } else if (email1 !== email2) {
        // email addresses do not match
        alert('Email addresses do not match');
        return false;
    } else if (!shipToBilling && !mailingAddress) {
        // if they do not want to ship to the billing address, then mailing address is required
        alert('Mailing address is required');
        return false;
    }
    return true;
}
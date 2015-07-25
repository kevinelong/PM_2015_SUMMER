function attachCheckboxHandlers() {
    var el = document.getElementById('itemChoice');
    var tops = el.getElementsByTagName('input');
    for (var i=0, len=tops.length; i<len; i++) {
        if ( tops[i].type === 'checkbox' ) {
            tops[i].onclick = updateTotal;
        }
    }
}

function updateTotal() {
    var form = this.form;
    var val = parseFloat( form.elements['total'].value );
    if ( this.checked ) {
        val += parseFloat(this.value);
    } else {
        val -= parseFloat(this.value);
    }

    // format val with correct number of decimal places
    // and use it to update value of total text box
    form.elements['total'].value = formatDecimal(val);
}

// format val to n number of decimal places
// modified version of Danny Goodman's (JS Bible)
function formatDecimal(val, n) {
    n = n || 2;
    var str = "" + Math.round ( parseFloat(val) * Math.pow(10, n) );
    while (str.length <= n) {
        str = "0" + str;
    }
    var pt = str.length - n;
    return str.slice(0,pt) + "." + str.slice(pt);
}
attachCheckboxHandlers();
//Main Page

//Shopping List


//function attachCheckboxHandlers() {
//    var el = document.getElementById('itemChoice');
//    var items = el.getElementsByTagName('input');
//    for (var i = 0, len = items.length; i < len; i++) {
//        if (items[i].type === 'checkbox') {
//            items[i].onclick = updateTotal;
//        }
//    }
//}
//
//function updateTotal() {
//    var form = this.form;
//    var val = parseFloat(form['total'].value);
//    if (this.checked) {
//        val += parseFloat(this.value);
//    } else {
//        val -= parseFloat(this.value);
//    }
//
//    // format val with correct number of decimal places
//    // and use it to update value of total text box
//    form.elements['total'].value = formatDecimal(val);
//}
//
////format val to n number of decimal places
////modified version of Danny Goodman's (JS Bible)
//function formatDecimal(val, n) {
//    n = n || 2;
//    var str = "" + Math.round(parseFloat(val) * Math.pow(10, n));
//    while (str.length <= n) {
//        str = "0" + str;
//    }
//    var pt = str.length - n;
//    return str.slice(0, pt) + "." + str.slice(pt);
//}
//
//attachCheckboxHandlers();

var cart = [];
var total = 0;


var addItems = document.getElementsByClassName("addCart");
    for (var i=0; i<addItems.length; i++){
        addItems[i].addEventListener('click', function(){
            var item = this.id;
            var value = parseInt(this.value * 100);
            total += value;
            cart.push(item);
            console.log(total);
        }, false);
    }

var removeItems = document.getElementsByClassName("removeCart");
    for (var i=0; i<removeItems.length; i++){
        removeItems[i].addEventListener('click', function(){
            var item = this.id;
            var index = cart.indexOf(item);
            console.log(item, index);
            if (cart.indexOf(item) !== -1){
                cart.splice(cart.indexOf(item), 1);
                var value = parseInt(this.value * 100);
                total -= value;
            }
            console.log(total);
        }, false);
    }

function checkOut() {
    console.log(cart);
    //window.open("checkout.html");
    var html = "<ol>";
    var finalTotal = "<p>" + checkOutTotal() + "</p>";
    for (var i=0; i<cart.length; i++){
        html += "<li>" + cart[i] + "</li>";
    }
    html += "</ol>";
    $("#cartItems").append(html, finalTotal);
    console.log(html);
}

function checkOutTotal() {
    total = "$" + total / 100;
    return total;
}



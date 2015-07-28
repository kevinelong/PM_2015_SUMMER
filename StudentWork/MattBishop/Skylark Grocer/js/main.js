//Main Page

//Shopping List
$(document).ready(function(){



    function attachCheckboxHandlers() {
        var el = document.getElementById('itemChoice');
        var items = el.getElementsByTagName('input');
        for (var i = 0, len = items.length; i < len; i++) {
            if (items[i].type === 'checkbox') {
                items[i].onclick = updateTotal;
            }
        }
    }

    function updateTotal() {
        var form = this.form;
        var val = parseFloat(form.elements['total'].value);
        if (this.checked) {
            val += parseFloat(this.value);
        } else {
            val -= parseFloat(this.value);
        }

        // format val with correct number of decimal places
        // and use it to update value of total text box
        form.elements['total'].value = formatDecimal(val);
    }

 //format val to n number of decimal places
 //modified version of Danny Goodman's (JS Bible)
    function formatDecimal(val, n) {
        n = n || 2;
        var str = "" + Math.round(parseFloat(val) * Math.pow(10, n));
        while (str.length <= n) {
            str = "0" + str;
        }
        var pt = str.length - n;
        return str.slice(0, pt) + "." + str.slice(pt);
    }

    attachCheckboxHandlers();

    var cart = [];

     $("#filet").change(function () {
        var item = $("#filet").next().text();
        cart.push(item);
        console.log(cart);
    });

    $("#cheese").change(function () {
        var item = $("#cheese").next().text();
        cart.push(item);
        console.log(cart);
    });

     $("#eggs").change(function () {
        var item = $("#eggs").next().text();
        cart.push(item);
        console.log(cart);
    });

    $("#bread").change(function () {
        var item = $("#bread").next().text();
        cart.push(item);
        console.log(cart);
    });

    $("#green_beans").change(function () {
        var item = $("#green_beans").next().text();
        cart.push(item);
        console.log(cart);
    });

    $("#raspberries").change(function () {
        var item = $("#raspberries").next().text();
        cart.push(item);
        console.log(cart);
    });

    $("#chocolate").change(function () {
        var item = $("#chocolate").next().text();
        cart.push(item);
        console.log(cart);
    });

    $("#coffee").change(function () {
        var item = $("#coffee").next().text();
        cart.push(item);
        console.log(cart);
    });

    $("#wine").change(function () {
        var item = $("#wine").next().text();
        cart.push(item);
        console.log(cart);
    });

    });

function checkOut() {
        window.open("checkout.html");
    }




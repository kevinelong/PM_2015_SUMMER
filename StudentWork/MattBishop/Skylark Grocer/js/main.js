
/**************************************
PAGE: SHOPPING
**************************************/

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

/**************************************
PAGE: RECIPES
**************************************/


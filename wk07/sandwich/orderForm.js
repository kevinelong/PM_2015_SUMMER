var mySandwich = {
    breadPrice: 1,
    meatPrice: 5,
    veggiesPrice: 2,
    getTotalPrice: function() {
        return this.breadPrice + this.meatPrice + this.veggiesPrice;
    }
};

function calculatePrice(form) {
    $('.price').slideDown(10000);
}

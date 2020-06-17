/**
 * Created by rachel on 7/20/15.
 */


$("#spam-button").on('click', function (e) {
    $("li").each(function() {
        $(this).text('Spammity spam');
    });
});

$("#order-button").on('click', function (e) {
    var numberOfItems = $('.selected').length;
    var order = "Your order is: ";
    $('.selected').each(function() {
        order += $(this).text() + ", ";
        });
    order += "and Spam.";
    $('#order-display').val(order);
});

$("li").on("click", function (e) {

    if (!$(this).hasClass("selected")) {
        $(this).animate({
            backgroundPositionLeft: '+=80',
            fontSize: '+=8'
            }, 500
        )
    }
    $(this).removeClass();
    $(this).addClass("selected");

});
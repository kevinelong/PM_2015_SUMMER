/**
 * Created by rachel on 7/20/15.
 */


$("#spam-button").on('click', function (e) {
    var entreeList = $('#entrees').text();
    console.log("entreeList");
});

$("li").on("click", function (e) {

    if ($(this).hasClass("unselected")) {
        $(this).fadeOut(1000).fadeIn(1000);
    }
    $(this).className = "selected";
});
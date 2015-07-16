/**
 * Created by rachel on 7/10/15.
 */

$(document).ready(function () {

    var shoppingList = ['this', 'that', 'the other thing', 'more stuff', 'where will it end', 'baubles', 'trinkets', 'etc', 'and of course pickles'];

    for (var i = 0; i < shoppingList.length; i++) {
        $("#test").append('<div class="container list">' + shoppingList[i] + '</div>');
    }

    $(".container").on('click', function (e) {
        if ($(this).hasClass("list")) {
            $(this).fadeOut(1000, function(){
                $(this).css("text-decoration", "line-through");
            }).fadeIn(1000);
            $(this).removeClass("list");
        }
    });

    $('#mybutton').click(function() {
    location.reload();

    });

    $(".default-button").on('click', function (e) {
        if (!$("div").hasClass("list")) {
                $(this).css("text-decoration", "");
            }
        });

    //var text = $("#item").val();
    //console.log(text);

    //$("test").append("item");

    //$("#addstuff").submit(function (e) {
    //   shoppingList.append($this.val());
    //    console.log("Hi!");
    //});



});


/**
 * Created by darwright on 7/13/15.
 */

var shoppingList = ['eggs', 'milk', 'yogurt', 'turkey', 'corn', 'cereal']

for (var i = 0; i < shoppingList.length; i++) {
    document.write('<div class="list" clicked="none" style="opacity: 1" ' + shoppingList[i] + '">' + shoppingList[i] + '</div>');
}

$('div').on('click', function() {
    if($(this).css('opacity') == "1" && $(this).attr('clicked') === "none"){
        $(this).fadeOut("slow", function(){
            $(this).css({display: "", "text-decoration": "line-through"});
        });
        $(this).attr("clicked", "first");
        $(this).fadeIn("slow");
    }
});

$('div').mouseover(function() {
    $(this).css({"background-color": "lightcyan", "color": "black"});
});


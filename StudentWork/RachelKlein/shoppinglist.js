/**
 * Created by rachel on 7/10/15.
 */

var shoppingList = ['this', 'that', 'the other thing', 'more stuff', 'where will it end', 'baubles', 'trinkets', 'etc', 'and of course pickles'];

for (var i = 0; i < shoppingList.length; i++) {
    document.write('<div class="container">' + shoppingList[i] + '</div>');
}

$('div').on('click', function(e) {
    $(this).fadeOut(1000);
}
);

$('button').on('click', function(e) {
    $('div').fadeIn(500);
});
var myItems = ['carrots', 'celery', 'flour', 'cereal', 'milk', 'paper towels'];
var openTag = '<p class="clickable">';
var closeTag = '<span class="glyphicon glyphicon-remove"></span></p>';


for (var i = 0; i < myItems.length; i++) {
    document.write(openTag + myItems[i] + closeTag);
}

// item purchased
$('p').on('click', function(e) {
    if ($(this).hasClass('clickable')) {
        $(this).fadeOut(1300, function () {
            $(this).css('text-decoration', 'line-through');
            $(this).find('span').hide();
        }).fadeIn('slow');
        $(this).removeClass();
    }
});

// dismiss by clicking the x
$('span').on('click', function() {
   $(this).parent().fadeOut(1000);
    return false; // prevents also clicking the parent p tag
});

// reset
$('button').on('click', function(e) {
    $('p').each(function(index){
        if ($(this).css('text-decoration') === 'line-through') {
            $(this).hide();
            $(this).css('text-decoration', '');
            $(this).find('span').show();
            $(this).fadeIn('slow');
        }
        $(this).attr('class', 'clickable');
        $(this).show();
    });

});
var myItems = ['carrots', 'celery', 'flour', 'cereal', 'milk', 'paper towels'];

for (var i = 0; i < myItems.length; i++) {
    document.write('<p>' + myItems[i] + '</p>');
}

$('p').on('click', function(e) {
    $(this).fadeOut(1300);
});

$('button').on('click', function(e) {
    $('p').fadeIn(500);
});
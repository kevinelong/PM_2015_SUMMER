$(document).ready(function() {
    $('li').on('click', function() {
        console.log('One click!');
        if ($(this).parent().attr('id') === 'available' ) {
            var id = $(this).attr('id');
            $('#ordered').append('<li id=new' + id + '>' + $(this).text() + '</li>');
            id = '#' + id;
            console.log('click from left', id);
            $(id).remove();
            }
        else if ($(this).parent().attr('id') === 'ordered' ){
            var id = $(this).attr('id');
            console.log('click on the right side');
            $('#available').append('<li id=old' + id + '>' + $(this).text() + '</li>');
            id = '#' + id;
            console.log('click from right', id);
            $(id).remove();
        }

    });



});

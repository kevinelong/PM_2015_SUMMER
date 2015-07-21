$(document).ready(function() {
    //get element by iD, and then make a click function for it? maybe?

    //$('li').on('click', function() {
    //    console.log('One click!');
    //    var par = $(this).parent().attr('id');
    //    console.log(par);
    //    if ($(this).parent().attr('id') === 'available' ) {
    //        var id = $(this).attr('id');
    //        $('#ordered').append('<li  class="item" id=new' + id + '>' + $(this).text() + '</li>');
    //        id = '#' + id;
    //        console.log('click from left', id);
    //        $(id).remove();
    //        }
    //    else if ($(this).parent().attr('id') === 'ordered' ){
    //        var id = $(this).attr('id');
    //        console.log('click on the right side');
    //        $('#available').append('<li  class="item" id=old' + id + '>' + $(this).text() + '</li>');
    //        id = '#' + id;
    //        console.log('click from right', id);
    //        $(id).remove();
    //    }
    //});

    $('#menu').on('click', function (event) {
        var target = $(event.target);
        if (target.hasClass('item')) {
            var id = target.attr('id');
            if (target.parent().attr('id') === 'available' ) {
                $('#ordered').append('<li  class="item" id=new' + id + '>' + target.text() + '</li>');
                id = '#' + id;
                $(id).remove();
            } //end of first nest if
            else if (target.parent().attr('id') === 'ordered' ){
                $('#available').append('<li  class="item" id=old' + id + '>' + target.text() + '</li>');
                id = '#' + id;
                $(id).remove();
            } //end of second nest if
        } // end first IF
    }); //end of doc ready





}); // end of doc ready

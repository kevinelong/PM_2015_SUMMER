$(document).ready(function() {
    $('#menu').on('click', function (event) {
        var target = $(event.target);
        if (target.hasClass('item')) {
            target.addClass('clicked');
            var id = target.attr('id');
            if (target.parent().attr('id') === 'available' ) {
                target.animate({
                    opacity: 0.0,
                    paddingRight: '+=80',
                    paddingTop: '+=200'
                }, 500, function() {
                    $('#ordered').append('<li  class="item" id=new' + id + '>' + target.text() + '</li>');
                    id = '#' + id;
                    $(id).remove();
                    }); // end of animate

            } //end of first nest if
            else if (target.parent().attr('id') === 'ordered' ){
                target.animate({
                    opacity: 0.0,
                    paddingRight: '+=80',
                    paddingTop: '+=200'
                }, 500, function() {
                    $('#available').append('<li  class="item" id=old' + id + '>' + target.text() + '</li>');
                    id = '#' + id;
                    $(id).remove();
                }); //end of animate
            } //end of second nest if
        } // end first IF
    }); //end of doc ready
}); // end of doc ready

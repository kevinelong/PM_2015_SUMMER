/**
 * Created by sophiaosintsev on 7/22/15.
 */
$(document).ready(function() {

    function close_accordion_section() {
        $('.accordion .accordion-section-title').removeClass('active');
        $('.accordion .accordion-section-content').slideUp(300).removeClass('open');
    }

    $('.accordion-section-title').click(function(e) {

        var currentAttrValue = $(this).attr('href');

        if($(e.target).is('.active')) {
            close_accordion_section();
        }else {
            close_accordion_section();

            $(this).addClass('active');
            $('.accordion ' + currentAttrValue).slideDown(300).addClass('open');
        }

        e.preventDefault();
    });


    $("button#addItem").on("click", function () {
        var addItem = $("#textbox").val();
        var select = $("#aisleSelect").val();
        var listItem = $("#" + select + "-list");
        console.log(listItem)
        if (listItem) {
            listItem.append("<div id='list'><li class='" + select + "'> " + addItem + "</li></div>");
        }
        if (listItem != undefined) {
            $("#categories").prepend(listItem.parent());
            $(listItem.parent()).show();
        }

        $("#textbox").keypress(function (e) {
            if (e.which == 13) {
                $("button#addItem").submit();
            }
        });

        $("#textbox").val("");

        if (addItem.length == 0) {
            alert('Please enter an item!');
        }

        $('#controls').fadeIn();

    });

    $(document).on('click', 'li', function () {
        $(this).toggleClass('complete');
    });

    $(document).on('dblclick', 'li', function () {
        $(this).remove();
    });

    $('button#clearAllItems').on('click', function () {
        $('div li').remove();
        $('#categories').remove();
        $('#controls').fadeOut();
    });
});


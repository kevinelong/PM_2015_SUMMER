$(document).ready(function(){

    //  main button click function
    $('button#addButton').on('click', function(){

        // create the new li from the form input
        var task = $("#textbox").val();
        $('<div><input id="toDoList" type="checkbox">' + task + '</input></div>').appendTo('.list');

        // clear form when button is pressed
        $("#textbox").val("");

        // Alert if the form in submitted empty
        if (task.length == 0) {
            alert("Please enter a task");
        };

    //    // makes other controls fade in when first task is created
    //    $('#controls').fadeIn();
    //    $('.task-headline').fadeIn();
    //});

    // mark as complete
    $(document).on('click','div',function(){
        $(this).toggleClass('complete');
    });

    // double click to remove
    $(document).on('dblclick','div',function(){
        $(this).remove();
    });

    //// Clear all tasks button
    //$('button#clear-all-tasks').on('click', function(){
    //    $('#task-list li').remove();
    //    $('.task-headline').fadeOut();
    //    $('#controls').fadeOut();
    //    $('.nothing-message').show('fast');
    //});
});


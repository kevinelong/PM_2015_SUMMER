/**
 * Created by stephen on 7/20/15.
 */
//$(':header').addClass('headline');
//$('li:lt(3)').hide()



//$(function() {
//   $('li').on('click', function(){
//      $('this').animate({
//          opacity: 0.0,
//          paddingLeft: '+=80'
//      },500,function(){
//      $(this).remove();
//      });
//   });
//
//});


$(function(){
    var $newItemButton = $('#newItemButton');
    var $newItemForm = $("#newItemForm");
    var $textInput = $("#text:Input");

    $newItemButton.show();
    $newItemForm.hide();

    $("#showForm").on("click", function () {
        $newItemButton.hide();
        $newItemForm.show();

    });

    $newItemForm.on('submit', function(e)){
        e.preventDefault();
        var newText = $("input:text").val();
        $("li:last").after("<li>" + newText + "</li">);
        $newItemForm.hide();
        $newItemButton.show();
        $textInput.val("");
         });





});
$(document).ready(function(){
 $("#baking1, #traveling1, #restoring1, #ocean1, #russian1, #duy1").hide();


  $("#baking").hover(function(){
    $("#baking1").toggle();
}); 

  $("#traveling").hover(function(){
    $("#traveling1").toggle();
}); 


  $("#restoring").hover(function(){
    $("#restoring1").toggle();
}); 

  $("#ocean").hover(function(){
    $("#ocean1").toggle();
}); 

  $("#russian").hover(function(){
    $("#russian1").toggle();
}); 

  $("#duy").hover(function(){
    $("#duy1").toggle();
});

});
/**
 * Created by darwright on 7/14/15.
 */
//unhide the shipping address table


function check() {
    if (document.getElementById("shipequalbill").checked === true){
        console.log('box is checked!');
        $("tr.hidden").show();
    }
    else if (document.getElementById("shipequalbill").checked === false){
        console.log('box is NOT checked!');
        $("tr.hidden").hide();
    }

}

//function uncheck() {
//    document.getElementById("shipequalbill").checked = false;
//    console.log('box is NOT checked!');
//}


//$(document).ready(function() {
//    if ($("#shipequalbill").is(':checked'))
//        $("tr.hidden").show();  // checked  //verified these commands in console hide/show the right fields
//    console.log('show!;');
//    if (!$("#shipequalbill").is(':checked'))
//    $("tr.hidden").hide();  // unchecked
//    console.log('HIDE!');
//});


//if(document.getElementById('#shipequalbill').checked) {
//    $(".rowClass").show();
//} else {
//    $(".rowClass").hide();
//}

//$('#shipequalbill').on('click', function() {
//    if($('#shipequalbill') === checked ){
//        $('.rowClass').css(display, 'block');
//        console.log('checked!');
//    }
//});


//$(document).ready(function() {
//    if ($('#shipequalbill') === 'checked') {
//        $('#shipequalbill').hide();
//        };
//    if ($('#shipequalbill') === 'unchecked') {
//        $('#shipequalbill').show();
//        };
//    });



//$("input:checkbox:not(:checked)").each(function() {
//    $('#shipequalbill').toggle();
//});
//
//$("input:checkbox").click(function(){
//    $('#shipequalbill').hide();
//});

//$("#shipequalbill").change(function(){
//    $("#shippingAddress tr.hide").toggle(!this.checked);
//    console.log('argh.')
//});


//
//if($("#shipequalbill").is(":checked")){
//
//    $("#shippingAddress tr.hide").hide();
//
//}else{
//
//    $("#shippingAddress tr.hide").show();
//}
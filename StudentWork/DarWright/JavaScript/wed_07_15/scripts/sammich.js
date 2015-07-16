/**
 * Created by darwright on 7/15/15.
 */
//

function calcTotal(){
    var total = 0;
    $('.ingredients tr').each(function() {
        var thisClassdata = {};
        thisClassdata.ClassName = $(this).attr('class');
        thisClassdata.Values = [];
        $(this).find('input:checked').each(function() {
            thisClassdata.Values.push($(this).attr('value'));
            console.log('classvalue: ', thisClassdata.Values);
            total += Number(thisClassdata.Values);
            //total += Number(thisClassdata.Values.push($(this).attr('value')));
            //console.log('total first:', total);

            //for ( var i = 0; i < thisClassdata.length; i++){
            //    total += thisClassdata[i] << 0;
            //}
            console.log('total in each:', total);
        });

        //for (var i = 0; i < thisClassdata.length; i++){
        //    if (thisClassdata[i]){
        //        console.log('value: ', thisClassdata[i]);
        //        total += Number(thisClassdata[i]);
        //        console.log('total in each:', total);
        //    }
        //}

        //for ( var i = 0; i < thisClassdata.length; i++){
        //    total += Number(thisClassdata[i]);
        //}
        //console.log('classvalue: ', thisClassdata.Values);
        //console.log('total in each:', total);

    });

    console.log('total:', total);


    console.log('total:', total);
}



//var thisClassData = {};
//thisClassData.ClassName = $(this).attr('class');
//thisClassData.Values = [];
//$(this).find('input:checked').each(function() {
//    thisClassData.Values.push($(this).attr('value'));
//});

//function calcTotal(){
//    $('.ingredients tr').each(function() {
//        $(this).find('td input:checked').each(fucntion(){
//
//        });
//    });
//}
//
//function calcTotal() {
//
//    var total = 0;
//    $('.ingredients tr').each(function () {
//        //processing this row
//        //how to process each cell(table td) where there is checkbox
//        $(this).find('td input:checked').each(function () {
//            var p = $(this).find('td .price');
//            //$(this).find(".customerIDCell").html();
//            console.log(p);
//            total += p;
//            console.log(total);
//            // it is checked, your code here...
//        });
//    });
//    alert(total)
//    return total
//}



//function calcTotal(price){
//    //var subtot = document.orderform.ingredients.subtotal.value;
//    //var subtot = document.getElementsByName("subtotal");
//    //var rowid = "#" + name;
//    //var r = $("#testing #row2").text();
//    //var subtot = $(rowid).text();
//    //var subtot = document.orderform.ingredients.subtotal.value;
//    //console.log(subtot);
//    //subtot += price;
//
//    //console.log($(this).price);
//    //subtot += $(this).price;
//    //console.log(subtot);
//    //return ("$" + subtot)
//
//    var subtot = 0;
//    subtot += price;
//    console.log(subtot);
//    return subtot
//}
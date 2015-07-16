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
            //console.log('classvalue: ', thisClassdata.Values);
            total += Number(thisClassdata.Values);
            //console.log('total in each:', total);
        });
    });
    return total
}
//}
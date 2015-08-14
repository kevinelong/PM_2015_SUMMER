/**
 * Created by darwright on 7/10/15.
 */
console.log('dar');

//var aStingRay = ["cat", "dog", "mouse", "fish"];
//bad ways to use arryas:
//var aRayZing = Array(1, 2, 3, 4);
//var bRay = new Array(1 ,2 ,3 ,4 );
//
//console.log(aStingRay);
//console.log(aStingRay[aStingRay.length-1])
//
//aStingRay.push('hamster');
//console.log(aStingRay);
//aStingRay.unshift('snake');
//console.log(aStingRay);
//aStingRay.pop();
//console.log(aStingRay);
//aStingRay.slice(1, 3);
//console.log(aStingRay);
//aStingRay.join();
//aStingRay.lastIndexOf();

// ready for some loops
//
//for (var i = 20; i <= 50; i+=2){
//    console.log(i)
//}
//var i = 20;
//while (i <= 50){
//    console.log(i)
//    i+=2;
//}

//
//Given an array that may have duplicates, write a function that will take that array and return one without the duplicates.
//    example: dedupper([1, 1, 2, 3]) will return [1, 2, 3]
//    example: dedupped([1, 2, 3, 1]) will return [1, 2, 3]
//    exampleL dedupped([3, 2, 3, 1]) will return [3, 2, 1]
// return the list in the same order

//
//var listc = [1, 1, 2, 3];
//var lista = [1, 2, 3, 1];
//var listb = [3, 2, 3, 1];
////var test = [];
//
//function dedupped(list){


//}

//var test = [];
//for (var i = 0; i < list.length; i++){
//    var element = list[i];
//    console.log('element is', list[i]);
//    var grrrr =  (list[i] in test);
//    console.log('can it find it?', grrrr);
//
//    if ( element === list[i]){
//        console.log('match you fuck')
//    }
//
//    if (grrrr === false) {
//        console.log('list first', list);
//        test.push(list[i]);
//
//        //list.reverse();
//        //list.pop();
//        //list.reverse();
//        //test.push(element)
//        //console.log('list after', list);
//        console.log('test after', test);
//
//    }
//    else {
//        //test.push(element);
//        console.log('test list from else', test)
//    }
//}

//var test = [];
//for (var i = 0; i < list.length; i++){
//    var element = list[i];
//    console.log('element is', element);
//    var grrrr =  (element in test);
//    console.log(grrrr);
//    if ((element in list) === false) {
//        console.log('list first', list);
//        if (element in test) {
//            console.log('test level 2', test);
//        }
//        else {
//            test.push(element);
//            console.log('test level 3', test);
//        }
//        //list.reverse();
//        //list.pop();
//        //list.reverse();
//        //test.push(element)
//        console.log('list after', list);
//        console.log('test after', test);
//
//    }
//    else {
//        test.push(element);
//        console.log('test list from else', test)
//    }
//}


//var test = [];
//for (var i = 0; i < list.length; i++){
//    console.log(list[i])
//    console.log(test)
//    if ((list[i] in test) === True){
//        console.log('found it!')
//        //continue
//    }
//    else{
//        console.log('list', list[i]);
//        test.push(list[i]);
//        console.log('test', test);
//    }
//
//}


//var obj = {a:1, b:2, c:3};
//
//for (var prop in obj) {
//    console.log("o." + prop + " = " + obj[prop]);
//}


//var numb;
//function dedupped(list){
//    for (var i = 0; i < list.length; i++){
//        var testnumb = list[i];
//        console.log('testnumber', testnumb);
//        var idx = list.indexOf(testnumb);
//        console.log('idx', idx);
//        if (idx != -1) {
//            //while (idx != -1) {
//                test.push(testnumb);
//                //idx = list.indexOf(idx + 1);
//                console.log(test);
//            //}
//        }
//    }
//}

//var indices = [];
//var array = ['a', 'b', 'a', 'c', 'a', 'd'];
//var element = 'a';
//var idx = array.indexOf(element);
//while (idx != -1) {
//    indices.push(idx);
//    idx = array.indexOf(element, idx + 1);
//}
//console.log(indices);
// [0, 2, 4]

//function dedupped(list) {
//    var result = [];
//    $.each(list, function(i, e) {
//        if ($.inArray(e, result) == -1) result.push(e);
//    });
//    return result;
//}
//
//console.log(listc);
//dedupped(listc);
//console.log(lista);
//dedupped(lista);
//console.log(listb);
//dedupped(listb);


// still fail on removing duplicates. It should not be this hard.

//


var shoppingList = ['eggs', 'milk', 'yogurt', 'turkey', 'corn', 'cereal'];

// for each item in our shopping list, display it on the webpage

for (var i = 0; i < shoppingList.length; i++){
    document.write('<div class="list" onclick="toggle_visibility(id)" style="display: block" id="' + shoppingList[i] + '">' + shoppingList[i] + '</div>');
    //document.write('<div class="list">' + '</div>');
    //document.write('<div class="list" onclick="toggle_visibility(id)">' + shoppingList[i] + '</div>');
}

function listitems() {
    //for (var i = 0; i < shoppingList.length; i++){
    //    document.write('<div class="list" onclick="toggle_visibility(id)" style="display: block" id="' + shoppingList[i] + '">' + shoppingList[i] + '</div>');
    //    //document.write('<div class="list">' + '</div>');
    //    //document.write('<div class="list" onclick="toggle_visibility(id)">' + shoppingList[i] + '</div>');
    //}
    var divs = document.getElementsByTagName("div");
    for(var i = 0; i < divs.length; i++){
        //do something to each div like
        $(".list *").filter(function(){
            $(this).css("display") = "block"};
    }
}

function toggle_visibility(id) {
    var e = document.getElementById(id);
        if(e.style.display == 'block')
        e.style.display = 'none';
    else
        e.style.display = 'block';
}



// create a webpage that lists the items in your shopping card
//give it some simple style
//when you click an itiem it disappears
// create a button that brings them all back

















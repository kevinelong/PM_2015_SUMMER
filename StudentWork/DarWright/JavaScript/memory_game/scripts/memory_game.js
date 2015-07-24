var images_array = [
    0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11
];

// Shuffles the image numbers from the array to make the images be randomly placed on the game board
Array.prototype.image_shuffle = function(){
    var i = this.length, j, temp;
    while(--i > 0){
        j = Math.floor(Math.random() * (i+1));
        temp = this[j];
        this[j] = this[i];
        this[i] = temp;
    }
};
// creates the game board, 12 spaces with unique ids
function newGame(){
    tiles_flipped = 0;
    var output = '';
    images_array.image_shuffle();
    for(var i = 0; i < images_array.length; i++){
        output += '<div><img class="pic" id="' + i + '" src="images/gonzo2.jpg" width="100%" height="100%"></div>';
    }
    document.getElementById('game_board').innerHTML = output;
}

// allows the pictures to be flipped over and if no match flips them back
var clicked_count = 0;
var clicked_id_1 = '';
var clicked_id_2 = '';
var matches = 0;
var big_click = 0;
function mainGame() {
    //console.log('clicked count is starting?', clicked_count);
    $('.pic').on('click', function() {
        if (clicked_count === 0) {
            clicked_id_1 = $(this).attr('id');
            var clicked_src_1 = "images/" + images_array[clicked_id_1] + ".jpg";
            $(this).attr('src', clicked_src_1);
            //console.log('clicked count is 0?', clicked_count);
            clicked_count +=1;
        }
        else if (clicked_count === 1) {
            clicked_id_2 = $(this).attr('id');
            var clicked_src_2 = "images/" + images_array[clicked_id_2] + ".jpg";
            $(this).attr('src', clicked_src_2);
            //console.log('clicked count is 1?', clicked_count);
            clicked_count += 1;
            //console.log('clicked count is 2?', clicked_count);
            setTimeout(flipOver, 1000);
        }
        big_click +=1;
    });
    if (matches === 12){
        alert('You won!');
        newGame();
    }


}// end of mainGame function

function flipOver() {
    //console.log('flipover!');
    //console.log('id 1:', clicked_id_1, 'id: 2', clicked_id_2);
    console.log('array 1: ', images_array[clicked_id_1], 'array 2:', images_array[clicked_id_2], 'matches: ', matches, 'big_click:', big_click);

    if (images_array[clicked_id_1] === images_array[clicked_id_2]){
        matches +=1;
        //console.log(matches);
        clicked_count = 0;

    }
    else if (images_array[clicked_id_1] !== images_array[clicked_id_2]){
        //alert('No match!');
        var cover_image_1 = "images/gonzo2.jpg";
        $('#' + clicked_id_1).attr('src', cover_image_1);
        var cover_image_2 = "images/gonzo2.jpg";
        $('#' + clicked_id_2).attr('src', cover_image_2);
        //console.log(matches);
        clicked_count = 0;
    }
    
}// end of flipOver function


$(document).ready(function() {
    mainGame();
    //setTimeout(flipOver(clicked_id_1, clicked_id_2),1000);
    //$.fn.preload = function() {
    //    this.each(function(){
    //        $('<img/>')[0].src = this;
    //    });
    //};
    //
    //$(images_array_preload).preload();
});//end of doc ready

jQuery.fn.preventDoubleClick = function() {
    $(this).on('click', function(e){
        var $el = $(this);
        if($el.data('clicked')){
            // Previously clicked, stop actions
            e.preventDefault();
            e.stopPropagation();
        }else{
            // Mark to ignore next click
            $el.data('clicked', true);
            // Unmark after 1 second
            window.setTimeout(function(){
                $el.removeData('clicked');
            }, 1000)
        }
    });
    return this;
};




var images_array_preload = [
    '<img src="images/1.jpg" width="71" height="90">', '<img src="images/2.jpg" width="71" height="90">',
    '<img src="images/3.jpg" width="71" height="90">', '<img src="images/4.jpg" width="71" height="90">',
    '<img src="images/5.jpg" width="71" height="90">', '<img src="images/6.jpg" width="71" height="90">',
    '<img src="images/7.jpg" width="71" height="90">', '<img src="images/8.jpg" width="71" height="90">',
    '<img src="images/9.jpg" width="71" height="90">', '<img src="images/10.jpg" width="71" height="90">',
    '<img src="images/11.jpg" width="71" height="90">', '<img src="images/0.jpg" width="71" height="90">'
];










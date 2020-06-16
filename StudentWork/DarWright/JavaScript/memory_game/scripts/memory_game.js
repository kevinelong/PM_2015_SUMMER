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
    clicked_count = 0;
    clicked_id_1 = '';
    clicked_id_2 = '';
    matches = 0;
    big_click = 0;
    $('#clicks').text('Clicks: ' + big_click);
    $('#total').text('Matches: ' + matches);
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
            clicked_count += 1;
            setTimeout(flipOver, 1000);
        }
        big_click +=1;
        $('#clicks').text('Clicks: ' + big_click);
    });

}// end of mainGame function
function flipOver() {
    //console.log('flipover!');
    //console.log('id 1:', clicked_id_1, 'id: 2', clicked_id_2);
    console.log('array 1: ', images_array[clicked_id_1], 'array 2:', images_array[clicked_id_2], 'matches: ', matches, 'big_click:', big_click);
    if (matches < 11) {
        if (images_array[clicked_id_1] === images_array[clicked_id_2]){
            matches +=1;
            clicked_count = 0;
            $('#total').text('Matches: ' + matches);
            $('#clicks').text('Clicks: ' + big_click);
        }
        else if (images_array[clicked_id_1] !== images_array[clicked_id_2]){
            var cover_image_1 = "images/gonzo2.jpg";
            $('#' + clicked_id_1).attr('src', cover_image_1);
            var cover_image_2 = "images/gonzo2.jpg";
            $('#' + clicked_id_2).attr('src', cover_image_2);
            clicked_count = 0;
            $('#clicks').text('Clicks: ' + big_click);
        }
    }

    if (matches >= 11){
        alert('You won!');
        newGame();

    }

}// end of flipOver function

$(document).ready(function() {
    mainGame();

    $.preloadImages = function() {
        for (var i = 0; i < arguments.length; i++) {
            $("<img />").attr("src", arguments[i]);
        }
    };
    $.preloadImages( "images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg", "images/5.jpg", "images/6.jpg",
        "images/7.jpg", "images/8.jpg", "images/9.jpg", "images/10.jpg", "images/11.jpg", "images/0.jpg");

    $('#total').text('Matches: ' + matches);
    $('#clicks').text('Clicks: ' + big_click);
});//end of doc ready








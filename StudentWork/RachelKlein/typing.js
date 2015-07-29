/**
 * Created by rachel on 7/22/15.
 */

// * Basic Functionality * //

// Create word list (10 values right now for testing purposes)

var wordList = ["orange", "cerulean", "sienna", "peach", "umber", "plum", "maroon",
    "vermillion", "goldenrod", "fern", "razzmatazz"];
// TODO: Make it so word list values on screen choose randomly from this list but do not duplicate anything that's
// already on the screen

// Display words from list on screen (randomly selected)

var listOfCurrentWords = [];

function addWord() {
    var currentWordIndex = Math.floor((Math.random() * 10) + 1);
    var currentWord = wordList[currentWordIndex];
    listOfCurrentWords.push(currentWord);
    console.log(currentWord);
    newDiv = ('<div class="' + currentWord + '">' + currentWord + '</div>');
    console.log(newDiv.className);
    $('#wordsonpage').append(newDiv);
}



var wordCounter = 0;
var wordTiming = setInterval(function() {
    wordCounter += 1;
    if(wordCounter === wordList.length){
        clearInterval(wordTiming);
}
    addWord();
}, 2000);


// Captures textbox input as user types and clears textbox when word match found in array

// Is this next line the best/clearest way to begin checking for text input?
window.onkeyup = checkText;
var inputTextValue;
function checkText(e) {
    inputTextValue = e.target.value;
    var inArray = listOfCurrentWords.indexOf(inputTextValue);
    // If word is typed correctly, any instances of that word on screen are removed
    if (inArray > -1) {
        var correctWord = $('#typing').val();
        var wordClass = '.' + correctWord;
        $(wordClass).remove();
        $('#typing').val('');
    }
}


// Compare to list of words currently on screen, return boolean of whether there's a match
// (See if I can make the entire word match, not just the end.)

// Remove word from screen if there is a match or if user didn't type it in time

// Create penalty for player if word on screen too long/hits right side of screen

// Keep score of words user typed correctly

// Listening event for reset button (other buttons also?)

// * Advanced Features * //

// Animate words to move across screen

// Set level that will affect animation speed

// Create win condition
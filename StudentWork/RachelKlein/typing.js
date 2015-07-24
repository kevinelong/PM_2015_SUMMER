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

var wordCounter = 0;
while (wordCounter < wordList.length) {
    var currentWordIndex = Math.floor((Math.random() * 10) + 1);
    var currentWord = wordList[currentWordIndex];
    console.log(currentWord);
    newDiv = ('<div>' + currentWord + '</div>');
    $('#wordsonpage').append(newDiv);
    // TODO: Figure out why class name is coming back as "undefined" - why isn't this line working?
    // Not working even for a string...
    $(newDiv).addClass(currentWord);
    console.log(newDiv.className);
    wordCounter += 1;
    // TODO: Figure out how to put a delay between words appearing. setTimeout?
}

// Capture textbox input as user types and clear textbox when word match found in array

// Is this next line the best/clearest way to begin checking for text input?
window.onkeyup = checkText;
var inputTextValue;
function checkText(e) {
    inputTextValue = e.target.value;
    var inArray = wordsOnPage.indexOf(inputTextValue);
    if (inArray > -1) {
        // TODO: Remove (most recent instance of) correct word from screen
        // This part is working - it's the assignment of class (above) that isn't.
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
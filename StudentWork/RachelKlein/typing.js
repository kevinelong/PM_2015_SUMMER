/**
 * Created by rachel on 7/22/15.
 */

// * Basic Functionality * //

// Create word list (10 values right now for testing purposes)

var wordList = ['mahogany', 'chestnut', 'melon', 'sepia', 'orange', 'copper', 'mango', 'tangerine', 'brass',
    'tumbleweed', 'sienna', 'peach', 'apricot', 'almond', 'gold', 'banana', 'sunglow', 'goldenrod', 'dandelion',
    'olive', 'lemon', 'canary', 'asparagus', 'lime', 'fern', 'shamrock', 'cerulean', 'cornflower', 'orchid', 'violet',
    'eggplant', 'cerise', 'jungle', 'pacific', 'denim', 'manatee', 'plum', 'timberwolf', 'maroon', 'vermillion',
    'razzmatazz', 'umber'];

// TODO: Make it so word list values on screen choose randomly from this list but do not duplicate anything that's
// already on the screen

// Display words from list on screen (randomly selected)

var listOfCurrentWords = [];

$('#wordsonpage')[0].style.width = window.innerWidth;
$('#wordsonpage')[0].style.height = window.innerHeight;

function addWord() {
    var currentWordIndex = Math.floor((Math.random() * wordList.length - 1) + 1);
    var currentWord = wordList[currentWordIndex];
    listOfCurrentWords.push(currentWord);
    var newDiv = document.createElement('div');
    newDiv.classList.add(currentWord);
    newDiv.innerHTML = currentWord;
    var offsetTop = Math.floor((Math.random() * 500) + 1);
    console.log(offsetTop);
    var offsetLeft = Math.floor((Math.random() * 500) + 1);
    console.log(offsetLeft);
    $(newDiv).css({position: "absolute"});
    newDiv.style.top = offsetTop + "px";
    newDiv.style.left = offsetLeft + "px";
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


// Remove word from screen if user didn't type it in time

// Create penalty for player if word on screen too long/hits right side of screen

// Keep score of words user typed correctly

// Listening event for reset button (other buttons also?)

// * Advanced Features * //

// Animate words to move across screen

// Set level that will affect animation speed

// Create win condition
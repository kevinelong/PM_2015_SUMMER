/**
 * Created by rachel on 7/22/15.
 */

// * Basic Functionality * //

// List of words to be typed

var wordList = ['mahogany', 'chestnut', 'melon', 'sepia', 'orange', 'copper', 'mango', 'tangerine', 'brass',
    'tumbleweed', 'sienna', 'peach', 'apricot', 'almond', 'gold', 'banana', 'sunglow', 'goldenrod', 'dandelion',
    'olive', 'lemon', 'canary', 'asparagus', 'lime', 'fern', 'shamrock', 'cerulean', 'cornflower', 'orchid', 'violet',
    'eggplant', 'cerise', 'jungle', 'pacific', 'denim', 'manatee', 'plum', 'timberwolf', 'maroon', 'vermillion',
    'razzmatazz', 'umber'];

// TODO: Make it so word list values on screen choose randomly from this list but do not duplicate anything that's
// already on the screen - use alreadyOnScreen variable below and compare to -1

// Display words from list on screen (randomly selected)

var listOfCurrentWords = [];

function isAlreadyOnScreen(word) {
    return listOfCurrentWords.indexOf(word);
}

function addWord() {
    var currentWordIndex = Math.floor((Math.random() * (wordList.length - 1)) + 1);
    var currentWord = wordList[currentWordIndex];
    alreadyThere = isAlreadyOnScreen(currentWord);
    //if (alreadyThere > -1) {
    //
    //}

    // Creates a new div with a class the same as the word
    // (the class will later be used to remove the word from the screen)

    listOfCurrentWords.push(currentWord);
    var newDiv = document.createElement('div');
    newDiv.classList.add(currentWord);
    newDiv.innerHTML = currentWord;

    // Creates a randomized position for each new word within the wordsOnPage div

    var offsetTop = Math.floor((Math.random() * 500) + 1);
    var offsetLeft = Math.floor((Math.random() * 500) + 1);
    $(newDiv).css({position: "absolute"});
    newDiv.style.top = offsetTop + "px";
    newDiv.style.left = offsetLeft + "px";

    // Assigns a randomly chosen color to the new word

    wordColor = chooseColor();
    $(newDiv).css({color: wordColor});

    $('#wordsonpage').append(newDiv);

    // Animates word going slowly to the right of the screen, then disappearing and being removed
    // from the array of words on the screen if it has not been typed by that point

    $(newDiv).animate({
        left: window.innerWidth
    }, 10000, function() {
        $(newDiv).remove();
        failedWord = newDiv.innerHTML;
        removeWord(failedWord);
    });

}

// Method to take a list out of the current available words (i.e. words that will give you points if you type them)
// if the word has already been typed or has reached the right part of the screen.

function removeWord(word) {
    wordIndex = listOfCurrentWords.indexOf(word);
    listOfCurrentWords.splice(wordIndex, 1);
}

// Method that randomly chooses a color for each new word.

function chooseColor() {
    // These values are based on Crayola colors, of course.
    var colorValues = ['CD4A4A', 'CC6666', 'BC5D58', 'FF5349', 'FD5E53', 'FD7C6E', 'FDBCB4', 'FF6E4A', 'FFA089',
        'EA7E5D', 'B4674D', 'A5694F', 'FF7538', 'FF7F49', 'DD9475', 'FF8243', 'FFA474', '9F8170', 'CD9575',
        'EFCDB8', 'D68A59', 'DEAA88', 'FAA76C', 'FFCFAB', 'FFBD88', 'FDD9B5', 'FFA343', 'EFDBC5', 'FFB653',
        'E7C697', 'FAE7B5', 'FFCF48', 'FCD975', 'FDDB6D', 'FCE883', 'F0E891', 'ECEABE', 'BAB86C', 'FDFC74',
        'FFFF99', 'C5E384', 'B2EC5D', '87A96B', 'A8E4A0', '1DF914', '76FF7A', '71BC78', '6DAE81', '9FE2BF',
        '1CAC78', '30BA8F', '45CEA2', '3BB08F', '1CD3A2', '17806D', '158078', '1FCECB', '78DBE2', '77DDE7',
        '80DAEB', '99EBD', '1CA9C9', '1DACD6', '9ACEEB', '1A4876', '1974D2', '2B6CC4', '1F75FE', 'C5D0E6',
        'B0B7C6', '5D76CB', 'A2ADD0', '979AAA', 'ADADD6', '7366BD', '7442C8', '7851A9', '9D81BA', '926EAE',
        'CDA4DE', '8F509D',  'C364C5', 'FB7EFD', 'FC74FD', '8E4585', 'FF1DCE', 'FF1DCE', 'FF48D0', 'E6A8D7',
        'C0448F', '6E5160', 'DD4492', 'FF43A4', 'F664AF', 'FCB4D5', 'FFBCD9', 'F75394', 'FFAACC', 'E3256B',
        'FDD7E4', 'CA3767', 'DE5D83', 'FC89AC', 'F780A1', 'C8385A', 'EE204D', 'FF496C', 'EF98AA', 'FC6C85',
        'FC2847', 'FF9BAA', 'CB4154', 'DBD7D2', 'CDC5C2', '95918C'];
    var colorIndex = Math.floor((Math.random() * (colorValues.length - 1)) + 1);
    chosenColor = "#" + colorValues[colorIndex];
    return chosenColor;
}

// Delays new words appearing on page by two seconds and stops when there are as many words as values in the list.

var wordCounter = 0;
var wordTiming = setInterval(function() {
    wordCounter += 1;
    if(wordCounter === wordList.length){
        clearInterval(wordTiming);
}
    addWord();
}, 2000);


// Captures textbox input as user types and clears textbox when word match found in array

window.onkeyup = checkText;
var inputTextValue;
var numberCorrect = 0;
function checkText(e) {
    inputTextValue = e.target.value;
    var inArray = listOfCurrentWords.indexOf(inputTextValue);
    // If word is typed correctly, any instances of that word on screen are removed
    if (inArray > -1) {
        var correctWord = $('#typing').val();
        var wordClass = '.' + correctWord;
        $(wordClass).remove();
        $('#typing').val('');
        // Augments the amount in the "words you got correct" textbox
        numberCorrect +=1;
        $('#correct').val(numberCorrect);
        removeWord(correctWord);

        // TODO: Figure out why removing the correctly typed word (and removing textbox value) isn't always working.
        // Is it just slowness due to the animation?

    }
}

// Listening event for reset button (other buttons also, to select level, etc?)

$('#reset').click(function() {
    location.reload();
});

// * Advanced Features * //

// Set level that will affect animation speed

// Create win condition

// Create penalty for player if word on screen too long/hits right side of screen
// Maybe if ANYTHING hits the right side of the screen they lose, and if they type all words that pop up they win that level?

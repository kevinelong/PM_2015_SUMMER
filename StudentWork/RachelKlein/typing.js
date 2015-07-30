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

// TODO: Break this code up into smaller functions to add color, determine position, etc.
function addWord() {
    var currentWordIndex = Math.floor((Math.random() * (wordList.length - 1)) + 1);
    var currentWord = wordList[currentWordIndex];
    listOfCurrentWords.push(currentWord);
    var newDiv = document.createElement('div');
    newDiv.classList.add(currentWord);
    newDiv.classList.add("childDiv");
    newDiv.innerHTML = currentWord;

// TODO: Make it so words don't overlap each other or the textbox/directions.
    var offsetTop = Math.floor((Math.random() * 500) + 1);
    var offsetLeft = Math.floor((Math.random() * 500) + 1);
    $(newDiv).css({position: "absolute"});
    newDiv.style.top = offsetTop + "px";
    newDiv.style.left = offsetLeft + "px";

    wordColor = chooseColor();
    $(newDiv).css({color: wordColor});

    $('#wordsonpage').append(newDiv);
}

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

// I think the syntax on this is right but how do I get it to continually animate all the child divs?
// Not working at all currently but it is also not throwing any errors.

$('.childDiv').animate({
    right: 0
}), 500, function() {
    $(this).remove();
};



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

// Listening event for reset button (other buttons also, to seletct level, etc?)

// * Advanced Features * //

// Animate words to move across screen

// Set level that will affect animation speed

// Create win condition
var wordCounter = 0;
while (wordCounter < wordList.length) {
    var currentWordIndex = Math.floor((Math.random() * 10) + 1);
    var currentWord = wordList[currentWordIndex];
    console.log(currentWord);
    newDiv = ('<div class="classname">' + currentWord + '</div>');
    $('#wordsonpage').append(newDiv);
    // TODO: Figure out why class name is coming back as "undefined" - why isn't this line working?    // Not working even for a string...    $(newDiv).addClass(currentWord);
    console.log(newDiv.className);
    wordCounter += 1;

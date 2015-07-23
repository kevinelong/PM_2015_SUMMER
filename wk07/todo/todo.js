function addNewItem(item, important) {
    // given a string representing the text of the item, create it
    if (!item) {
        // do not create empty items
        return;
    }

    // add item to list
    var itemElement = document.createElement('div');
    var itemTextElement = document.createTextNode(item);
    itemElement.appendChild(itemTextElement);
    var position = document.getElementById('list');
    position.appendChild(itemElement);

    // give the div styling
    itemElement.className = 'item';
    if (important) {
        itemElement.className = itemElement.className + ' important';
    }

    // clear the input fields
    var inputField = document.getElementById('itemInput');
    inputField.value = '';
    var checkField = document.getElementById('important');
    checkField.checked = false;
}

function completeItem(event) {
    var item = event.target;

    // remove item from parent
    var parentItem = item.parentNode;
    parentItem.removeChild(item);

    // add it to done list
    var doneList = document.getElementById('doneList');
    doneList.appendChild(item);
}

function clickAddButton() {
    var item = document.getElementById('itemInput');
    var itemText = item.value;
    var important = document.getElementById('important').checked;
    addNewItem(itemText, important);

    // add focus to the text input box
    item.focus();
}

var button = $('#addItemButton');
var itemList = $('#list');
var itemInput = $('#itemInput');
var navAnchor = $('nav a');

// add button event listener to add new item
button.on('click', clickAddButton);

// complete item event listener
itemList.on('click', function (e) {
    completeItem(e);
});

// watch for return key to be pressed when input box is in focus
itemInput.on('keyup', function (e) {
    if (e.keyCode === 13) {
        clickAddButton();
    }
});

// use ajax to load the next page
navAnchor.on('click', function (e) {
    e.preventDefault();
    var url = this.href;

    $('nav a.current').removeClass('current');
    $(this).addClass('current');

    $('#container').remove();
    $('#content').load(url + ' #content').hide().fadeIn(1000);
});
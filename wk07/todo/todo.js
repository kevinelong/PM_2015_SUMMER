var todosArray = [];
var completesArray = [];
function addNewItem(item, list) {
    // given a string representing the text of the item, create it
    // the list arg is the id of the list element to add it to
    // to allow for adding the element to either the done or the todos list
    if (!item) {
        // do not create empty items
        return;
    }

    // add item to list on page
    var itemElement = $('<div class=\"item\">' + item + '</div>');
    $('#' + list).append(itemElement);

    // clear the input fields
    $('#itemInput').val('');
}

function completeItem(event) {
    var item = $(event.target);

    // remove item from parent and add to done list
    item.remove();
    $('#doneList').append(item);

    // remove it from the todosArray and add it to the completesArray
    var itemText = item.textContent;
    var index = todosArray.indexOf(itemText);
    todosArray.splice(index, 1);
    completesArray.push(itemText);
}

function clickAddButton() {
    var item = $('#itemInput')[0];  // get the first, should only be one
    var itemText = item.value;
    addNewItem(itemText, 'list');

    // add focus to the text input box
    item.focus();
    todosArray.push(itemText);
}

function addTodosListeners() {
    // adds the event listeners for the todos page
    var button = $('#addItemButton');
    var itemList = $('#list');
    var itemInput = $('#itemInput');

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
}
addTodosListeners();

function loadTodosPage() {
    // add todos back to page
    todosArray.forEach(function(item, i, a) {
        addNewItem(item, 'list');
    });
    // add completes back to page
    completesArray.forEach(function(item, i, a) {
        addNewItem(item, 'doneList');
    });
    addTodosListeners();
}

function loadPage(page) {
    var id = page.id;
    if (id === 'homeAnchor') {
        loadTodosPage();
    }
}

// use ajax to load the next page
var navAnchor = $('nav a');
navAnchor.on('click', function (e) {
    var anchor = this;
    e.preventDefault();
    var url = this.href;

    $('nav a.current').removeClass('current');
    $(this).addClass('current');

    $('#container').remove();
    $('#content').load(url + ' #content', function() {
        loadPage(anchor);
    }).hide().fadeIn(500);
});
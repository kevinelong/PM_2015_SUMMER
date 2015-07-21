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

// add button event listener
var button = document.getElementById('addItemButton');
button.addEventListener('click', function() {
    var itemText = document.getElementById('itemInput').value;
    var important = document.getElementById('important').checked;
    addNewItem(itemText, important);
});

// complete item event listener
var itemList = document.getElementById('list');
itemList.addEventListener('click', function(e) {
   completeItem(e);
});


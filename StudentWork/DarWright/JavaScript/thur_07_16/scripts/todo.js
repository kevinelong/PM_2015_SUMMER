/**
 * Created by darwright on 7/16/15.
 */

function getTask() {
    var item = window.prompt('Add item: ');
    addTask(item)
}

function addTask(newItem) {
    var ulNode = document.getElementsByTagName('ul')[0];
    var UpdateItem = document.createElement('li');
    UpdateItem.className=('list');
    UpdateItem.id=(newItem);
    var updateItem = document.createTextNode(newItem);
    UpdateItem.appendChild(updateItem);
    ulNode.appendChild(UpdateItem);
    addButtons(newItem);
}

function addButtons(newItem) {
    var itemNode = document.getElementById(newItem);
    console.log(itemNode);
    itemNode.innerHTML= newItem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
        "<button class='btn2' onclick='addImportant(&#39;" + newItem + "&#39;)'>" +
        "Important</button> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; " +
        "<button class='btn2' onclick='addSemiImportant(&#39;" + newItem + "&#39;)'>" +
        "Semi_Important</button> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; " +
        "<button class='btn2' onclick='removeImportant(&#39;" + newItem + "&#39;)'>" +
        "Not Important</button> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; " +
        "<button class='btn2' onclick='removeTask(&#39;" + newItem + "&#39;)'>Done!</button>"
}

function removeTask(id){
    element = document.getElementById(id);
    element.parentNode.removeChild(element);
}

function addImportant(id){
    var item = document.getElementById(id);
    console.log(item);
    item.className=("important");
}

function addSemiImportant(id){
    var item = document.getElementById(id);
    console.log(item);
    item.className=("semi_important");
}

function removeImportant(id){
    var item = document.getElementById(id);
    console.log(item);
    item.className=("list");
}
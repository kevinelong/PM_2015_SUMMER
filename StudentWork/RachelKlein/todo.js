/**
 * Created by rachel on 7/17/15.
 */

var button = document.getElementById("newbutton");
var goalList = document.getElementById("goals");

button.addEventListener("click", function() {
    var newGoal = addGoal();
    pickPriority(newGoal);
}, false);
goalList.addEventListener("click", missionAccomplished, false);
goalList.addEventListener("dblclick", goAway, false);

function addGoal() {
    var promptGoal = document.getElementById("textbox").value;
    var newGoal = document.createElement('li');
    var newGoalText = document.createTextNode(promptGoal);
    newGoal.appendChild(newGoalText);
    var position = document.getElementsByTagName('ul')[0];
    position.appendChild(newGoal);
    document.getElementById("textbox").value = '';
    return newGoal;
}

function missionAccomplished(e) {
    var target = e.target;
    target.className = "done";
}

function goAway(e) {
    var target = e.target;
    target.parentNode.removeChild(target);
}

function pickPriority(newGoal) {
    var priority = document.getElementById("priority_menu").value;

    if (priority === "high") {
        newGoal.className = "high";
     }

    else if (priority === "low") {
        newGoal.className = "low";
    }

    else if (priority === "medium") {
        newGoal.className = "medium";
    }
}
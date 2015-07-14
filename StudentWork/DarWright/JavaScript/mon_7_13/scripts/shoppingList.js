/**
 * Created by darwright on 7/13/15.
 */

var shoppingList = ['eggs', 'milk', 'yogurt', 'turkey', 'corn', 'cereal']

for (var i = 0; i < shoppingList.length; i++){
    document.write('<div class="list" onclick="toggle_visibility(id)" style="display: block" id="'
        + shoppingList[i] + '">' + shoppingList[i] + '</div>');


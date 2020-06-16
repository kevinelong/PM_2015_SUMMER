// Given an array with duplicates, this function will return the array without the duplicates.
// This could have been done in a much simpler way if I had used indexOf to see if the value was
// NOT in the list (would return -1).

mantaRay = [1, 2, 3, 3, 3, 4, 4, 5];

var deDupping = function(someArray) {
    var newArray = [];
    for (var i = 0; i <= someArray.length; i += 1) {
        if (isInArray(newArray, someArray[i]) === false) {
            newArray.push(someArray[i])
        }
    }
    return newArray;
}

var isInArray = function(anArray, value) {
    var counter = 0;
    while (counter <= anArray.length) {
        counter ++;
        if (value == anArray[counter]) {
             return true;
            }
   }
    return false;
}

console.log(mantaRay);
var newMantaRay = deDupping(mantaRay);
console.log(newMantaRay);


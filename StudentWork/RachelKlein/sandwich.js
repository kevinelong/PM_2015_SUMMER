/**
 * Created by rachel on 7/15/15.
 */

// Sandwich maker

// All prices are in cents and calories are per serving (2 slices of bread, etc).

function Bread(price, calories) {
    this.price = price;
    this.calories = calories;
}

function Meat(price, calories) {
    this.price = price;
    this.calories = calories;
}

function Cheese(price, calories) {
    this.price = price;
    this.calories = calories;
}

function Veggie(price, calories) {
    this.price = price;
    this.calories = calories;
}

// Types of bread available

var sourdough = new Bread(50, 370);
var wholewheat = new Bread(50, 140);
var twelvegrain = new Bread(50, 220);
var glutenfree = new Bread(100, 160);
var nobread = new Bread(0, 0);

// Types of meat (or "meat" as the case may be) available

var turkey = new Meat(100, 120);
var roastbeef = new Meat(100, 300);
var bacon = new Meat(200, 200);
var tofurkey = new Meat(150, 100);
var nomeat = new Meat(0, 0);

// Types of cheese available

var cheddar = new Cheese(100, 250);
var swiss = new Cheese(100, 200);
var daiya = new Cheese(150, 90);
var nocheese = new Cheese(0, 0);

// Types of veggies available

var greens = new Veggie(50, 5);
var roastedveggies = new Veggie(100, 50);
var noveggies = new Veggie(0, 0);

function submitSandwich() {
    var breadType = document.sandwichform.bread.value;
    var meatType = document.sandwichform.meat.value;
    var cheeseType = document.sandwichform.cheese.value;
    var veggieType = document.sandwichform.veggie.value;

    var bread;
    var meat;
    var cheese;
    var veggie;

    if (breadType === 'sourdough') {
        bread = sourdough;
    }
    else if (breadType === 'wholewheat') {
        bread = wholewheat;
    }
    else if (breadType === 'twelvegrain') {
        bread = twelvegrain;
    }
    else if (breadType === 'glutenfree') {
        bread = glutenfree;
    }
    else if (breadType === 'nobread') {
        bread = nobread;
    }


    if (meatType === 'turkey') {
        meat = turkey;
    }

    else if (meatType === 'roastbeef') {
        meat = roastbeef;
    }

    else if (meatType === 'bacon') {
        meat = bacon;
    }

    else if (meatType === 'tofurkey') {
        meat = tofurkey;
    }

    else if (meatType === 'nomeat') {
        meat = nomeat;
    }


    if (cheeseType === 'cheddar') {
        cheese = cheddar;
    }

    else if (cheeseType === 'swiss') {
        cheese = swiss;
    }

    else if (cheeseType === 'daiya') {
        cheese = daiya;
    }

    else if (cheeseType === 'nocheese') {
        cheese = nocheese;
    }


    if (veggieType === 'greens') {
        veggie = greens;
    }

    else if (veggieType === 'roastedveggies') {
        veggie = roastedveggies;
    }

    else if (veggieType === 'noveggies') {
        veggie = noveggies;
    }

    customerSandwich = new Sandwich(bread, meat, cheese, veggie);
    var sandwichPrice = customerSandwich.getSandwichPrice();
    // Converting the sandwich price to dollars.
    sandwichPrice /= 100;

    var sandwichStuff = document.forms[0];
    var sandwichText = "";
    for (i = 0; i < sandwichStuff.length; i++) {
        if (sandwichStuff[i].checked) {
            sandwichText = sandwichText + sandwichStuff[i].value + " ";
            }
        }

    //if (document.registrationForm.calorie_count.checked === true) {
    //    var sandwichCalories = customerSandwich.getSandwichCalories();
    //    sandwichText = sandwichText + "which is " + sandwichCalories + " calories."
    //}

    if (sandwichText != "") {
        alert("Ye ordered a sandwich with: " + sandwichText + ". That will be $" + sandwichPrice + ".");
        return true;
    }
    return false;
}

function Sandwich(bread, meat, cheese, veggie) {
    this.bread = bread;
    this.meat = meat;
    this.cheese = cheese;
    this.veggie = veggie;

    this.getSandwichPrice = function() {
        var sandwichPrice = this.bread.price + this.meat.price + this.cheese.price + this.veggie.price;
        return sandwichPrice;
    }

    this.getSandwichCalories = function() {
        var sandwichCalories = this.bread.calories + this.meat.calories + this.cheese.calories + this.veggie.calories;
        return sandwichCalories;
    }
}
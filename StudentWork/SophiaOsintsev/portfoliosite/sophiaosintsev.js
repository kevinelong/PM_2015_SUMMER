$(document).ready(function(){
    var quotes = new Array();

        quotes[0] = "Failure will never overtake me if my determination to succeed is strong enough. -Og Mandino";
        quotes[1] = "What you do today can improve all your tomorrows. -Ralph Marston";
        quotes[2] = "In order to succeed, we must first believe that we can. -Nikos Kazantzakis";
        quotes[3] = "Always do your best. What you plant now, you will harvest later. -Og Mandino";
        quotes[4] = "It does not matter how slowly you go as long as you do not stop. -Confucius";
        quotes[5] = "With the new day comes new strength and new thoughts. -Eleanor Roosevelt";
        quotes[6] = "Don't watch the clock; do what it does. Keep going. -Sam Levenson";
    console.log(quotes);
    var counter = 0;

    function slideshow() {
        if (counter > 4) counter = 0;
        $("#textslide").text(quotes[counter]);
        counter++;
        console.log(counter);
        setTimeout(slideshow, 4000);
    }
    slideshow();


    $("#baking1, #traveling1, #restoring1, #ocean1, #russian1, #duy1").hide();


    $("#baking").hover(function(){
        $("#baking1").toggle();
    });

    $("#traveling").hover(function(){
        $("#traveling1").toggle();
    });


    $("#restoring").hover(function(){
        $("#restoring1").toggle();
    });

    $("#ocean").hover(function(){
        $("#ocean1").toggle();
    });

    $("#russian").hover(function(){
        $("#russian1").toggle();
    });

    $("#duy").hover(function(){
        $("#duy1").toggle();
    });

});

/**
 * Created by stephen on 7/15/15.
 */


var hotel = {

    name:'The Kings Plaza Hotel,
    rooms:500,
    roomtypes: ['2T','1Q','2Q','1K','2K'],
    booked:400,
    gym: true,
    checkAvaliblity: function() {
        return this.rooms-this.booked;
    }
};
var elName= document.getElementById('hotelName');
        elName.textContent =hotel.name;

var elRooms =document.getElementById('rooms');
        elRooms.textContent = hotel.checkAvaliblity();

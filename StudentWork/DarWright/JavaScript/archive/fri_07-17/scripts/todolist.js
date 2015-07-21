$(document).ready(function() {
    //click add item, remove .hidden class to show form
    $('#btnAddItem').click(function(event) {
        event.preventDefault();
        $('#createItem').removeClass('hidden');
    });

    //Save the item to the list
    $('#btnSaveItem').click(function(event) {
        event.preventDefault();
        var itemName = document.getElementById("item").value;
        var importantLevel = document.getElementById("important").value;

        var table = document.getElementById("tblItems");
        var row =table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = itemName;
        cell2.innerHTML = importantLevel;
        cell3.innerHTML = '<a href="#" id="btnDeleteItem" >Delete item</a>';

        //clear the form after. Can this be another function?
        document.getElementById("item").value = '';
        $("#important").val('Semi');
    });

    //clear the form
    $('#btnClearItem').click(function(event){
        event.preventDefault();
        document.getElementById("item").value = '';
        $("#important").val('Semi');
    });

    //delete the row
    $('#tblItems').on('click', 'tr a', function (event){
        event.preventDefault();
        $(this).closest('tr').remove();
    });
});



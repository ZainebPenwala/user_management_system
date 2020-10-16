$( document ).ready(function()
{
    $('#user-listings').DataTable({
        initComplete: function() {
            $('#user-listings').appendTo($('#outside'))
        }
    });
});
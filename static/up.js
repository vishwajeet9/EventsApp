
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function ajaxsetup() {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

}
//$(document).ready(function() {
//    $('#optionvalue').change(function () {
//        ajaxsetup();
//        var id = $("#optionvalue").val();
//         $.ajax({
//           url: "/api/details/" + id,
//           type: "GET",
//           dataType :'json',
//           success: function(data) {
//               $('#eventname1').val(data.data[0].fields.eventname);
//               $('#firstname1').val(data.data[0].fields.firstname);
//               $('#lastname1').val(data.data[0].fields.lastname);
//               $('#event1').val(data.data[0].fields.info1);
//               $('#date23').val(data.data[0].fields.date);
//               console.log(data);
//               alert("Loaded!")
//           },
//           error:function() {
//               alert("error in getting from server")
//           }
//
//
//        });




$(document).ready(function(){
    $('#dateRange').click(function(){
        ajaxsetup();
        var date1 = $("#optionvalue3").val();
        var date2 = $("#optionvalue4").val();
        $.ajax({
            url:"search",
            type:"POST",
            data: {
                'search_date1': date1,
                'search_date2': date2
            },
            success:function(data1){
               $("#search").html(data1)
            },
            error:function(data1) {
                alert("No Events on selected date ")
            }

        });

    });
});



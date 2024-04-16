// using ajax to send data to the python file
$(document).ready(function () {
    d = "fetchuserid"
    $.ajax({
        method: 'post',
        url: 'pythonf/signup2.py',
        data: {
            what: d
        },
        success: function (data) {
            // console.log(data);
            $('#mySelect').append(data)
        },
    });

});



$(document).ready(function () {
    $('#search').on('click', function () {
        // alert("searching")
        userid = $('#mySelect').val()
        username = $('#username').val()

        // alert(userid)

        $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
                what: "fetch_by_id_name",
                userid: userid,
                username: username,
            },
            success: function (data) {
                console.log(data);
               
                // alert(username)
                $('#tab').css({ "visibility": "visible" })
                $('#tab').append(data)
            },
        });
    })
})





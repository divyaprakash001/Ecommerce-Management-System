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


// code for display incoming data after executing query
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

                localStorage.removeItem("sdata")

                if (data.includes("please enter remaining field")) {
                    $(".msg").text("please fill all inputs")
                    $(".msg").css({ "color": "red" })
                } else if (data != []) {
                    $(".msg").css({ "display": "none" })
                    $('#tab').css({ "visibility": "visible" })
                    $('#table_container').html(data)
                } else if (data.includes("no data available")) {
                    alert('empty result set')
                    $(".msg").text("no data is comming")
                    $(".msg").css({ "color": "red" })
                }
            },
        });
    })
})




// all records code for display incoming data after executing query
$(document).ready(function () {
    $('#all_records_btn').on('click', function () {

        $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
                what: "fetch_all",
            },
            success: function (data) {
                console.log(data);

                // localStorage.removeItem("sdata")

                if (data != []) {
                    $(".msg").css({ "display": "none" })
                    $('#tab').css({ "visibility": "visible" })
                    $('#table_container').html(data)

                } else if (data.includes("no data available")) {
                    alert('empty result set')
                    $(".msg").text("no data is comming")
                    $(".msg").css({ "color": "red" })
                }
            },
        });
    })


})

$(document).ready(function () {
    $(".del").on("click", function () {
        alert("deletion")
    })
})














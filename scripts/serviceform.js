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

                if (data.includes("please enter remaining field")) {
                    $(".msg").text("please fill all inputs")
                    $(".msg").css({ "color": "red" })
                } else if (data != []) {
                    $(".msg").css({ "display": "none" })
                    $('#tab').css({ "visibility": "visible" })
                    $('#table_container').html(data)
                } else if (data.includes("no data available")) {
                    // alert('empty result set')
                    $(".msg").text("no data is comming")
                    $(".msg").css({ "color": "red" })
                }


                // if user click on delete button
                $(".del").on("click", function () {
                    d = "delete"
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    console.log(uid);

                    $.ajax({
                        method: 'post',
                        url: 'pythonf/signup2.py',
                        data: {
                            what: d,
                            userid: uid
                        },
                        success: function (data) {
                            console.log(data);
                            if (data.includes("data deleted successfully")) {
                                console.log("ho gyaa dlete");
                            }
                        },
                    });
                    $(this).closest('tr').remove();


                    // let v = $(this).closest('tr').remove();
                    // console.log(v);
                })

                // code for update the data when use click on update button
                $(".update").on("click", function () {
                    d = "fetchForUpdate"
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    // console.log(uid);

                    $.ajax({
                        method: 'post',
                        url: 'pythonf/signup2.py',
                        data: {
                            what: d,
                            userid: uid
                        },
                        success: function (data) {
                            console.log(data);
                            if (data.includes("data fetching successfully")) {
                                $("#table_container").css({ "display": "none" })
                                $("#myform").css({ "display": "none" })
                                $(".form_placeholder").html(data)
                            }

                            // code for saving the updated the data when use click on update button
                            $("#save").on("click", function () {
                                d = "savetheupdate"
                                uid1 = $("#uid").val();
                                uname1 = $("#uname").val();
                                uemail1 = $("#uemail").val();
                                umob1 = $("#umob").val();

                                $.ajax({
                                    method: 'post',
                                    url: 'pythonf/signup2.py',
                                    data: {
                                        what: d,
                                        uid: uid1,
                                        uname: uname1,
                                        uemail: uemail1,
                                        umob: umob1
                                    },
                                    success: function (data) {
                                        // window.location.href = 'showData.html'
                                        console.log(data);

                                        if (data.includes("successfully saved")) {
                                            if (data.includes("successfully saved")) {
                                                $(".msg").css({ "display": "block", "color": "green" });
                                                $(".msg").text("data updated successfully");
                                            } else {
                                                $(".msg").css({ "display": "block", "color": "red" });
                                                $(".msg").text("data updation failed. Some error occured.");
                                            }
                                        }
                                    },
                                });
                            })
                        },
                    });
                })
            },
        });
    })
})





// ----------------********************************-------------------





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


                if (data != []) {
                    $(".msg").css({ "display": "none" })
                    $('#tab').css({ "visibility": "visible" })
                    $('#table_container').html(data)

                } else if (data.includes("no data available")) {
                    alert('empty result set')
                    $(".msg").text("no data is comming")
                    $(".msg").css({ "color": "red" })
                }

                // code for deleting the data when use click on delete button
                $(".del").on("click", function () {
                    d = "delete"
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    console.log(uid);

                    $.ajax({
                        method: 'post',
                        url: 'pythonf/signup2.py',
                        data: {
                            what: d,
                            userid: uid
                        },
                        success: function (data) {
                            console.log(data);
                            if (data.includes("data deleted successfully")) {
                                $(".msg").css({ "display": "block", "color": "green" });
                                $(".msg").text("data deleted successfully");
                            } else {
                                $(".msg").css({ "display": "block", "color": "red" });
                                $(".msg").text("data deletion failed. Some error occured.");
                            }
                        },
                    });
                    $(this).closest('tr').remove();
                })


                // code for update the data when use click on update button
                $(".update").on("click", function () {
                    d = "fetchForUpdate"
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    // console.log(uid);

                    $.ajax({
                        method: 'post',
                        url: 'pythonf/signup2.py',
                        data: {
                            what: d,
                            userid: uid
                        },
                        success: function (data) {
                            console.log(data);
                            if (data.includes("data fetching successfully")) {
                                $("#table_container").css({ "display": "none" })
                                $("#myform").css({ "display": "none" })
                                $(".form_placeholder").html(data)
                            }

                            // code for saving the updated the data when use click on update button
                            $("#save").on("click", function () {
                                d = "savetheupdate"
                                uid1 = $("#uid").val();
                                uname1 = $("#uname").val();
                                uemail1 = $("#uemail").val();
                                umob1 = $("#umob").val();



                                $.ajax({
                                    method: 'post',
                                    url: 'pythonf/signup2.py',
                                    data: {
                                        what: d,
                                        uid: uid1,
                                        uname: uname1,
                                        uemail: uemail1,
                                        umob: umob1
                                    },
                                    success: function (data) {
                                        // window.location.href = 'showData.html'
                                        console.log(data);

                                        if (data.includes("successfully saved")) {
                                            $(".msg").css({ "display": "block", "color": "green" });
                                            $(".msg").text("data updated successfully");
                                        } else {
                                            $(".msg").css({ "display": "block", "color": "red" });
                                            $(".msg").text("data updation failed. Some error occured.");
                                        }
                                    },
                                });
                            })
                        },
                    });
                })
            },
        });
    })
})















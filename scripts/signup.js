// on clicking on login, redirect to login page
let loginbtn = document.querySelector("#loginbtn");
loginbtn.addEventListener("click", function () {
    window.location.href = 'login.html';
});



// animation on label on click on input element
$(function () {

    // loading navbar on all pages
    $("#nav_placeholder").load("nav.html")

    // animation on label or placeholder of input field
    $('input[type="text"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' })
    });
    $('input[type="email"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' })
    });
    $('input[type="password"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' })
    });

    // by default setting the box display : none;
    $(".fa-xmark").click(function () {
        $('.msg_box').css("display", "none")
    })
});


// using ajax to send data to the python file
$(function () {
    $('#subbtn').click(function (e) {
        e.preventDefault()
        // getting the data from input field of signup.html
        // usertype1 = $('#ucustomer').val();
        usertype1 = 'customer';
        userid1 = $('#userid').val();
        username1 = $("#username").val();
        useremail1 = $('#uemail').val();
        mobno1 = $('#mobno').val();
        upass1 = $('#upass').val();
        uagree1 = $('#uagree').val();
        d = "insert"

        // check whether user tick term and conditions
        if ($('#uagree').not(':checked').length) {
            uagree1 = "off"
        } else {
            uagree1 = "on"
        }


        // sending the form input field data to python file signup2.py
        $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
                usertype: usertype1,
                userid: userid1,
                username: username1,
                useremail: useremail1,
                mobno: mobno1,
                upass: upass1,
                uagree: uagree1,
                what: d
            },
            success: function (data, status, jqxhr) {
                console.log(data);
                console.log(status);
                console.log(jqxhr);

                // if data successfully inserted in database
                if (data.includes("inserted")) {
                    $('.msg').html("Success entry")
                    $('.msg_box').css({ "display": "block", "color": 'green' })
                    $('#userid').val("");
                    $("#username").val("");
                    $('#uemail').val("");
                    $('#mobno').val("");
                    $('#upass').val("");
                    $('#uagree').val("");
                    $("#urpass").val("");
                }

                // if duplicate userid filled or gone to db
                if (data.includes("Duplicate entry")) {
                    $('.msg').html("Duplicate entry")
                    $('.msg_box').css({ "display": "block", "color": "red" })
                }

                // if user donot check term and condition then display the message 
                if (uagree1 == 'off') {
                    $('.msg').html("Accept terms & conditions")
                    $('.msg_box').css({ "display": "block", "color": "red" })
                }

                // if at least one input field is empty then display the message
                if (data.includes("Error !!! One of the field is empty")) {
                    $('.msg').html("empty field")
                    $('.msg_box').css({ "display": "block", "color": "red" })
                }

            },
        });
    });
});





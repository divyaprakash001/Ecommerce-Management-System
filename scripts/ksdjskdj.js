// on clicking on login, redirect to login page
let loginbtn = document.querySelector("#loginbtn");
loginbtn.addEventListener("click", function () {
    window.location.href = 'login.html';
});


// animation on label on click on input element
$(function () {
    $('input[type="text"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' })
    });
    $('input[type="email"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' })
    });
    $('input[type="password"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' })
    });
});



// using ajax to send data to the python file
$(function () {
    $('#subbtn').click(function (e) {
        e.preventDefault()
        usertype1 = $('#ucustomer').val();
        userid1 = $('#userid').val();
        username1 = $("#username").val();
        useremail1 = $('#uemail').val();
        mobno1 = $('#mobno').val();
        upass1 = $('#upass').val();
        uagree1 = $('#uagree').val();
        // alert(userid)
        $.ajax({
            method: 'post',
            data: {
                usertype: usertype1,
                userid: userid1,
                username: username1,
                useremail: useremail1,
                mobno: mobno1,
                upass: upass1,
                uagree: uagree1,
            },
            url: 'pythonf/signup.py',
            success: function (data,status) {
                console.log(data);
                console.log(status);
            }
        });
    });
});





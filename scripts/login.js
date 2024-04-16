$(document).ready(function () {
    $('#logbtn').on('click', function (e) {
        e.preventDefault();
    });

    $("#signupbtn").on("click", function () {
        window.location.href = 'signup.html';
    })

    $('#forgetpass').on("click",function(){
        window.location.href = 'forgetpassword.html';
    })
 
})

$(function(){
    $('input[type="email"]').click(function(){
        $(this).siblings('.lab').css({'top':'-.6rem'});
    })
    $('input[type="password"]').click(function(){
        $(this).siblings('.lab').css({'top':'-.6rem'});
    })
})


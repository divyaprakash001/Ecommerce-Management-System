$(document).ready(function () {
    $('#logbtn').on('click', function (e) {
        e.preventDefault();
    });

    $("#signupbtn").on("click", function () {
        window.location.href = 'signup.html'
    })
 
})

$(function(){
    // $('input[type="text"]').click(function(){
    //     $(this).siblings('.lab').css({'top':'0rem'})
    // })
    $('input[type="email"]').click(function(){
        $(this).siblings('.lab').css({'top':'-1rem'})
    })
    $('input[type="password"]').click(function(){
        $(this).siblings('.lab').css({'top':'-1rem'})
    })
})
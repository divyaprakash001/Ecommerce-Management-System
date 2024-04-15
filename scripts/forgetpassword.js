$(function () {
    // $('input[type="text"]').click(function(){
    //     $(this).siblings('.lab').css({'top':'0rem'})
    // })
    $('input[type="email"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' });
    })
    $('input[type="text"]').click(function () {
        $(this).siblings('.lab').css({ 'top': '-.6rem' });
    })

    $('#loginbtn').on("click", function () {
        window.location.href = "login.html";
    })

})

$(function () {
    $('#getotp').on("click", function (e) {
        e.preventDefault();
        window.location.href = "updatepassword.html";
    })
})
$(document).ready(function () {
    $('#logbtn').on('click', function (e) {
        e.preventDefault();
    });

    $("#signupbtn").on("click", function () {
        window.location.href = 'signup.html'
    })

})
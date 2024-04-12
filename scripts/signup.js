let loginbtn = document.querySelector("#loginbtn");
loginbtn.addEventListener("click", function () {
    window.location.href = 'login.html';
})

// let subbtn = document.querySelector("#subbtn");
// subbtn.addEventListener("click", function (e) {
//     alert("Are you sure to submit this form ?")
//     e.preventDefault();
// })

$(function () {
    $('#subbtn').click(function (e) {
        e.preventDefault()
        userid = $('#userid').val();
        ufname = $("#ufname").val();
        ulname = $("#ulname").val();
        useremail = $('#uemail').val();
        mobno = $('#mobno').val();
        upass = $('#upass').val();
        urpass = $('#urpass').val();
        uagree = $('#uagree').val();
        // alert(userid)
        $.ajax({
            method: 'post',

            // data: JSON.stringify({
            //     userid1: userid,
            //     ufname1: ufname,
            //     ulname1: ulname,
            //     useremail1: useremail,
            //     mobno1: mobno,
            //     upass1: upass,
            //     urpass1: urpass,
            //     uagree1: uagree,
            // }),
            url: 'pythonf/signup1.py',
            datatype: "data",
            success: function (data1) {
                console.log(data1);
                console.log(data1.message);
                console.log(data1.keys);
                console.log(data1.data);
            }
        });
    });
});
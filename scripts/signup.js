let loginbtn = document.querySelector("#loginbtn");
loginbtn.addEventListener("click", function () {
    window.location.href = 'login.html';
})

let subbtn = document.querySelector("#subbtn");
subbtn.addEventListener("click", function (e) {
    alert("Are you sure to submit this form ?")
    e.preventDefault();
})
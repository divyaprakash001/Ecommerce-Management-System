let signupbtn = document.querySelector("#signupbtn");
loginbtn.addEventListener("click", function () {
    window.location.href = 'login.html';
})

let logbtn = document.querySelector("#logbtn");
logbtn.addEventListener("click", function (e) {
    alert("Are you sure to login ?")
    e.preventDefault();
})
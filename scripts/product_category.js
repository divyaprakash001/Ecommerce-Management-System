

$(document).ready(function () {
  $('input[type="text"]').click(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });


  $(".search_btn").on('click', function () {
    window.location.href = "pages-search-product_category.html";
  })
  $(".add_btn").on('click', function () {
    window.location.href = "pages-product_category.html";
  })
})

$(document).ready(function () {
  $("#sub_btn").on("click", function (e) {
    e.preventDefault();



    d = "insert_pro_cat";
    pro_cat_id1 = $("#pro_cat_id").val();
    pro_cat_name1 = $("#pro_cat_name").val();
    pro_cat_desc1 = $("#pro_cat_desc").val();

    // console.log(pro_cat_id1, pro_cat_name1, pro_cat_desc1);

    $.ajax({
      method: 'post',
      url: 'pythonf/signup2.py',
      data: {
        pro_cat_id: pro_cat_id1,
        pro_cat_name: pro_cat_name1,
        pro_cat_desc: pro_cat_desc1,
        what: d
      }, success: function (response) {
        console.log(response);



        if (response.includes("product category inserted")) {
          swal({
            title: "Yeah!",
            text: "Data Inserted Successfully!",
            icon: "success",
          });
          $('#pro_cat_id').val("");
          $('#pro_cat_name').val("");
          $("#pro_cat_desc").val("");
        } else if (response.includes("Error !!! One of the field is empty")) {
          alert("Error !!! One of the field is empty")
          swal({
            title: "Failed!",
            text: "One of the field is empty!",
            icon: "error",
          });
        } else {
          alert("something erro")
        }

      },
      error: function (errorData) {
        console.error(errorData)
      }
    })




  })
})


// using ajax to send data to the python file
$(document).ready(function () {
  $("#search_btn").on('click', function (e) {
    e.preventDefault()
    d = "fetchcatid"
    $.ajax({
      method: 'post',
      url: 'pythonf/signup2.py',
      data: {
        what: d
      },
      success: function (data) {
        console.log(data);
        // $('#mySelect').append(data)
      },
    });
  })

});
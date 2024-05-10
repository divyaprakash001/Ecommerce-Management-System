$(document).ready(function () {

  $('input[type="text"]').click(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });
  $('textarea').click(function () {
    $(this).siblings('.lab').css({ 'top': '-.5rem' })
  });

  $(".search_btn").on("click", function () {
    window.location.href = "pages-search-product_details.html"
  })

  $(".add_btn").on('click', function () {
    window.location.href = "pages-product_entry_form.html";
  })
})



$(document).ready(function () {

  // using ajax to send data to the python file and fetch product category id
  d = "fetchcatid"
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: d
    },
    success: function (data) {
      console.log(data);
      $('#prod_cat_id').append(data)
    },
  });


  // on clicking of submit button on product entry form 
  let imageDataUrl1 = ""
  let imageDataUrl2 = ""
  let imageDataUrl3 = ""

  // image data url for image 1
  $("#prod_file1").on("change", function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (event) {
      imageDataUrl1 = event.target.result;
      // console.log("Image data URL:", imageDataUrl1);
      // You can perform further actions with the image data URL here
    };

    if (file) {
      reader.readAsDataURL(file);
    } else {
      console.error("No file selected.");
    }
  });


  // image data url for image 2
  $("#prod_file2").on("change", function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (event) {
      imageDataUrl2 = event.target.result;
      // console.log("Image data URL:", imageDataUrl2);
      // You can perform further actions with the image data URL here
    };

    if (file) {
      reader.readAsDataURL(file);
    } else {
      console.error("No file selected.");
    }
  });



  // image data url for image 3
  $("#prod_file3").on("change", function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (event) {
      imageDataUrl3 = event.target.result;
      // console.log("Image data URL:", imageDataUrl3);
      // You can perform further actions with the image data URL here
    };

    if (file) {
      reader.readAsDataURL(file);
    } else {
      console.error("No file selected.");
    }
  });

  $("#sub_btn").on("click", function (e) {
    e.preventDefault();

    d = "insert_product";
    // alert(d)
    


    $.ajax({
      method: 'post',
      url: 'pythonf/signup2.py',
      data: {
        prod_id: $("#prod_id").val(),
        prod_name: $("#prod_name").val(),
        prod_cat_id: $("#prod_cat_id").val(),
        prod_stock: $("#prod_stock").val(),
        prod_ori_price: $("#prod_ori_price").val(),
        prod_dis_price: $("#prod_dis_price").val(),
        prod_width: $("#prod_width").val(),
        prod_height: $("#prod_height").val(),
        prod_size: $("#prod_size").val(),
        prod_file1: imageDataUrl1,
        prod_file2: imageDataUrl2,
        prod_file3: imageDataUrl3,
        prod_desc: $("#prod_desc").val(),
        what: d
      }, success: function (response) {
        console.log(response);



        if (response.includes("product inserted")) {
          swal({
            title: "Yeah!",
            text: "Data Inserted Successfully!",
            icon: "success",
          });
          $("#prod_id").val("");
          $("#prod_name").val("");
          $("#prod_cat_id").val("");
          $("#prod_stock").val("");
          $("#prod_ori_price").val("");
          $("#prod_dis_price").val("");
          $("#prod_width").val("");
          $("#prod_height").val("");
          $("#prod_size").val("");
          $("#prod_file1").val("");
          $("#prod_file2").val("");
          $("#prod_file3").val("");
          $("#prod_desc").val("");
        } else if (response.includes("Error !!! One of the field is empty")) {
          // alert("Error !!! One of the field is empty")
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


$(document).ready(function () {
  imageDataUrl1=""
  imageDataUrl2=""
  imageDataUrl3=""
  
  let d = ''
  $('input[type="text"]').click(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });


  $(".search_btn").on('click', function () {
    window.location.href = "pages-search-product_category.html";
  })
  $(".add_btn").on('click', function () {
    window.location.href = "pages-product_entry_form.html";
  })




  // using ajax to send data to the python file
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "fetchcatid"
    },
    success: function (data) {
      console.log(data);
      $('#pro_cat_id').append(data)
    },
  });


  // using ajax to send data to the python file
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "fetchprodid"
    },
    success: function (data) {
      console.log(data);
      $('#prod_id').append(data)
    },
  });




  // code for display incoming data after executing query
  $('#search_btn').on('click', function () {

    $.ajax({
      method: 'post',
      url: 'pythonf/signup2.py',
      data: {
        what: "fetch_prod_details_conditions",
        pro_id: $('#prod_id').val(),
        prod_name: $('#prod_name').val(),
        prod_cat_name: $('#prod_cat_name').val(),
        pro_cat_id: $('#pro_cat_id').val(),
        prod_stock: $('#prod_stock').val(),
        prod_price_range: $('#prod_price_range').val(),
        prod_size: $('#prod_size').val(),
      },
      success: function (data) {
        console.log(data);
        // alert(data)

        if (data.includes("please select one field")) {
          $('.below_card').css({ "display": "none" })
          swal({
            title: "Failed!",
            text: "please select atleast one field",
            icon: "error",
          });
        } else if (data.includes("product details fetched successfully")) {
          $('.below_card').css({ "display": "block" })
          $('.table_container').html(data)

        } else if (data.includes("no data available")) {
          $('.below_card').css({ "display": "none" })
          swal({
            title: "Failed!",
            text: "no data available",
            icon: "error",
          });
        }
        // ------------------------------

          // action perform on clicking of view button
          $('.view').click(function () {
            $(this).siblings('.img_card').css({ 'scale': '1' }) 
          })
          $('.cut').click(function () {
            $('.img_card').css({ 'scale': '0' })
          })
          
          
          // if user click on delete button
        $(".del").on("click", function () {
          d = "deleteprod"
          let pid = $(this).closest('tr').children('td:first-child').text();
          console.log(pid);

          swal({
            title: "Are you sure?",
            text: "Once deleted, you will not be able to recover this data!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
          })
            .then((willDelete) => {
              if (willDelete) {
                $.ajax({
                  method: 'post',
                  url: 'pythonf/signup2.py',
                  data: {
                    what: d,
                    prod_id: pid
                  },
                  success: function (data) {
                    console.log(data);

                    if (data.includes("data deleted successfully")) {

                      swal("Yeah! Your data has been deleted!", {
                        icon: "success",
                      });

                    } else {
                      swal({
                        title: "Failed!",
                        text: "unable to delete somethings error!",
                        icon: "error",
                      });
                    }
                  },
                });
                $(this).closest('tr').remove();
              } else {
                swal("Your data is safe!", { icon: "success" });
              }
            });
        });

        $(".edit").on("click", function () {
          d = "fetchForProdUpdate"
          let pid = $(this).closest('tr').children('td:first-child').text();
          // alert(pid)
          $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
              what: d,
              prod_id_f: pid
            },
            success: function (data) {
              // alert("hello")
              console.log(data);
              if (data.includes("data fetching successfully")) {
                $('.form_placeholder').css({ 'scale': '1' })
                $(".form_placeholder").html(data)

                
                // // image data url for image 1
                $("#prod_file1").on("change", function (event) {
                  var file = event.target.files[0];
                  var reader = new FileReader();

                  reader.onload = function (event) {
                    imageDataUrl1 = event.target.result;
                    $("#image1").attr('src', imageDataUrl1)
                    // console.log("Image data URL:", imageDataUrl1);
                    // You can perform further actions with the image data URL here
                  };

                  if (file) {
                    reader.readAsDataURL(file);
                  } else {
                    console.error("No file selected.");
                  }
                });


                // // image data url for image 2
                $("#prod_file2").on("change", function (event) {
                  var file = event.target.files[0];
                  var reader = new FileReader();

                  reader.onload = function (event) {
                    imageDataUrl2 = event.target.result;
                    $("#image2").attr('src', imageDataUrl2)
                  };

                  if (file) {
                    reader.readAsDataURL(file);
                  } else {
                    console.error("No file selected.");
                  }
                });



                // // image data url for image 3
                $("#prod_file3").on("change", function (event) {
                  var file = event.target.files[0];
                  var reader = new FileReader();

                  reader.onload = function (event) {
                    imageDataUrl3 = event.target.result;
                    $("#image3").attr('src', imageDataUrl3)
                  };

                  if (file) {
                    reader.readAsDataURL(file);
                  } else {
                    console.error("No file selected.");
                  }
                });


                // code for saving the updated the data when use click on update button
                $(".save").on("click", function (e) {
                  e.preventDefault();
                  d = "savetheprodupdate"

                  // alert(d)


                  let previmage1 = $('#image1').attr('src');
                  let previmage2 = $('#image2').attr('src');
                  let previmage3 = $('#image3').attr('src');

                  if(imageDataUrl1 == ''){
                    imageDataUrl1 = previmage1
                  }

                  if(imageDataUrl2 == ''){
                    imageDataUrl2 = previmage2
                  }

                  if(imageDataUrl3 == ''){
                    imageDataUrl3 = previmage3
                  }

                  

                  $.ajax({
                    method: 'post',
                    url: 'pythonf/signup2.py',
                    data: {
                      what: d,
                      prod_id1: $("#prod_id1").val(),
                      prod_name1: $("#prod_name1").val(),
                      prod_cat_id1: $("#prod_cat_id1").val(),
                      prod_stock1: $("#stock_size1").val(),
                      prod_ori_price1: $("#prod_ori_price1").val(),
                      prod_dis_price1: $("#prod_dis_price1").val(),
                      upd_prod_width1: $("#upd_prod_width1").val(),
                      prod_size_upd1: $("#prod_size_upd1").val(),
                      prod_file11: imageDataUrl1,
                      prod_file21: imageDataUrl2,
                      prod_file31: imageDataUrl3,
                      prod_desc1: $("#prod_desc1").val(),
                    },
                    success: function (data) {
                      // window.location.href = 'showData.html'
                      console.log(data);

                      if (data.includes("successfully updated the product data")) {
                        swal({
                          title: "Success!",
                          text: "Data updated successfully",
                          icon: "success",
                        });
                        $('.form_placeholder').css({ "scale": "0" })
                        // $(this).siblings('.updcard').css({ 'scale': '0' })
                      } else if(data.includes("no field should be empty")) {
                        swal({
                          title: "Failed!",
                          text: "one of the field is empty error",
                          icon: "error",
                        });
                      }else{
                        swal({
                          title: "Failed!",
                          text: "Something error! Please try again.",
                          icon: "error",
                        });
                      }
                    },
                  });
                })



                $(".fa-xmark").on("click",function(){
                  $(".form_placeholder").css({'scale':'0'})
                })


              }

              


            },
          });
        });

      


      },
    });
  });





});



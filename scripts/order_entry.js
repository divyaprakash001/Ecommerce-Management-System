$(document).ready(function () {

  $('input[type="text"]').focus(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });
  $('textarea').focus(function () {
    $(this).siblings('.lab').css({ 'top': '0rem' })
  });

  $(".search_btn").on("click", function () {
    window.location.href = "pages-search-order.html"
  })

  $(".add_btn").on('click', function () {
    window.location.href = "pages-order_entry_form.html";
  })
  $("#refresh").on('click', function () {
    window.location.reload()
  })
})


let order_id = '';

// doing insertion when click on submit button on product entry page
$("#sub_btn").on("click", function (e) {
  e.preventDefault();
  order_id = $("#order_id").val();
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "insert_order",
      order_id: order_id,
      user_id: $("#user_id").val(),
      order_date: $("#order_date").val(),
      shipping_addr: $("#shipping_addr").val(),
    }, success: function (response) {
      console.log(response);

      if (response.includes("order inserted successfully")) {
        swal({
          title: "Yeah!",
          text: "Data Inserted Successfully!",
          icon: "success",
        }).then((value) => {
          // location.reload();
          swal({
            title: "Do you want to buy product now?",
            text: "On clicking we are going on buy product page!",
            icon: "warning",
            buttons: true,
            // dangerMode: true,
          })
          .then((willDelete) => {
            if (willDelete) {
              localStorage.setItem("order_id",order_id);
              window.location.href = "pages-order_details_form.html"
            } else {
              swal("Buy amazing products at price!", { icon: "success" });
            }
          });



        })
      } else if (response.includes("Error !!! One of the field is empty")) {
        // alert("Error !!! One of the field is empty")
        swal({
          title: "Failed!",
          text: "One of the field is empty!",
          icon: "error",
        });
      }
      else if (response.includes("order already exists")) {
        // alert("Error !!! One of the field is empty")
        swal({
          title: "Failed!",
          text: "Order already exists!",
          icon: "error",
        });
      }
      else {
        swal({
          title: "Failed!",
          text: "sonethings error!",
          icon: "error",
        });
      }

    },
    error: function (errorData) {
      console.error(errorData)
    }
  })




});

// using ajax to send data to the python file
$.ajax({
  method: 'post',
  url: 'pythonf/signup2.py',
  data: {
    what: "fetchorderid"
  },
  success: function (data) {
    console.log(data);
    $('#order_id').append(data)
  },
});


$.ajax({
  method: 'post',
  url: 'pythonf/signup2.py',
  data: {
    what: "fetchuserid"
  },
  success: function (data) {
    console.log(data);
    $('#user_id').append(data)
  },
});

// code for display incoming data after executing query
$('#search_btn').on('click', function () {

  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "fetch_order_details_conditions",
      order_id: $('#order_id').val(),
      user_id: $('#user_id').val(),
      order_date: $('#order_date').val(),
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
      // $('.view').click(function () {
      //   $(this).siblings('.img_card').css({ 'scale': '1' })
      // })
      // $('.cut').click(function () {
      //   $('.img_card').css({ 'scale': '0' })
      // })


      // if user click on delete button
      $(".del").on("click", function () {
        d = "deleteorder"
        let oid = $(this).closest('tr').children('td:first-child').text();
        console.log(oid);

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
                  order_id: oid
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
        d = "fetchForOrderUpdate"

        

        let oid = $(this).closest('tr').children('td:first-child').text();
        // alert(pid)
        $.ajax({
          method: 'post',
          url: 'pythonf/signup2.py',
          data: {
            what: d,
            order_id: oid
          },
          success: function (data) {
            // alert("hello")
            console.log(data);
            if (data.includes("data fetching successfully")) {
              $('.form_placeholder').css({ 'scale': '1' })
              $(".form_placeholder").html(data)


              // code for saving the updated the data when use click on update button
              $(".save").on("click", function (e) {
                e.preventDefault();
                d = "saveorderupdate"


                $.ajax({
                  method: 'post',
                  url: 'pythonf/signup2.py',
                  data: {
                    what: d,
                    order_id1: $("#order_id1").val(),
                    user_id1: $("#user_id1").val(),
                    order_date1: $("#order_date1").val(),
                    shipping_addr1: $("#shipping_addr1").val(),
                  },
                  success: function (data) {
                    // window.location.href = 'showData.html'
                    console.log(data);

                    if (data.includes("successfully updated the order data")) {
                      swal({
                        title: "Success!",
                        text: "Data updated successfully",
                        icon: "success",
                      });
                      $('.form_placeholder').css({ "scale": "0" })
                      // $(this).siblings('.updcard').css({ 'scale': '0' })
                    } else if (data.includes("no field should be empty")) {
                      swal({
                        title: "Failed!",
                        text: "one of the field is empty error",
                        icon: "error",
                      });
                      $('.form_placeholder').css({ "scale": "0" })
                    } else {
                      swal({
                        title: "Failed!",
                        text: "Something error! Please try again.",
                        icon: "error",
                      });
                      $('.form_placeholder').css({ "scale": "0" })
                    }
                  },
                });
              })



              $(".fa-xmark").on("click", function () {
                $(".form_placeholder").css({ 'scale': '0' })
              })


            }




          },
        });
      });




    },
  });
});

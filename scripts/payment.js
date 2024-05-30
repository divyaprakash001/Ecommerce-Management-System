// const { default: state } = require("sweetalert/typings/modules/state");

$(document).ready(function () {

  $('input[type="text"]').focus(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });
  $('input[type="number"]').focus(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });
  $('textarea').focus(function () {
    $(this).siblings('.lab').css({ 'top': '0rem' })
  });

  $(".search_btn").on("click", function () {
    window.location.href = "pages-search_payment.html"
  })

  $(".add_btn").on('click', function () {
    window.location.href = "pages-payment_entry_form.html";
  })
  $("#refresh").on('click', function () {
    window.location.reload()
  })
})


// fetching user id from user_info table
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


// generating automatic userid
$.ajax({
  method: 'post',
  url: 'pythonf/signup2.py',
  data: {
    what: "generatePaymentId"
  },
  success: function (data) {
    // console.log(data);
    $('#payment_id').val(data)
  },
});


// Get the current date and time
var currentDate = new Date();

// Get the time zone offset in minutes
var timezoneOffsetInMinutes = currentDate.getTimezoneOffset();

// Adjust the current date by adding the offset
currentDate.setMinutes(currentDate.getMinutes() - timezoneOffsetInMinutes);

// Format the date and time in the required format (YYYY-MM-DDTHH:MM)
var formattedDate = currentDate.toISOString().slice(0, 16);

// Set the value of the datetime-local input element using jQuery
$("#order_date").val(formattedDate);



// doing insertion when click on submit button on product entry page
$(document).on("click", "#sub_btn", function (e) {
  e.preventDefault();

  // console.log(formData); // Output the array of input values


  // doing ajax call for data manipulation and insertion
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "insert_payment",
      "payment_id": $("#payment_id").val(),
      "order_id": $("#order_id").val(),
      "order_date": $("#order_date").val(),
      "payment_mode": $("#payment_mode").val(),
      "total_amount": $("#total_amount").val(),
    },
    success: function (data) {
      console.log(data);
      if (data.includes("payment success")) {
        swal({
          title: "Yeah!",
          text: "Payment Success!!!",
          icon: "success",
        }).then(() => {
          location.reload();
        })
      }
      else if (data.includes("one of the field is empty")) {
        swal({
          title: "Failed!",
          text: "One of the field is empty!!!",
          icon: "error",
        });
      } else if (data.includes("payment allready done")) {
        swal({
          title: "Failed!",
          text: "Payment Already Done!!!",
          icon: "error"
        })
      } else {
        swal({
          title: "Failed!",
          text: "Some error occured!!!",
          icon: "error"
        })
      }

    },
    error: function (errorData) {
      console.log('eeror is ', errorData);
    }
  })
});













// all operations for searching

// fetching category id
$.ajax({
  method: 'post',
  url: 'pythonf/signup2.py',
  data: {
    what: "fetchorderid"
  },
  success: function (data) {
    console.log(data);
    $('#order_id').append(data)
    // i++;
  },
});

$.ajax({
  method: 'post',
  url: 'pythonf/signup2.py',
  data: {
    what: "fetchPaymentId"
  },
  success: function (data) {
    console.log(data);
    $('#payment_id').append(data)
    // i++;
  },
});




// code for display incoming data after executing query
$("#search_btnn").on('click', function (e) {
  e.preventDefault()
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "fetch_payment_details_conditions",
      payment_id: $('#payment_id').val(),
      order_id: $('#order_id').val(),
      order_date: $('#order_date1').val(),
      payment_mode: $('#payment_mode').val(),
    },
    success: function (data) {
      // alert("hello")
      console.log(data);
      // alert(data)

      if (data.includes("please select one field")) {
        $('.below_card').css({ "display": "none" })
        swal({
          title: "Failed!",
          text: "please select atleast one field",
          icon: "error",
        });
      } else if (data.includes("payment details fetched successfully")) {
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
      else {
        // $('.below_card').css({ "display": "none" })
        swal({
          title: "Failed!",
          text: "Something went wrong!!!",
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
        d = "deletepayment"
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
                  payment_id: pid
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




      // edit button
      $(".edit").on("click", function () {
        d = "fetchForOrderUpdate"
        // alert(d)

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


            if (data.includes("order status is success")) {
              swal({
                title: "Failed!",
                text: "Can't Update Because Order Status Is Success!!!",
                icon: "error",
              });
            }
            else if (data.includes("data fetching successfully")) {
              // $('.form_placeholder').css({ 'scale': '1' })
              // $(".form_placeholder").html(data)
              var originalString = data;

              // Remove the last '&&'
              if (originalString.endsWith("&&")) {
                originalString = originalString.slice(0, -2);
              }

              // Split the string into a list using the separator '&&'
              var splitArray = originalString.split("&&");

              console.log(splitArray);
              localStorage.setItem("order_data", JSON.stringify(splitArray))
              window.location.href = "pages-order_update.html";



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

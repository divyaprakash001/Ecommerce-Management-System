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
    window.location.href = "pages-search-order.html"
  })

  $(".add_btn").on('click', function () {
    window.location.href = "pages-order_entry_form.html";
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
    what: "generateOrderId"
  },
  success: function (data) {
    // console.log(data);
    $('#order_id').val(data)
    // i++;
  },
});


// Get the current date and time
var currentDate = new Date();

// Format the date and time in the required format (YYYY-MM-DDTHH:MM)
var formattedDate = currentDate.toISOString().slice(0, 16);
// alert(formattedDate)
// Set the value of the datetime-local input element using jQuery
$("#order_date").val(formattedDate);


let stateData = `
<option value="" selected disabled>----- Select Any State -----</option>
<option value="Andhra Pradesh">Andhra Pradesh</option>
<option value="Arunachal Pradesh">Arunachal Pradesh</option>
<option value="Assam">Assam</option>
<option value="Bihar">Bihar</option>
<option value="Chandigarh">Chandigarh</option>
<option value="Chattisgarh">Chattisgarh</option>
<option value="Delhi">Delhi</option>
<option value="Goa">Goa</option>
<option value="Gujarat">Gujarat</option>
<option value="Haryana">Haryana</option>
<option value="Himachal Pradesh">Himachal Pradesh</option>
<option value="jammu & Kashmir">Jammu & Kashmir</option>
<option value="Jharkhand">Jharkhand</option>
<option value="Karnataka">Karnataka</option>
<option value="Kerala">Kerala</option>
<option value="Lakshadweep">Lakshadweep</option>
<option value="Madhya Pradesh">Madhya Pradesh</option>
<option value="Maharashtra">Maharashtra</option>
<option value="Manipur">Manipur</option>
<option value="Meghalaya">Meghalaya</option>
<option value="Mizoram">Mizoram</option>
<option value="Odisha">Odisha</option>
<option value="Punjab">Punjab</option>
<option value="Rajasthan">Rajasthan</option>
<option value="Sikkim">Sikkim</option>
<option value="Tamil Nadu">Tamil Nadu</option>
<option value="Telangana">Telangana</option>
<option value="Tripura">Tripura</option>
<option value="Uttar Pradesh">Uttar Pradesh</option>
<option value="Uttarakhand">Uttarakhand</option>
<option value="West Bengal">West Bengal</option>
<option value="Andaman & Nicobar">Andaman & Nicobar</option>
<option value="Dadra & Nagar Haveli and Daman & Diu">Dadra & Nagar Haveli and Daman
  & Diu</option>
<option value="Pondicherry">Pondicherry</option>
<option value="Nagaland"> Nagaland</option>
`

$("#country").on("change", function () {
  // alert($("#country").val())
  if ($("#country").val() == "India") {
    $("#state").html(stateData)
  }
})

$("#state").on("change", function () {
  // alert($(this).val())
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      state_name: $('#state').val(),
      what: "fetchDistrict"
    },
    success: function (data) {
      // console.log(data);
      // $(".prod_id").empty()
      $(`#district`).html(data)
      // j++;
    },
  });
})



// let i = 0;

$.ajax({
  method: 'post',
  url: 'pythonf/signup2.py',
  data: {
    what: "fetchcatid"
  },
  success: function (data) {
    // console.log(data);
    $(`.prod_cat_0`).append(data)
    // i++;
  },
});

// let j=0;

// on change of prod_cat fetch product id for product name
$(document).on('change', `.prod_cat_0`, function () {

  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      prod_cat_id: $(this).val(),
      what: "fetchprodid"
    },
    success: function (data) {
      // console.log(data);
      // $(".prod_id").empty()
      $(`.prod_id_0`).html(data)
      // j++;
    },
  });
});



// doing insertion when click on submit button on product entry page
$(document).on("click", "#sub_btn", function (e) {
  e.preventDefault();

  // Collect form data
  let formData = {
    // "what": 'insert_order',
    "user_id": $("#user_id").val(),
    "order_id": $("#order_id").val(),
    "order_date": $("#order_date").val(),
    "country": $("#country").val(),
    "state": $("#state").val(),
    "district": $("#district").val(),
    "city": $("#city").val(),
    "pincode": $("#pincode").val(),
    "landmark": $("#landmark").val(),
    products: []  //keeping the dict data of product in array
  };

// iterating the no. of each rows start with class prod_row
  $("[class^='prod_row']").each(function () {
    // keeping the data in dictionary form
    var prod = {
      prod_cat: $(this).find("select[class^='prod_cat_']").val(), // Get the value of each input element
      prod_id: $(this).find("select[class^='prod_id_']").val(), // Get the value of each input element
      prod_quantity: $(this).find("[class^='quantity']").val() // Get the value of each input element
    }
    formData.products.push(prod); // Add the value to the array
  });

  // console.log(formData); // Output the array of input values


// doing ajax call for data manipulation and insertion
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "insert_order2",
      formData: JSON.stringify(formData)
    },
    success: function (data) {
      console.log(data);
      if (data.includes("Order inserted successfully")) {
        swal({
          title: "Yeah!",
          text: "Your Order Placed!!!",
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
      } else if (data.includes("order already exists")) {
        swal({
          title: "Failed!",
          text: "Order already exists!!!",
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

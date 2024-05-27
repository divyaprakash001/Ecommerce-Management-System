$(document).ready(function () {
  $('input[type="text"]').focus(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });
  $('input[type="number"]').focus(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });

  $("#refresh").on('click', function () {
    window.location.reload()
  })




  var amount = null;
  let prod_id = null;


  let order_id = localStorage.getItem("order_id");
  $(".order_id").val(order_id)

  // fetch product id
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "fetchprodid",
      // prod_id: prod_id
    },
    success: function (data) {
      console.log(data);
      $(".prod_id").append(data)
    },
  })


    // .then(() => {

      $(".prod_id, .quantity").on("focusout", function () {
        prod_id = $(".prod_id").val();
        quantity = $(".quantity").val();

        // alert(prod_id )
        // alert(quantity )
        if (prod_id && quantity) {
          // alert(prod_id)
          $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
              what: "fetchproductprice",
              prod_id: prod_id
            },
            success: function (data) {
              console.log(data);
              amount = parseInt(data) * parseInt($(".quantity").val())
              $(".amount").val(amount)
            },
          });
        }

      })
    // })
  //   $(document).on("change", ".prod_id, .quantity", function () {
  //     var prod_id = $(this).closest('tr').find('.prod_id').val();
  //     var quantity = $(this).closest('tr').find('.quantity').val();

  //     if (prod_id && quantity) { // Check if both fields are filled
  //         $.ajax({
  //             method: 'post',
  //             url: 'pythonf/signup2.py',
  //             data: {
  //                 what: "fetchproductprice",
  //                 prod_id: prod_id
  //             },
  //             success: function (data) {
  //                 console.log(data);
  //                 var amount = parseInt(data) * parseInt(quantity);
  //                 $(this).closest('tr').find('.amount').val(amount);
  //             }.bind(this), // Ensure "this" refers to the correct element
  //             error: function (xhr, status, error) {
  //                 console.error("Error:", error);
  //             }
  //         });
  //     }
  // });

});

// console.log(prod_id);



// doing insertion when click on submit button on product entry page
$("#sub_btn").on("click", function (e) {
  e.preventDefault();


  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: "insert_final_order",
      order_id: $("#order_id").val(),
      prod_id: $("#prod_id").val(),
      quantity: $("#quantity").val(),
      amount: $("#amount").val(),
    }, success: function (response) {
      console.log(response);

      if (response.includes("order details inserted successfully")) {
        swal({
          title: "Yeah!",
          text: "Order Details Inserted Successfully!",
          icon: "success",
        }).then((value) => {
          location.reload();
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









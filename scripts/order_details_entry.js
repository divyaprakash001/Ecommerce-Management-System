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


  $(".fa-plus").on("click", function () {
    var newRow = $("#myForm tbody tr:last").prev().clone();
    newRow.find(".addRowIcon").removeClass("fa-plus").addClass("fa-minus");
    // newRow.find(".addRowIcon").removeClass("addRowIcon").addClass("removeRowIcon");
    newRow.insertBefore("#myForm tbody tr:last");
  })

 

  // on click of minus icon, row deleted
  $(".removeRowIcon").on("click", function () {
    alert("helo")
    $(this).closest("tr").remove();
  })




  var amount = null;
  let prod_id = null

  // // fetch order id
  // $.ajax({
  //   method: 'post',
  //   url: 'pythonf/signup2.py',
  //   data: {
  //     what: "fetchorderid"
  //   },
  //   success: function (data) {
  //     console.log(data);
  //     $('#order_id').append(data)
  //   },
  // });


  let order_id = localStorage.getItem("order_id");
  // alert(order_id)
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

      $(".same_change").on("focusout", function () {
        prod_id = $(".prod_id").val();
        quantity = $(".quantity").val();

        // alert(prod_id )
        // alert(quantity )
        if ((prod_id != null || prod_id != '') && (quantity != null || quantity != '')) {
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
              amount = parseInt(data) * parseInt($("#quantity").val())
              $(".amount").val(amount)
            },
          });
        }

      })
    // })



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

  // using ajax to send data to the python file









})





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




// using ajax to send data to the python file
$(document).ready(function () {
  d = "fetchcatid"
  $.ajax({
    method: 'post',
    url: 'pythonf/signup2.py',
    data: {
      what: d
    },
    success: function (data) {
      console.log(data);
      $('#mySelect').append(data)
    },
  });
})




// code for display incoming data after executing query
$(document).ready(function () {
  $('#search_sub_btn').on('click', function () {
    // alert("searching")
    pro_cat_id1 = $('#mySelect').val()
    pro_cat_name1 = $('#pro_cat_name').val()

    $.ajax({
      method: 'post',
      url: 'pythonf/signup2.py',
      data: {
        what: "fetch_by_catid_catname",
        pro_cat_id: pro_cat_id1,
        pro_cat_name: pro_cat_name1,
      },
      success: function (data) {
        console.log(data);
        // alert(data)

        if (data.includes("please select one field")) {
          // $(".msg").text("please select atleast one field")
          // $(".msg").css({ "color": "red" , "display":"block"})
          $('.below_card').css({ "display": "none" })
          swal({
            title: "Failed!",
            text: "please select atleast one field",
            icon: "error",
          });
        } else if (data.includes("product category fetched successfully")) {
          $(".msg").css({ "display": "none" })
          $('.below_card').css({ "display": "block" })
          $('.table_container').html(data)
        } else if (data.includes("no data available")) {
          // $(".msg").text("no data available")
          // $(".msg").css({ "color": "red", "display":"block" })
          $('.below_card').css({ "display": "none" })
          swal({
            title: "Failed!",
            text: "no data available",
            icon: "error",
          });
        }

        $(".table_container").html(data)

        // if user click on delete button
        $(".del").on("click", function () {
          d = "deletecat"
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
                    pro_cat_id: pid
                  },
                  success: function (data) {
                    console.log(data);
                    if (data.includes("data deleted successfully")) {
                      swal("Yeah! Your data has been deleted!", {
                        icon: "success",
                      });
                    }
                  },
                });
                $(this).closest('tr').remove();
              } else {
                swal("Your data is safe!", {icon:"success"});
              }
            });

        })

        // code for update the data when use click on update button
        $(".update").on("click", function () {
          d = "fetchForcatUpdate"
          let pcid = $(this).closest('tr').children('td:first-child').text();
          // console.log(uid);

          $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
              what: d,
              pro_cat_id: pcid
            },
            success: function (data) {
              console.log(data);
              if (data.includes("data fetching successfully")) {
                $("#table_container").css({ "display": "none" })
                $("#myform").css({ "display": "none" })
                $(".form_placeholder").css({ "display": "block" })
                $(".form_placeholder").html(data)
              }

              $(".form_placeholder .fa-xmark").on("click",function(){
                  $(".form_placeholder").css({"display":"none"});
              })

              // code for saving the updated the data when use click on update button
              $("#save").on("click", function () {
                d = "savethecatupdate"
                pcid = $("#pcid").val();
                pcname = $("#pcname").val();
                pcdesc = $("#pcdesc").val();

                $.ajax({
                  method: 'post',
                  url: 'pythonf/signup2.py',
                  data: {
                    what: d,
                    pro_cat_id: pcid,
                    pro_cat_name: pcname,
                    pro_cat_desc: pcdesc,
                  },
                  success: function (data) {
                    // window.location.href = 'showData.html'
                    console.log(data);

                    if (data.includes("successfully saved")) {
                      swal({
                        title: "Success!",
                        text: "Data updated successfully",
                        icon: "success",
                      });
                      $('.form_placeholder').css({ "display": "none" })
                    } else {
                      swal({
                        title: "Failed!",
                        text: "somethings error",
                        icon: "error",
                      });
                    }
                  },
                });
              })
            },
          });
        })
      },
    });
  })
})





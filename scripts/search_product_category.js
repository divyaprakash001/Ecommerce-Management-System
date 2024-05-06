

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

        $(".table_container").html(data)

        if (data.includes("please select one field")) {
          $(".msg").text("please select atleast one field")
          $(".msg").css({ "color": "red" })
        } else if (data.includes("product category fetched successfully")) {
          $(".msg").css({ "display": "none" })
          $('.below_card').css({ "display": "block" })
          $('.table_container').html(data)
        } else if (data.includes("no data available")) {
          // alert('empty result set')
          $(".msg").text("no data is available")
          $(".msg").css({ "color": "red" })
        }


        // if user click on delete button
        $(".del").on("click", function () {
          d = "delete"
          let uid = $(this).closest('tr').children('td:first-child').text();
          console.log(uid);

          $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
              what: d,
              userid: uid
            },
            success: function (data) {
              console.log(data);
              if (data.includes("data deleted successfully")) {
                console.log("ho gyaa dlete");
              }
            },
          });
          $(this).closest('tr').remove();


          // let v = $(this).closest('tr').remove();
          // console.log(v);
        })

        // code for update the data when use click on update button
        $(".update").on("click", function () {
          d = "fetchForUpdate"
          let uid = $(this).closest('tr').children('td:first-child').text();
          // console.log(uid);

          $.ajax({
            method: 'post',
            url: 'pythonf/signup2.py',
            data: {
              what: d,
              userid: uid
            },
            success: function (data) {
              console.log(data);
              if (data.includes("data fetching successfully")) {
                $("#table_container").css({ "display": "none" })
                $("#myform").css({ "display": "none" })
                $(".form_placeholder").html(data)
              }

              // code for saving the updated the data when use click on update button
              $("#save").on("click", function () {
                d = "savetheupdate"
                uid1 = $("#uid").val();
                uname1 = $("#uname").val();
                uemail1 = $("#uemail").val();
                umob1 = $("#umob").val();

                $.ajax({
                  method: 'post',
                  url: 'pythonf/signup2.py',
                  data: {
                    what: d,
                    uid: uid1,
                    uname: uname1,
                    uemail: uemail1,
                    umob: umob1
                  },
                  success: function (data) {
                    // window.location.href = 'showData.html'
                    console.log(data);

                    if (data.includes("successfully saved")) {
                      if (data.includes("successfully saved")) {
                        $(".msg").css({ "display": "block", "color": "green" });
                        $(".msg").text("data updated successfully");
                      } else {
                        $(".msg").css({ "display": "block", "color": "red" });
                        $(".msg").text("data updation failed. Some error occured.");
                      }
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





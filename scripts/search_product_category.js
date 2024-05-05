

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
  




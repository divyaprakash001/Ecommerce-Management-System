$(document).ready(function () {

  $('input[type="text"]').click(function () {
    $(this).siblings('.lab').css({ 'top': '-.4rem' })
  });
  $('textarea').click(function () {
    $(this).siblings('.lab').css({ 'top': '-.5rem' })
  });

  $(".search_btn").on("click",function(){
    window.location.href = "pages-search-product_details.html"
  })

  $(".add_btn").on('click', function () {
    window.location.href = "pages-product_entry_form.html";
  })
})

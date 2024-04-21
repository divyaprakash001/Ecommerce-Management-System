$(function(){

     // loading navbar on all pages
     $("#nav_placeholder").load("nav.html")

    $('input[type="text"]').click(function(){
        $(this).siblings('label').css({'top':'0rem'})
    })
})
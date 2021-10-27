$(document).ready(function(){
    $('img').click(function(){
        $(this).fadeOut(1600)
    })
    $('.btn').click(function() {
        $('img').fadeIn(1600)
    })
})
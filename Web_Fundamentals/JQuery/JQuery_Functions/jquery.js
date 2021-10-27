$(document).ready(function() {
    $('#addClass .btn').click( function() { 
        $('#addClass .descript').addClass('red') 
    });
    
    $('#slideToggle .btn').click(function() {
        $('#road-runner').slideToggle()
    });

    $('#append .btn').click(function() {
        $('#append .descript').append("<br>This is a new paragraph appeneded to the end of the last one.")
    });

    $('#hideShow .hide').click(function(){
        $('#hideShow p').hide()
    });
    $('#hideShow .show').click(function(){
        $('#hideShow p').show()
    });


    $('#fadeInOut .fadeOut').click(function(){
        $('#fadeInOut #boo').fadeOut(1600)
    });
    $('#fadeInOut .fadeIn').click(function(){
        $('#fadeInOut #boo').fadeIn(1600)
    });
})

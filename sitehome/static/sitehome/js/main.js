$(document).ready(function () {
    
    if(screen.width <= 440){
        $('.menu').hide();

        $('.burger').click(function (e) { 
            e.preventDefault();
            $('.menu').slideToggle();
        });
    }

    if(screen.width > 440){
        $('.burger').hide();

        $('nav').addClass('nav-bar');

        var contactIMG = $('.contact-img').html();    
        $('.contact-img').remove();
        var div = '<div class="contact-img">' + contactIMG + '</div>';
        $('.down').prepend(div);
    }

    

    
});
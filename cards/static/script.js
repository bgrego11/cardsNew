/*global $, document, setTimeout, i*/
$(document).ready(function () {

    'use strict';

    var slide  = $('.slide'),
        slideAelements = $('.slide-a-child'),
        slideBelements = $('.slide-b-child'),
        slideCelements = $('.slide-c-child'),
        slideDelements = $('.slide-d-child'),
        replay = $('button.replay');



    slide.each(function (i) {
        if (i < 3) {
            setTimeout(function () {
                slide.eq(i).fadeOut();
            }, 5000 * (i + 1));
        }
    });


    function animateSlideA() {
      slideAelements.each(function (i) {
          setTimeout(function () {
              slideAelements.eq(i).addClass('is-visible');
          }, 300 * (i + 1));
      });
    }

    function animateSlideB() {
      slideBelements.each(function (i) {
          setTimeout(function () {
              slideBelements.eq(i).addClass('is-visible');
          }, 300 * (i + 1));
      });
   }

     function animateSlideC() {
      slideCelements.each(function (i) {
          setTimeout(function () {
              slideCelements.eq(i).addClass('is-visible');
          }, 150 * (i + 1));
      });
    }

    function animateSlideD() {
      slideDelements.each(function (i) {
          setTimeout(function () {
              slideDelements.eq(i).addClass('is-visible');
          }, 300 * (i + 1));
      });
    }

    animateSlideA();

    setTimeout(function () {
       animateSlideB();
    }, 3000);

    setTimeout(function () {
       animateSlideC();
    }, 7000);

    setTimeout(function () {
       animateSlideD();
    }, 10000);


   replay.on('click', function () {
     location.reload(true);
   });


// sidebar nav functions
$("#sidebar").mCustomScrollbar({
    theme: "minimal"
});

$('#dismiss, .overlay').on('click', function () {
    $('#sidebar').removeClass('active');
    $('.overlay').fadeOut();
});

$('#sidebarCollapse').on('click', function () {
    $('#sidebar').addClass('active');
    $('.overlay').fadeIn();
    $('.collapse.in').toggleClass('in');
    $('a[aria-expanded=true]').attr('aria-expanded', 'false');
});


});


$('#register').on('click', function (){
    user = {
        username: $('#username').val(),
        password: $('#password').val()
    }

    
    $.post('../register', user).then(function(data) {
        console.log(data)
    });
    $('#username').val(''),
    $('#password').val('')
})

$('#auth').on('click', function (){
    
    user = {
        username: $('#username').val(),
        password: $('#password').val()
    }
    console.log(user)
    $.ajax({
        url: "../auth",
        type: "POST",
        data: user,
        dataType: "json",
        success: function (result) {
            switch (result) {
                case true:
                    processResponse(result);
                    break;
                default:
                   console.log(result);
            }
        },
        error: function (xhr, ajaxOptions, thrownError) {
        alert(xhr.status);
        alert(thrownError);
        }
    });

    
})
var main = function() {
  /* Push the body and the nav over by 200px over */
 /* $('.icon-menu').click(function() {
    $('.menu').animate({
      right: "0px"
    }, 200);

  });*/

  /* Then push them back */
  /*$('.icon-close').click(function() {
    $('.menu').animate({
      right: "-200px"
    }, 200);

  });*/
  $('.icon-toggle').click(function() {
    $('.menu').toggle();
  });

  $(window).resize(function() {
        // This will fire each time the window is resized:
        if($(window).width() >= 768) {
            // if larger or equal
            $('.menu').hide();
        }
    });
  
};

$(document).ready(main);